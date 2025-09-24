# Google Drive to Snowflake Intelligence Pipeline Demo

Transform your Google Drive business documents into actionable strategic intelligence with Snowflake Intelligence and Cortex Search.

## 🎯 Overview

This demo showcases a complete end-to-end pipeline that:

1. **Extracts** business documents from Google Drive folders
2. **Processes** unstructured content from various file formats (PDF, DOCX, XLSX, PPTX, TXT)
3. **Analyzes** documents using Snowflake Cortex AI to generate strategic insights
4. **Enables** intelligent search and querying through Cortex Search
5. **Provides** executive dashboards and actionable intelligence reports

## 🏗️ Architecture

```
Google Drive Documents → Document Processor → Snowflake Cortex AI → Strategic Intelligence
         ↓                      ↓                    ↓                      ↓
   📁 Business Files    🔄 Content Extraction   🧠 AI Analysis      📊 Search & Insights
```

### Components

- **Google Drive Integration**: Secure API access to extract business documents
- **Document Processing**: Multi-format content extraction (PDF, Office files, text)
- **Snowflake Intelligence**: Cortex AI for strategic analysis and insight generation
- **Cortex Search**: Intelligent search capabilities over processed documents
- **Dashboard & Reporting**: Executive-level insights and metrics

## 🚀 Quick Start

### Prerequisites

1. **Snowflake Account** with Cortex AI enabled
2. **Google Cloud Project** with Drive API enabled
3. **Python 3.8+** environment

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Snowflake-Labs/openflow-unstructured-data-pipeline-demo.git
cd openflow-unstructured-data-pipeline-demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your credentials
```

4. Set up Google Drive API:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Enable Google Drive API
   - Create credentials (OAuth 2.0 Client ID)
   - Download credentials JSON file to `config/google_credentials.json`

5. Initialize Snowflake database:
```bash
# Run the SQL setup script in your Snowflake environment
cat sql/setup_database.sql
```

### Run the Pipeline

```bash
python examples/run_pipeline.py
```

### Search Intelligence

```bash
python examples/search_intelligence.py
```

## 📋 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Snowflake Configuration
SNOWFLAKE_ACCOUNT=your_account.region
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_DATABASE=UNSTRUCTURED_DEMO
SNOWFLAKE_SCHEMA=INTELLIGENCE
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_ROLE=ACCOUNTADMIN

# Google Drive API Configuration
GOOGLE_DRIVE_CREDENTIALS_FILE=config/google_credentials.json
GOOGLE_DRIVE_FOLDER_ID=your_google_drive_folder_id

# Cortex AI Configuration
CORTEX_MODEL=mistral-7b

# Pipeline Configuration
BATCH_SIZE=10
PROCESSING_THREADS=4
```

### Google Drive Setup

1. Create a Google Cloud Project
2. Enable Google Drive API
3. Create OAuth 2.0 credentials
4. Download credentials JSON
5. Get the folder ID from your Google Drive URL:
   ```
   https://drive.google.com/drive/folders/[FOLDER_ID_HERE]
   ```

## 🔧 Usage Examples

### Basic Pipeline Execution

```python
from src.pipeline.orchestrator import PipelineOrchestrator

# Initialize with configuration
config = {
    'SNOWFLAKE_ACCOUNT': 'your_account',
    'SNOWFLAKE_USER': 'your_user',
    # ... other config
}

orchestrator = PipelineOrchestrator(config)

# Initialize infrastructure
orchestrator.initialize_infrastructure()

# Run complete pipeline
results = orchestrator.run_full_pipeline('your_folder_id')

print(f"Processed {results['stages']['processing']['documents_processed']} documents")
print(f"Generated {results['stages']['intelligence']['insights_generated']} insights")
```

### Intelligent Search

```python
# Search for strategic content
results = orchestrator.search_intelligence("market expansion strategy")

for result in results:
    print(f"Document: {result['file_name']}")
    print(f"Content: {result['content'][:200]}...")
```

### Dashboard Analytics

```python
# Get strategic intelligence dashboard
dashboard = orchestrator.get_strategic_dashboard()

print(f"Total Documents: {dashboard['document_statistics']['total_documents']}")
print(f"Categories: {len(dashboard['category_breakdown'])}")
```

## 📊 Strategic Intelligence Features

### Document Categorization

The pipeline automatically categorizes documents into strategic areas:

- **Strategic Planning**: Vision, roadmaps, strategic initiatives
- **Financial Analysis**: Budget, revenue, profit analysis
- **Market Intelligence**: Competitive analysis, customer insights
- **Operational Insights**: Process improvements, efficiency metrics
- **Risk Management**: Compliance, governance, risk assessment
- **Human Resources**: Performance, organizational development

