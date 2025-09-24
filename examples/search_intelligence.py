#!/usr/bin/env python3
"""
Example script demonstrating intelligent search capabilities using Cortex Search.
This shows how to query the processed business documents for strategic insights.
"""

import os
import sys
import logging
from dotenv import load_dotenv

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pipeline.orchestrator import PipelineOrchestrator

def setup_logging():
    """Configure logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def load_configuration():
    """Load configuration from environment variables."""
    load_dotenv()
    
    config = {
        'SNOWFLAKE_ACCOUNT': os.getenv('SNOWFLAKE_ACCOUNT'),
        'SNOWFLAKE_USER': os.getenv('SNOWFLAKE_USER'),
        'SNOWFLAKE_PASSWORD': os.getenv('SNOWFLAKE_PASSWORD'),
        'SNOWFLAKE_DATABASE': os.getenv('SNOWFLAKE_DATABASE', 'UNSTRUCTURED_DEMO'),
        'SNOWFLAKE_SCHEMA': os.getenv('SNOWFLAKE_SCHEMA', 'INTELLIGENCE'),
        'SNOWFLAKE_WAREHOUSE': os.getenv('SNOWFLAKE_WAREHOUSE', 'COMPUTE_WH'),
        'SNOWFLAKE_ROLE': os.getenv('SNOWFLAKE_ROLE', 'ACCOUNTADMIN'),
    }
    
    return config

def interactive_search_demo(orchestrator):
    """Run an interactive search demonstration."""
    print("\n" + "="*60)
    print("INTERACTIVE STRATEGIC INTELLIGENCE SEARCH")
    print("="*60)
    print("Enter search queries to find relevant business insights.")
    print("Type 'quit' to exit, 'help' for example queries.")
    print()
    
    example_queries = [
        "strategic planning initiatives",
        "revenue growth opportunities", 
        "operational efficiency improvements",
        "market expansion strategies",
        "financial performance metrics",
        "risk management approaches",
        "customer satisfaction trends",
        "competitive advantage factors"
    ]
    
    while True:
        try:
            query = input("Search Query: ").strip()
            
            if not query:
                continue
            elif query.lower() == 'quit':
                break
            elif query.lower() == 'help':
                print("\nExample queries you can try:")
                for i, example in enumerate(example_queries, 1):
                    print(f"  {i}. {example}")
                print()
                continue
            
            print(f"\nSearching for: '{query}'...")
            results = orchestrator.search_intelligence(query, limit=5)
            
            if results:
                print(f"Found {len(results)} results:\n")
                
                for i, result in enumerate(results, 1):
                    print(f"Result {i}:")
                    print(f"  Document: {result.get('file_name', 'Unknown')}")
                    print(f"  Category: {result.get('strategic_category', 'General')}")
                    print(f"  Content Preview: {result.get('content', '')[:200]}...")
                    print(f"  Relevance Score: {result.get('relevance_score', 'N/A')}")
                    print()
            else:
                print("No results found. Try a different query or check if documents are processed.\n")
                
        except KeyboardInterrupt:
            print("\nSearch demo interrupted.")
            break
        except Exception as e:
            print(f"Search error: {e}\n")

def predefined_search_demo(orchestrator):
    """Run predefined search queries to demonstrate capabilities."""
    print("\n" + "="*60)
    print("PREDEFINED SEARCH DEMONSTRATIONS")
    print("="*60)
    
    search_scenarios = [
        {
            "title": "Strategic Planning Intelligence",
            "query": "strategic objectives roadmap vision",
            "description": "Finding strategic planning documents and initiatives"
        },
        {
            "title": "Financial Performance Analysis", 
            "query": "revenue profit margin financial performance",
            "description": "Searching for financial metrics and performance data"
        },
        {
            "title": "Market Intelligence",
            "query": "market share competition customer analysis",
            "description": "Identifying market analysis and competitive intelligence"
        },
        {
            "title": "Operational Excellence",
            "query": "efficiency process improvement operational",
            "description": "Finding operational improvement opportunities"
        },
        {
            "title": "Risk Management",
            "query": "risk mitigation compliance governance",
            "description": "Discovering risk management strategies and compliance"
        }
    ]
    
    for scenario in search_scenarios:
        print(f"\n📊 {scenario['title']}")
        print(f"Description: {scenario['description']}")
        print(f"Query: '{scenario['query']}'")
        print("-" * 50)
        
        try:
            results = orchestrator.search_intelligence(scenario['query'], limit=3)
            
            if results:
                print(f"✓ Found {len(results)} relevant documents:")
                
                for i, result in enumerate(results, 1):
                    doc_name = result.get('file_name', 'Unknown Document')
                    category = result.get('strategic_category', 'General')
                    content_preview = result.get('content', '')[:150]
                    
                    print(f"  {i}. {doc_name} ({category})")
                    print(f"     Preview: {content_preview}...")
                    
            else:
                print("✗ No matching documents found")
                
        except Exception as e:
            print(f"✗ Search failed: {e}")
        
        print()

def generate_intelligence_report(orchestrator):
    """Generate a comprehensive intelligence report."""
    print("\n" + "="*60)
    print("STRATEGIC INTELLIGENCE REPORT")
    print("="*60)
    
    try:
        dashboard = orchestrator.get_strategic_dashboard()
        
        if not dashboard:
            print("No dashboard data available. Ensure documents have been processed.")
            return
        
        # Document statistics
        doc_stats = dashboard.get('document_statistics', {})
        print(f"📄 DOCUMENT OVERVIEW")
        print(f"   Total Documents Processed: {doc_stats.get('TOTAL_DOCUMENTS', 0)}")
        print(f"   Strategic Categories: {doc_stats.get('CATEGORIES', 0)}")
        print(f"   Recently Processed: {doc_stats.get('RECENT_PROCESSED', 0)}")
        print(f"   Average Priority Score: {doc_stats.get('AVG_PRIORITY', 0):.1f}")
        
        # Category breakdown
        categories = dashboard.get('category_breakdown', [])
        if categories:
            print(f"\n📊 STRATEGIC CATEGORY ANALYSIS")
            for cat in categories[:5]:
                category_name = cat.get('STRATEGIC_CATEGORY', 'Unknown')
                doc_count = cat.get('DOC_COUNT', 0)
                avg_value = cat.get('AVG_STRATEGIC_VALUE', 0) or 0
                
                print(f"   {category_name.replace('_', ' ').title()}: {doc_count} docs (Avg Value: {avg_value:.1f})")
        
        # Top insights
        top_insights = dashboard.get('top_insights', [])
        if top_insights:
            print(f"\n🎯 TOP STRATEGIC INSIGHTS")
            for i, insight in enumerate(top_insights[:5], 1):
                title = insight.get('TITLE', 'Untitled')
                summary = insight.get('SUMMARY', '')[:100]
                value = insight.get('STRATEGIC_VALUE', 0)
                confidence = insight.get('CONFIDENCE_SCORE', 0)
                
                print(f"   {i}. {title}")
                print(f"      Value: {value}/10, Confidence: {confidence:.1%}")
                print(f"      Summary: {summary}...")
                print()
        
        # Recent activity
        recent_activity = dashboard.get('recent_activity', [])
        if recent_activity:
            print(f"⏰ RECENT PROCESSING ACTIVITY")
            for activity in recent_activity[:5]:
                file_name = activity.get('FILE_NAME', 'Unknown')
                category = activity.get('STRATEGIC_CATEGORY', 'General')
                processed_time = activity.get('PROCESSED_TIME', '')
                
                print(f"   {file_name} ({category}) - {processed_time}")
        
        print(f"\n" + "="*60)
        print("Report generated successfully!")
        print("This intelligence can be used for executive decision-making and strategic planning.")
        
    except Exception as e:
        print(f"Error generating intelligence report: {e}")

def main():
    """Main execution function."""
    print("=== Snowflake Cortex Search Intelligence Demo ===")
    print("Demonstrating intelligent search capabilities over business documents")
    
    setup_logging()
    
    try:
        # Load configuration
        config = load_configuration()
        
        if not all([config['SNOWFLAKE_ACCOUNT'], config['SNOWFLAKE_USER'], config['SNOWFLAKE_PASSWORD']]):
            print("Missing required Snowflake credentials. Please check your .env file.")
            sys.exit(1)
        
        # Initialize orchestrator
        orchestrator = PipelineOrchestrator(config)
        
        print("Connecting to Snowflake...")
        orchestrator.snowflake_client.connect()
        print("✓ Connected successfully")
        
        # Show menu
        while True:
            print("\n" + "="*40)
            print("INTELLIGENCE SEARCH MENU")
            print("="*40)
            print("1. Interactive Search")
            print("2. Predefined Search Demo")
            print("3. Generate Intelligence Report") 
            print("4. Exit")
            
            choice = input("\nSelect option (1-4): ").strip()
            
            if choice == '1':
                interactive_search_demo(orchestrator)
            elif choice == '2':
                predefined_search_demo(orchestrator)
            elif choice == '3':
                generate_intelligence_report(orchestrator)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-4.")
    
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
    except Exception as e:
        print(f"Demo failed: {e}")
    finally:
        try:
            orchestrator.cleanup()
        except:
            pass

if __name__ == "__main__":
    main()