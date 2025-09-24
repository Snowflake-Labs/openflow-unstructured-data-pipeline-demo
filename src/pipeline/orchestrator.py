"""
Main orchestrator for the unstructured data pipeline.
Coordinates Google Drive extraction, document processing, and Snowflake intelligence generation.
"""
import os
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
import time

from ..google_drive.client import GoogleDriveClient
from ..snowflake.client import SnowflakeClient
from .processor import DocumentProcessor

class PipelineOrchestrator:
    """Main orchestrator for the unstructured data to intelligence pipeline."""
    
    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Initialize clients
        self.google_drive_client = GoogleDriveClient(
            credentials_file=config.get('GOOGLE_DRIVE_CREDENTIALS_FILE'),
            token_file=config.get('GOOGLE_DRIVE_TOKEN_FILE', 'config/token.json')
        )
        
        snowflake_params = {
            'account': config.get('SNOWFLAKE_ACCOUNT'),
            'user': config.get('SNOWFLAKE_USER'),
            'password': config.get('SNOWFLAKE_PASSWORD'),
            'database': config.get('SNOWFLAKE_DATABASE', 'UNSTRUCTURED_DEMO'),
            'schema': config.get('SNOWFLAKE_SCHEMA', 'INTELLIGENCE'),
            'warehouse': config.get('SNOWFLAKE_WAREHOUSE', 'COMPUTE_WH'),
            'role': config.get('SNOWFLAKE_ROLE', 'ACCOUNTADMIN')
        }
        
        self.snowflake_client = SnowflakeClient(snowflake_params)
        self.document_processor = DocumentProcessor()
        
        # Pipeline configuration
        self.batch_size = int(config.get('BATCH_SIZE', 10))
        self.processing_threads = int(config.get('PROCESSING_THREADS', 4))
        self.cortex_model = config.get('CORTEX_MODEL', 'mistral-7b')
        
    def initialize_infrastructure(self) -> bool:
        """Initialize the required infrastructure (databases, tables, search services)."""
        try:
            self.logger.info("Initializing Snowflake infrastructure...")
            
            # Connect to Snowflake and create tables
            self.snowflake_client.connect()
            self.snowflake_client.create_tables()
            
            # Create Cortex Search service
            self.snowflake_client.create_cortex_search_service()
            
            self.logger.info("Infrastructure initialization completed")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to initialize infrastructure: {e}")
            return False
    
    def run_full_pipeline(self, google_drive_folder_id: str) -> Dict[str, Any]:
        """
        Run the complete pipeline from Google Drive to Strategic Intelligence.
        
        Args:
            google_drive_folder_id: Google Drive folder ID containing business documents
            
        Returns:
            Pipeline execution results
        """
        pipeline_start_time = datetime.now()
        results = {
            'pipeline_id': f"pipeline_{int(pipeline_start_time.timestamp())}",
            'start_time': pipeline_start_time,
            'status': 'running',
            'stages': {},
            'metrics': {}
        }
        
        try:
            # Stage 1: Document Discovery
            self.logger.info("Stage 1: Discovering business documents from Google Drive...")
            discovery_start = time.time()
            
            documents = self.google_drive_client.get_business_documents(google_drive_folder_id)
            
            results['stages']['discovery'] = {
                'status': 'completed',
                'duration_seconds': time.time() - discovery_start,
                'documents_found': len(documents),
                'categories': list(set(doc.get('strategic_category') for doc in documents))
            }
            
            if not documents:
                results['status'] = 'completed'
                results['message'] = 'No business documents found in the specified folder'
                return results
            
            # Stage 2: Document Download and Processing
            self.logger.info(f"Stage 2: Processing {len(documents)} documents...")
            processing_start = time.time()
            
            processed_docs = self._process_documents_batch(documents)
            
            results['stages']['processing'] = {
                'status': 'completed',
                'duration_seconds': time.time() - processing_start,
                'documents_processed': len(processed_docs),
                'successful_extractions': len([d for d in processed_docs if not d.get('error')]),
                'failed_extractions': len([d for d in processed_docs if d.get('error')])
            }
            
            # Stage 3: Intelligence Generation
            self.logger.info("Stage 3: Generating strategic intelligence insights...")
            intelligence_start = time.time()
            
            intelligence_results = self._generate_intelligence_insights(processed_docs)
            
            results['stages']['intelligence'] = {
                'status': 'completed',
                'duration_seconds': time.time() - intelligence_start,
                'insights_generated': len(intelligence_results),
                'avg_confidence': sum(r.get('confidence_score', 0) for r in intelligence_results) / len(intelligence_results) if intelligence_results else 0,
                'avg_strategic_value': sum(r.get('strategic_value', 0) for r in intelligence_results) / len(intelligence_results) if intelligence_results else 0
            }
            
            # Stage 4: Search Index Creation
            self.logger.info("Stage 4: Creating search indexes...")
            search_start = time.time()
            
            search_results = self._create_search_indexes(processed_docs)
            
            results['stages']['search'] = {
                'status': 'completed',
                'duration_seconds': time.time() - search_start,
                'documents_indexed': search_results.get('indexed_count', 0)
            }
            
            # Final metrics
            results['end_time'] = datetime.now()
            results['total_duration_seconds'] = (results['end_time'] - results['start_time']).total_seconds()
            results['status'] = 'completed'
            
            # Generate summary metrics
            results['metrics'] = self._generate_pipeline_metrics(results)
            
            self.logger.info(f"Pipeline completed successfully in {results['total_duration_seconds']:.2f} seconds")
            
        except Exception as e:
            results['status'] = 'failed'
            results['error'] = str(e)
            results['end_time'] = datetime.now()
            self.logger.error(f"Pipeline failed: {e}")
        
        return results
    
    def _process_documents_batch(self, documents: List[Dict]) -> List[Dict[str, Any]]:
        """Process documents in batches."""
        processed_docs = []
        
        for i in range(0, len(documents), self.batch_size):
            batch = documents[i:i + self.batch_size]
            self.logger.info(f"Processing batch {i//self.batch_size + 1} ({len(batch)} documents)")
            
            for document in batch:
                try:
                    # Download document
                    file_path = self.google_drive_client.download_file(
                        document['id'],
                        document['name']
                    )
                    
                    if not file_path:
                        continue
                    
                    # Insert document metadata
                    document['download_path'] = file_path
                    doc_id = self.snowflake_client.insert_document_metadata(document)
                    
                    # Extract content
                    content_result = self.document_processor.extract_content(
                        file_path, document.get('mimeType')
                    )
                    
                    if content_result.get('error'):
                        self.logger.warning(f"Content extraction failed for {document['name']}: {content_result['error']}")
                        continue
                    
                    # Chunk content for processing
                    chunks = self.document_processor.chunk_content(content_result['content'])
                    
                    for chunk in chunks:
                        content_id = self.snowflake_client.insert_document_content(
                            doc_id,
                            chunk['content'],
                            content_result.get('file_type', 'text'),
                            chunk.get('chunk_number', 1)
                        )
                    
                    processed_doc = {
                        'doc_id': doc_id,
                        'original_document': document,
                        'content_result': content_result,
                        'chunks': chunks,
                        'file_path': file_path
                    }
                    
                    processed_docs.append(processed_doc)
                    
                except Exception as e:
                    self.logger.error(f"Error processing document {document.get('name', 'unknown')}: {e}")
        
        return processed_docs
    
    def _generate_intelligence_insights(self, processed_docs: List[Dict]) -> List[Dict[str, Any]]:
        """Generate strategic intelligence insights for processed documents."""
        intelligence_results = []
        
        for doc in processed_docs:
            if doc.get('content_result', {}).get('error'):
                continue
            
            try:
                content = doc['content_result']['content']
                if not content or len(content.strip()) < 100:  # Skip very short content
                    continue
                
                self.logger.info(f"Generating insights for document: {doc['doc_id']}")
                
                # Generate insights using Cortex AI
                insights = self.snowflake_client.generate_intelligence_insights(
                    doc['doc_id'],
                    content,
                    self.cortex_model
                )
                
                if insights:
                    # Insert insights into database
                    insight_id = self.snowflake_client.insert_intelligence_insights(insights)
                    insights['insight_id'] = insight_id
                    intelligence_results.append(insights)
                
            except Exception as e:
                self.logger.error(f"Error generating insights for {doc['doc_id']}: {e}")
        
        return intelligence_results
    
    def _create_search_indexes(self, processed_docs: List[Dict]) -> Dict[str, Any]:
        """Create search indexes for intelligent querying."""
        search_results = {'indexed_count': 0}
        
        try:
            # Update document processing status
            for doc in processed_docs:
                if not doc.get('content_result', {}).get('error'):
                    # Mark content as completed for search indexing
                    self.snowflake_client.session.sql(f"""
                        UPDATE DOCUMENT_CONTENT 
                        SET PROCESSING_STATUS = 'COMPLETED'
                        WHERE DOC_ID = '{doc['doc_id']}'
                    """).collect()
                    
                    search_results['indexed_count'] += 1
            
            self.logger.info(f"Updated processing status for {search_results['indexed_count']} documents")
            
        except Exception as e:
            self.logger.error(f"Error creating search indexes: {e}")
        
        return search_results
    
    def _generate_pipeline_metrics(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive pipeline metrics."""
        metrics = {
            'total_execution_time': results.get('total_duration_seconds', 0),
            'documents_per_second': 0,
            'success_rate': 0,
            'stage_performance': {}
        }
        
        try:
            # Calculate documents per second
            total_docs = results['stages'].get('discovery', {}).get('documents_found', 0)
            if total_docs > 0 and results.get('total_duration_seconds', 0) > 0:
                metrics['documents_per_second'] = total_docs / results['total_duration_seconds']
            
            # Calculate success rate
            processed = results['stages'].get('processing', {}).get('documents_processed', 0)
            successful = results['stages'].get('processing', {}).get('successful_extractions', 0)
            if processed > 0:
                metrics['success_rate'] = successful / processed
            
            # Stage performance
            for stage, data in results['stages'].items():
                duration = data.get('duration_seconds', 0)
                metrics['stage_performance'][stage] = {
                    'duration_seconds': duration,
                    'percentage_of_total': (duration / results.get('total_duration_seconds', 1)) * 100
                }
        
        except Exception as e:
            self.logger.error(f"Error generating metrics: {e}")
        
        return metrics
    
    def search_intelligence(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search the processed business intelligence using Cortex Search.
        
        Args:
            query: Search query
            limit: Maximum number of results
            
        Returns:
            List of search results
        """
        try:
            results = self.snowflake_client.search_business_intelligence(query, limit=limit)
            
            self.logger.info(f"Search query '{query}' returned {len(results)} results")
            return results
            
        except Exception as e:
            self.logger.error(f"Error searching intelligence: {e}")
            return []
    
    def get_strategic_dashboard(self) -> Dict[str, Any]:
        """Get strategic intelligence dashboard data."""
        try:
            dashboard_data = self.snowflake_client.get_strategic_dashboard_data()
            
            # Enhance with additional metrics
            dashboard_data['recent_activity'] = self._get_recent_activity()
            dashboard_data['top_insights'] = self._get_top_insights()
            
            return dashboard_data
            
        except Exception as e:
            self.logger.error(f"Error getting dashboard data: {e}")
            return {}
    
    def _get_recent_activity(self) -> List[Dict[str, Any]]:
        """Get recent pipeline activity."""
        try:
            query = """
            SELECT 
                DOC_ID,
                FILE_NAME,
                STRATEGIC_CATEGORY,
                PROCESSED_TIME
            FROM DOCUMENTS
            WHERE PROCESSED_TIME >= CURRENT_DATE - 7
            ORDER BY PROCESSED_TIME DESC
            LIMIT 10
            """
            
            results = self.snowflake_client.session.sql(query).collect()
            return [row.as_dict() for row in results]
            
        except Exception as e:
            self.logger.error(f"Error getting recent activity: {e}")
            return []
    
    def _get_top_insights(self) -> List[Dict[str, Any]]:
        """Get top strategic insights by value."""
        try:
            query = """
            SELECT 
                ii.TITLE,
                ii.SUMMARY,
                ii.STRATEGIC_VALUE,
                ii.CONFIDENCE_SCORE,
                d.FILE_NAME,
                d.STRATEGIC_CATEGORY
            FROM INTELLIGENCE_INSIGHTS ii
            JOIN DOCUMENTS d ON ii.DOC_ID = d.DOC_ID
            ORDER BY ii.STRATEGIC_VALUE DESC, ii.CONFIDENCE_SCORE DESC
            LIMIT 5
            """
            
            results = self.snowflake_client.session.sql(query).collect()
            return [row.as_dict() for row in results]
            
        except Exception as e:
            self.logger.error(f"Error getting top insights: {e}")
            return []
    
    def cleanup(self):
        """Clean up resources."""
        try:
            if self.snowflake_client:
                self.snowflake_client.close()
                
            self.logger.info("Pipeline orchestrator cleanup completed")
            
        except Exception as e:
            self.logger.error(f"Error during cleanup: {e}")