### AI-Generated Insights

Each document is analyzed by Snowflake Cortex AI to generate:

- **Executive Summary**: Key takeaways for leadership
- **Strategic Points**: Important business implications
- **Actionable Items**: Recommended next steps
- **Risk Factors**: Potential challenges identified
- **Opportunities**: Growth and improvement areas
- **Strategic Value Rating**: 1-10 priority score

### Search Capabilities

Cortex Search enables intelligent querying:

```sql
-- Example search queries
SELECT * FROM CORTEX_SEARCH('business_intelligence_search', 'revenue growth opportunities');
SELECT * FROM CORTEX_SEARCH('business_intelligence_search', 'operational efficiency');
SELECT * FROM CORTEX_SEARCH('business_intelligence_search', 'market competition analysis');
```

## 🗂️ Database Schema

### Core Tables

- **DOCUMENTS**: Document metadata and categorization
- **DOCUMENT_CONTENT**: Extracted text content with chunking
- **INTELLIGENCE_INSIGHTS**: AI-generated strategic insights
- **SEARCH_INDEX**: Cortex Search indexes and embeddings

### Key Views

- **V_STRATEGIC_OVERVIEW**: Category-level strategic metrics
- **V_RECENT_INSIGHTS**: Latest AI-generated insights
- **V_PROCESSING_STATUS**: Document processing pipeline status

## 🔍 Example Use Cases

### 1. Executive Strategy Review
```
Query: "strategic objectives for Q4"
→ Finds: Strategic planning documents, quarterly goals, initiative roadmaps
→ Insights: Priority initiatives, resource requirements, success metrics
```

### 2. Financial Performance Analysis
```
Query: "revenue growth and profitability"
→ Finds: Financial reports, budget analyses, performance metrics
→ Insights: Growth drivers, margin opportunities, cost optimization areas
```

### 3. Market Intelligence
```
Query: "competitive landscape and market share"
→ Finds: Market research, competitor analysis, customer surveys
→ Insights: Competitive advantages, market opportunities, customer preferences
```

### 4. Operational Excellence
```
Query: "process improvement and efficiency"
→ Finds: Operational reports, workflow documentation, efficiency studies
→ Insights: Bottlenecks, automation opportunities, best practices
```

## 📈 Pipeline Metrics

The system tracks comprehensive metrics:

- **Processing Performance**: Documents/second, success rates
- **Content Quality**: Word counts, extraction accuracy
- **Intelligence Value**: Confidence scores, strategic ratings
- **Search Effectiveness**: Query success rates, result relevance

## 🛠️ Development

### Project Structure

```
├── src/
│   ├── google_drive/       # Google Drive API integration
│   ├── snowflake/         # Snowflake and Cortex AI client
│   ├── pipeline/          # Document processing and orchestration
│   └── cortex/           # Cortex-specific utilities
├── sql/                  # Database setup scripts
├── examples/            # Example usage scripts
├── docs/               # Additional documentation
├── scripts/            # Utility scripts
└── config/            # Configuration files
```

### Adding New Document Types

1. Extend `DocumentProcessor.extract_content()` method
2. Add MIME type handling in `GoogleDriveClient`
3. Update content chunking logic if needed

### Custom Intelligence Models

1. Modify `SnowflakeClient.generate_intelligence_insights()`
2. Update prompts for domain-specific analysis
3. Adjust strategic categorization logic

## 🔒 Security & Compliance

- **Authentication**: OAuth 2.0 for Google Drive, secure Snowflake connection
- **Data Privacy**: Documents processed in secure Snowflake environment
- **Access Control**: Role-based permissions for Snowflake resources
- **Audit Trail**: Complete processing logs and lineage tracking

## 🚨 Troubleshooting

### Common Issues

1. **Google Drive Authentication**: Ensure OAuth credentials are correctly configured
2. **Snowflake Connection**: Verify account URL, credentials, and warehouse access
3. **Cortex AI Access**: Confirm Cortex AI is enabled in your Snowflake account
4. **Document Processing**: Check supported file formats and file accessibility

### Logs and Monitoring

- Pipeline execution logs: `pipeline_run_*.log`
- Application logs: Configure logging level in scripts
- Snowflake query logs: Available in Snowflake console

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions and support:

- **Issues**: GitHub Issues
- **Documentation**: See `docs/` directory
- **Snowflake Support**: Contact your Snowflake representative

---

**Transform your business documents into strategic intelligence with the power of Snowflake Cortex AI! 🚀**
