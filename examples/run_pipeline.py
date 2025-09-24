#!/usr/bin/env python3
"""
Example script to run the complete unstructured data pipeline.
This demonstrates how to extract business documents from Google Drive,
process them, and generate strategic intelligence using Snowflake Cortex AI.
"""

import os
import sys
import logging
from datetime import datetime
from dotenv import load_dotenv

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pipeline.orchestrator import PipelineOrchestrator

def setup_logging():
    """Configure logging for the pipeline execution."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'pipeline_run_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def load_configuration():
    """Load configuration from environment variables."""
    # Load environment variables from .env file
    load_dotenv()
    
    required_vars = [
        'SNOWFLAKE_ACCOUNT',
        'SNOWFLAKE_USER', 
        'SNOWFLAKE_PASSWORD',
        'GOOGLE_DRIVE_CREDENTIALS_FILE',
        'GOOGLE_DRIVE_FOLDER_ID'
    ]
    
    config = {}
    missing_vars = []
    
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
        else:
            config[var] = value
    
    if missing_vars:
        print(f"Missing required environment variables: {', '.join(missing_vars)}")
        print("Please check your .env file or environment configuration.")
        sys.exit(1)
    
    # Optional configuration with defaults
    optional_vars = {
        'SNOWFLAKE_DATABASE': 'UNSTRUCTURED_DEMO',
        'SNOWFLAKE_SCHEMA': 'INTELLIGENCE', 
        'SNOWFLAKE_WAREHOUSE': 'COMPUTE_WH',
        'SNOWFLAKE_ROLE': 'ACCOUNTADMIN',
        'CORTEX_MODEL': 'mistral-7b',
        'BATCH_SIZE': '10',
        'PROCESSING_THREADS': '4'
    }
    
    for var, default in optional_vars.items():
        config[var] = os.getenv(var, default)
    
    return config

def main():
    """Main execution function."""
    print("=== Snowflake Unstructured Data Pipeline Demo ===")
    print("Transforming Google Drive documents into actionable strategic intelligence")
    print()
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Load configuration
        config = load_configuration()
        logger.info("Configuration loaded successfully")
        
        # Initialize pipeline orchestrator
        orchestrator = PipelineOrchestrator(config)
        
        # Initialize infrastructure
        print("Initializing Snowflake infrastructure...")
        if not orchestrator.initialize_infrastructure():
            print("Failed to initialize infrastructure. Check your Snowflake connection.")
            sys.exit(1)
        
        print("✓ Infrastructure initialized successfully")
        
        # Get Google Drive folder ID
        folder_id = config['GOOGLE_DRIVE_FOLDER_ID']
        print(f"Processing documents from Google Drive folder: {folder_id}")
        
        # Run the complete pipeline
        print("\nStarting pipeline execution...")
        print("This may take several minutes depending on the number of documents...")
        
        results = orchestrator.run_full_pipeline(folder_id)
        
        # Display results
        print("\n" + "="*60)
        print("PIPELINE EXECUTION RESULTS")
        print("="*60)
        
        print(f"Pipeline ID: {results['pipeline_id']}")
        print(f"Status: {results['status']}")
        print(f"Total Duration: {results.get('total_duration_seconds', 0):.2f} seconds")
        
        if results['status'] == 'failed':
            print(f"Error: {results.get('error', 'Unknown error')}")
            sys.exit(1)
        
        # Stage results
        print("\nStage Results:")
        for stage, data in results.get('stages', {}).items():
            print(f"  {stage.title()}:")
            print(f"    Status: {data.get('status', 'unknown')}")
            print(f"    Duration: {data.get('duration_seconds', 0):.2f}s")
            
            if stage == 'discovery':
                print(f"    Documents Found: {data.get('documents_found', 0)}")
                print(f"    Categories: {', '.join(data.get('categories', []))}")
            elif stage == 'processing':
                print(f"    Documents Processed: {data.get('documents_processed', 0)}")
                print(f"    Successful: {data.get('successful_extractions', 0)}")
                print(f"    Failed: {data.get('failed_extractions', 0)}")
            elif stage == 'intelligence':
                print(f"    Insights Generated: {data.get('insights_generated', 0)}")
                print(f"    Avg Confidence: {data.get('avg_confidence', 0):.2f}")
                print(f"    Avg Strategic Value: {data.get('avg_strategic_value', 0):.1f}")
            elif stage == 'search':
                print(f"    Documents Indexed: {data.get('documents_indexed', 0)}")
        
        # Metrics
        metrics = results.get('metrics', {})
        print(f"\nPerformance Metrics:")
        print(f"  Documents/Second: {metrics.get('documents_per_second', 0):.2f}")
        print(f"  Success Rate: {metrics.get('success_rate', 0):.1%}")
        
        # Demonstrate search functionality
        print("\n" + "="*60)
        print("DEMONSTRATING SEARCH FUNCTIONALITY")
        print("="*60)
        
        search_queries = [
            "strategic planning",
            "financial performance", 
            "market analysis",
            "risk management",
            "operational efficiency"
        ]
        
        for query in search_queries:
            print(f"\nSearching for: '{query}'")
            search_results = orchestrator.search_intelligence(query, limit=3)
            
            if search_results:
                print(f"  Found {len(search_results)} results:")
                for i, result in enumerate(search_results[:2], 1):
                    print(f"    {i}. {result.get('title', 'Untitled')}")
            else:
                print("  No results found")
        
        # Show dashboard data
        print("\n" + "="*60)
        print("STRATEGIC INTELLIGENCE DASHBOARD")
        print("="*60)
        
        dashboard = orchestrator.get_strategic_dashboard()
        
        if dashboard:
            doc_stats = dashboard.get('document_statistics', {})
            print(f"Total Documents: {doc_stats.get('TOTAL_DOCUMENTS', 0)}")
            print(f"Document Categories: {doc_stats.get('CATEGORIES', 0)}")
            print(f"Recently Processed: {doc_stats.get('RECENT_PROCESSED', 0)}")
            
            categories = dashboard.get('category_breakdown', [])
            if categories:
                print(f"\nTop Document Categories:")
                for cat in categories[:5]:
                    print(f"  {cat.get('STRATEGIC_CATEGORY', 'Unknown')}: {cat.get('DOC_COUNT', 0)} docs")
            
            top_insights = dashboard.get('top_insights', [])
            if top_insights:
                print(f"\nTop Strategic Insights:")
                for insight in top_insights[:3]:
                    print(f"  • {insight.get('TITLE', 'Untitled')} (Value: {insight.get('STRATEGIC_VALUE', 0)})")
        
        print("\n" + "="*60)
        print("PIPELINE COMPLETED SUCCESSFULLY!")
        print("="*60)
        print(f"Your business documents have been transformed into actionable strategic intelligence.")
        print(f"You can now use Snowflake's Cortex Search to query your business knowledge base.")
        print(f"Access your results in Snowflake database: {config['SNOWFLAKE_DATABASE']}")
        
    except KeyboardInterrupt:
        print("\nPipeline execution interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}", exc_info=True)
        print(f"\nPipeline execution failed: {e}")
        sys.exit(1)
    finally:
        # Cleanup
        try:
            orchestrator.cleanup()
        except:
            pass

if __name__ == "__main__":
    main()