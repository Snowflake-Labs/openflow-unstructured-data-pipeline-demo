"""
Snowflake client for storing and processing unstructured documents with Cortex AI.
"""
import os
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
import json

import snowflake.connector
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col, lit
from snowflake.snowpark.types import StructType, StructField, StringType, TimestampType, IntegerType

class SnowflakeClient:
    """Client for interacting with Snowflake for document storage and Cortex AI processing."""
    
    def __init__(self, connection_params: Dict[str, str]):
        self.connection_params = connection_params
        self.session = None
        self.logger = logging.getLogger(__name__)
        
    def connect(self) -> None:
        """Establish connection to Snowflake."""
        try:
            self.session = Session.builder.configs(self.connection_params).create()
            self.logger.info("Successfully connected to Snowflake")
            
            # Set up database and schema
            database = self.connection_params.get('database', 'UNSTRUCTURED_DEMO')
            schema = self.connection_params.get('schema', 'INTELLIGENCE')
            
            self.session.sql(f"USE DATABASE {database}").collect()
            self.session.sql(f"USE SCHEMA {schema}").collect()
            
        except Exception as e:
            self.logger.error(f"Failed to connect to Snowflake: {e}")
            raise
    
    def create_tables(self) -> None:
        """Create necessary tables for the unstructured data pipeline."""
        if not self.session:
            self.connect()
        
        # Create documents table
        create_documents_table = """
        CREATE TABLE IF NOT EXISTS DOCUMENTS (
            DOC_ID VARCHAR(255) PRIMARY KEY,
            FILE_NAME VARCHAR(500),
            FILE_TYPE VARCHAR(100),
            SOURCE_FOLDER VARCHAR(255),
            STRATEGIC_CATEGORY VARCHAR(100),
            EXTRACTION_PRIORITY INTEGER,
            FILE_SIZE_BYTES INTEGER,
            CREATED_TIME TIMESTAMP,
            MODIFIED_TIME TIMESTAMP,
            PROCESSED_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
            DOWNLOAD_PATH VARCHAR(1000),
            WEB_VIEW_LINK VARCHAR(1000),
            METADATA VARIANT
        )
        """
        
        # Create document content table
        create_content_table = """
        CREATE TABLE IF NOT EXISTS DOCUMENT_CONTENT (
            CONTENT_ID VARCHAR(255) PRIMARY KEY,
            DOC_ID VARCHAR(255),
            RAW_CONTENT TEXT,
            PROCESSED_CONTENT TEXT,
            CONTENT_TYPE VARCHAR(100),
            PAGE_NUMBER INTEGER,
            CHUNK_NUMBER INTEGER,
            CHUNK_SIZE INTEGER,
            PROCESSING_STATUS VARCHAR(50) DEFAULT 'PENDING',
            CREATED_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
            FOREIGN KEY (DOC_ID) REFERENCES DOCUMENTS(DOC_ID)
        )
        """
        
        # Create intelligence insights table
        create_insights_table = """
        CREATE TABLE IF NOT EXISTS INTELLIGENCE_INSIGHTS (
            INSIGHT_ID VARCHAR(255) PRIMARY KEY,
            DOC_ID VARCHAR(255),
            INSIGHT_TYPE VARCHAR(100),
            INSIGHT_CATEGORY VARCHAR(100),
            TITLE VARCHAR(500),
            SUMMARY TEXT,
            KEY_POINTS VARIANT,
            CONFIDENCE_SCORE FLOAT,
            STRATEGIC_VALUE INTEGER,
            ACTIONABLE_ITEMS VARIANT,
            GENERATED_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
            MODEL_USED VARCHAR(100),
            FOREIGN KEY (DOC_ID) REFERENCES DOCUMENTS(DOC_ID)
        )
        """
        
        # Create search index table for Cortex Search
        create_search_index_table = """
        CREATE TABLE IF NOT EXISTS SEARCH_INDEX (
            INDEX_ID VARCHAR(255) PRIMARY KEY,
            DOC_ID VARCHAR(255),
            CONTENT_CHUNK TEXT,
            EMBEDDINGS VECTOR(FLOAT, 768),
            CHUNK_METADATA VARIANT,
            INDEXED_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
            FOREIGN KEY (DOC_ID) REFERENCES DOCUMENTS(DOC_ID)
        )
        """
        
        try:
            self.session.sql(create_documents_table).collect()
            self.session.sql(create_content_table).collect()
            self.session.sql(create_insights_table).collect()
            self.session.sql(create_search_index_table).collect()
            
            self.logger.info("Successfully created all required tables")
            
        except Exception as e:
            self.logger.error(f"Error creating tables: {e}")
            raise
    
    def insert_document_metadata(self, document: Dict[str, Any]) -> str:
        """
        Insert document metadata into the DOCUMENTS table.
        
        Args:
            document: Document metadata dictionary
            
        Returns:
            Document ID
        """
        if not self.session:
            self.connect()
        
        doc_id = f"{document['id']}_{int(datetime.now().timestamp())}"
        
        insert_query = """
        INSERT INTO DOCUMENTS (
            DOC_ID, FILE_NAME, FILE_TYPE, SOURCE_FOLDER, STRATEGIC_CATEGORY,
            EXTRACTION_PRIORITY, FILE_SIZE_BYTES, CREATED_TIME, MODIFIED_TIME,
            DOWNLOAD_PATH, WEB_VIEW_LINK, METADATA
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        try:
            # Parse timestamps
            created_time = None
            modified_time = None
            
            if document.get('createdTime'):
                created_time = datetime.fromisoformat(document['createdTime'].replace('Z', '+00:00'))
            if document.get('modifiedTime'):
                modified_time = datetime.fromisoformat(document['modifiedTime'].replace('Z', '+00:00'))
            
            # Prepare metadata as JSON
            metadata = {
                'original_id': document.get('id'),
                'mime_type': document.get('mimeType'),
                'web_view_link': document.get('webViewLink'),
                'size': document.get('size'),
                'extraction_priority': document.get('extraction_priority')
            }
            
            self.session.sql(insert_query).bind([
                doc_id,
                document.get('name'),
                document.get('mimeType'),
                document.get('source_folder', 'unknown'),
                document.get('strategic_category', 'general_business'),
                document.get('extraction_priority', 3),
                int(document.get('size', 0)) if document.get('size') else None,
                created_time,
                modified_time,
                document.get('download_path'),
                document.get('webViewLink'),
                json.dumps(metadata)
            ]).collect()
            
            self.logger.info(f"Inserted document metadata: {doc_id}")
            return doc_id
            
        except Exception as e:
            self.logger.error(f"Error inserting document metadata: {e}")
            raise
    
    def insert_document_content(self, doc_id: str, content: str, content_type: str = 'text', 
                               page_number: int = 1, chunk_number: int = 1) -> str:
        """
        Insert document content into the DOCUMENT_CONTENT table.
        
        Args:
            doc_id: Document ID
            content: Raw content text
            content_type: Type of content
            page_number: Page number (for multi-page documents)
            chunk_number: Chunk number (for chunked content)
            
        Returns:
            Content ID
        """
        if not self.session:
            self.connect()
        
        content_id = f"{doc_id}_content_{page_number}_{chunk_number}"
        
        insert_query = """
        INSERT INTO DOCUMENT_CONTENT (
            CONTENT_ID, DOC_ID, RAW_CONTENT, CONTENT_TYPE, 
            PAGE_NUMBER, CHUNK_NUMBER, CHUNK_SIZE
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        
        try:
            self.session.sql(insert_query).bind([
                content_id,
                doc_id,
                content,
                content_type,
                page_number,
                chunk_number,
                len(content)
            ]).collect()
            
            self.logger.info(f"Inserted document content: {content_id}")
            return content_id
            
        except Exception as e:
            self.logger.error(f"Error inserting document content: {e}")
            raise
    
    def generate_intelligence_insights(self, doc_id: str, content: str, model: str = 'mistral-7b') -> Dict[str, Any]:
        """
        Use Snowflake Cortex AI to generate strategic intelligence insights.
        
        Args:
            doc_id: Document ID
            content: Document content
            model: Cortex AI model to use
            
        Returns:
            Generated insights dictionary
        """
        if not self.session:
            self.connect()
        
        # Strategic intelligence prompt
        intelligence_prompt = f"""
        Analyze the following business document and provide strategic intelligence insights:

        Document Content:
        {content[:4000]}  # Limit content to avoid token limits

        Please provide:
        1. Executive Summary (2-3 sentences)
        2. Key Strategic Points (3-5 bullet points)
        3. Actionable Insights (3-5 recommendations)
        4. Risk Factors (if any)
        5. Opportunities Identified
        6. Strategic Value Rating (1-10)

        Format the response as structured analysis suitable for executive decision-making.
        """
        
        try:
            # Use Snowflake Cortex COMPLETE function
            cortex_query = f"""
            SELECT SNOWFLAKE.CORTEX.COMPLETE(
                '{model}',
                '{intelligence_prompt.replace("'", "''")}' -- Escape single quotes
            ) as insights
            """
            
            result = self.session.sql(cortex_query).collect()
            insights_text = result[0]['INSIGHTS'] if result else ""
            
            # Structure the insights
            insights = {
                'raw_analysis': insights_text,
                'generated_time': datetime.now(),
                'model_used': model,
                'doc_id': doc_id
            }
            
            # Parse and categorize insights (simplified parsing)
            insights['summary'] = self._extract_section(insights_text, 'Executive Summary')
            insights['key_points'] = self._extract_section(insights_text, 'Key Strategic Points')
            insights['actionable_items'] = self._extract_section(insights_text, 'Actionable Insights')
            insights['confidence_score'] = 0.85  # Default confidence
            insights['strategic_value'] = self._extract_strategic_value(insights_text)
            
            return insights
            
        except Exception as e:
            self.logger.error(f"Error generating intelligence insights: {e}")
            return {}
    
    def insert_intelligence_insights(self, insights: Dict[str, Any]) -> str:
        """Insert generated intelligence insights into the database."""
        if not self.session:
            self.connect()
        
        insight_id = f"{insights['doc_id']}_insights_{int(datetime.now().timestamp())}"
        
        insert_query = """
        INSERT INTO INTELLIGENCE_INSIGHTS (
            INSIGHT_ID, DOC_ID, INSIGHT_TYPE, INSIGHT_CATEGORY, TITLE,
            SUMMARY, KEY_POINTS, CONFIDENCE_SCORE, STRATEGIC_VALUE,
            ACTIONABLE_ITEMS, MODEL_USED
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        try:
            self.session.sql(insert_query).bind([
                insight_id,
                insights['doc_id'],
                'strategic_analysis',
                'cortex_generated',
                'Strategic Intelligence Analysis',
                insights.get('summary', ''),
                json.dumps(insights.get('key_points', [])),
                insights.get('confidence_score', 0.0),
                insights.get('strategic_value', 5),
                json.dumps(insights.get('actionable_items', [])),
                insights.get('model_used', 'unknown')
            ]).collect()
            
            self.logger.info(f"Inserted intelligence insights: {insight_id}")
            return insight_id
            
        except Exception as e:
            self.logger.error(f"Error inserting intelligence insights: {e}")
            raise
    
    def create_cortex_search_service(self, service_name: str = 'BUSINESS_INTELLIGENCE_SEARCH') -> None:
        """Create a Cortex Search service for intelligent document querying."""
        if not self.session:
            self.connect()
        
        try:
            # Create search service
            create_service_query = f"""
            CREATE OR REPLACE CORTEX SEARCH SERVICE {service_name}
            ON RAW_CONTENT
            ATTRIBUTES STRATEGIC_CATEGORY, FILE_TYPE, INSIGHT_CATEGORY
            WAREHOUSE = {self.connection_params.get('warehouse', 'COMPUTE_WH')}
            TARGET_LAG = '1 hour'
            AS (
                SELECT 
                    dc.RAW_CONTENT,
                    d.STRATEGIC_CATEGORY,
                    d.FILE_TYPE,
                    ii.INSIGHT_CATEGORY,
                    dc.DOC_ID
                FROM DOCUMENT_CONTENT dc
                JOIN DOCUMENTS d ON dc.DOC_ID = d.DOC_ID
                LEFT JOIN INTELLIGENCE_INSIGHTS ii ON dc.DOC_ID = ii.DOC_ID
                WHERE dc.PROCESSING_STATUS = 'COMPLETED'
            )
            """
            
            self.session.sql(create_service_query).collect()
            self.logger.info(f"Created Cortex Search service: {service_name}")
            
        except Exception as e:
            self.logger.error(f"Error creating Cortex Search service: {e}")
            # Don't raise as this might be due to service already existing
    
    def search_business_intelligence(self, query: str, service_name: str = 'BUSINESS_INTELLIGENCE_SEARCH', 
                                   limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search business documents using Cortex Search for strategic intelligence.
        
        Args:
            query: Search query
            service_name: Name of the Cortex Search service
            limit: Maximum number of results
            
        Returns:
            List of search results with relevance scores
        """
        if not self.session:
            self.connect()
        
        try:
            search_query = f"""
            SELECT 
                PARSE_JSON(results) as search_results
            FROM TABLE(
                CORTEX_SEARCH(
                    '{service_name}',
                    '{query.replace("'", "''")}',  -- Escape single quotes
                    {{ 'limit': {limit} }}
                )
            )
            """
            
            results = self.session.sql(search_query).collect()
            
            if results:
                search_results = []
                for row in results:
                    result_data = row['SEARCH_RESULTS']
                    if isinstance(result_data, str):
                        result_data = json.loads(result_data)
                    search_results.append(result_data)
                
                self.logger.info(f"Found {len(search_results)} search results for query: {query}")
                return search_results
            
            return []
            
        except Exception as e:
            self.logger.error(f"Error searching business intelligence: {e}")
            return []
    
    def get_strategic_dashboard_data(self) -> Dict[str, Any]:
        """Get aggregated data for strategic intelligence dashboard."""
        if not self.session:
            self.connect()
        
        try:
            # Document statistics
            doc_stats_query = """
            SELECT 
                COUNT(*) as total_documents,
                COUNT(DISTINCT STRATEGIC_CATEGORY) as categories,
                AVG(EXTRACTION_PRIORITY) as avg_priority,
                COUNT(CASE WHEN PROCESSED_TIME >= CURRENT_DATE - 7 then 1 END) as recent_processed
            FROM DOCUMENTS
            """
            
            # Category breakdown
            category_query = """
            SELECT 
                STRATEGIC_CATEGORY,
                COUNT(*) as doc_count,
                AVG(ii.STRATEGIC_VALUE) as avg_strategic_value
            FROM DOCUMENTS d
            LEFT JOIN INTELLIGENCE_INSIGHTS ii ON d.DOC_ID = ii.DOC_ID
            GROUP BY STRATEGIC_CATEGORY
            ORDER BY doc_count DESC
            """
            
            # Recent insights
            insights_query = """
            SELECT 
                INSIGHT_TYPE,
                COUNT(*) as insight_count,
                AVG(CONFIDENCE_SCORE) as avg_confidence,
                AVG(STRATEGIC_VALUE) as avg_value
            FROM INTELLIGENCE_INSIGHTS
            WHERE GENERATED_TIME >= CURRENT_DATE - 30
            GROUP BY INSIGHT_TYPE
            """
            
            doc_stats = self.session.sql(doc_stats_query).collect()
            categories = self.session.sql(category_query).collect()
            insights = self.session.sql(insights_query).collect()
            
            dashboard_data = {
                'document_statistics': doc_stats[0].as_dict() if doc_stats else {},
                'category_breakdown': [row.as_dict() for row in categories],
                'insight_statistics': [row.as_dict() for row in insights],
                'generated_time': datetime.now()
            }
            
            return dashboard_data
            
        except Exception as e:
            self.logger.error(f"Error getting dashboard data: {e}")
            return {}
    
    def _extract_section(self, text: str, section_name: str) -> str:
        """Extract a specific section from the generated insights text."""
        try:
            lines = text.split('\n')
            section_content = []
            in_section = False
            
            for line in lines:
                if section_name.lower() in line.lower():
                    in_section = True
                    continue
                elif in_section and line.strip() and any(header in line.lower() for header in ['summary', 'points', 'insights', 'factors', 'opportunities', 'rating']):
                    break
                elif in_section and line.strip():
                    section_content.append(line.strip())
            
            return '\n'.join(section_content)
        except:
            return ""
    
    def _extract_strategic_value(self, text: str) -> int:
        """Extract strategic value rating from the insights text."""
        try:
            import re
            rating_match = re.search(r'rating.*?(\d+)', text.lower())
            if rating_match:
                return int(rating_match.group(1))
            return 5  # Default rating
        except:
            return 5
    
    def close(self) -> None:
        """Close the Snowflake session."""
        if self.session:
            self.session.close()
            self.logger.info("Snowflake session closed")