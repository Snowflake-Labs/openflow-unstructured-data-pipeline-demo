# Complete Setup Guide for Google Drive to Snowflake Intelligence Pipeline

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] Snowflake account with Cortex AI enabled
- [ ] Google Cloud project with billing enabled
- [ ] Python 3.8+ installed
- [ ] Git installed
- [ ] Administrative access to configure APIs

## 🔧 Step-by-Step Setup

### 1. Repository Setup

```bash
# Clone the repository
git clone https://github.com/Snowflake-Labs/openflow-unstructured-data-pipeline-demo.git
cd openflow-unstructured-data-pipeline-demo

# Run automated setup
./scripts/setup.sh
```

### 2. Google Drive API Setup

#### 2.1 Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "New Project" and create a project named "Snowflake-Intelligence-Demo"
3. Enable billing for the project

#### 2.2 Enable Google Drive API

1. In Google Cloud Console, go to "APIs & Services" > "Library"
2. Search for "Google Drive API"
3. Click "Enable"

#### 2.3 Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth 2.0 Client ID"
3. If prompted, configure OAuth consent screen first:
   - User Type: External (for testing) or Internal (for organization)
   - App name: "Snowflake Intelligence Pipeline"
   - User support email: Your email
   - Scopes: Add `../auth/drive.readonly`
4. For OAuth 2.0 Client ID:
   - Application type: Desktop application
   - Name: "Snowflake Pipeline Client"
5. Download the JSON file and save it as `config/google_credentials.json`

#### 2.4 Get Google Drive Folder ID

1. Create a folder in Google Drive with business documents
2. Open the folder in your browser
3. Copy the folder ID from the URL:
   ```
   https://drive.google.com/drive/folders/[THIS_IS_YOUR_FOLDER_ID]
   ```

### 3. Snowflake Setup

#### 3.1 Verify Cortex AI Access

```sql
-- Test Cortex AI availability
SELECT SNOWFLAKE.CORTEX.COMPLETE('mistral-7b', 'Hello, how are you?');
```

If this fails, contact your Snowflake administrator to enable Cortex AI.

#### 3.2 Create Database and Schema

```sql
-- Run the complete setup script
-- Copy and paste the contents of sql/setup_database.sql
-- Or run it directly in your Snowflake environment
```

#### 3.3 Create Compute Resources

```sql
-- Create a warehouse for processing (if not exists)
CREATE WAREHOUSE IF NOT EXISTS INTELLIGENCE_WH
WITH 
    WAREHOUSE_SIZE = 'MEDIUM'
    AUTO_SUSPEND = 300
    AUTO_RESUME = TRUE;

-- Grant access to your role
GRANT USAGE ON WAREHOUSE INTELLIGENCE_WH TO ROLE YOUR_ROLE;
```

### 4. Configuration

#### 4.1 Environment Variables

Edit the `.env` file with your specific values:

```env
# Snowflake Configuration
SNOWFLAKE_ACCOUNT=your_account.your_region.snowflakecomputing.com
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_DATABASE=UNSTRUCTURED_DEMO
SNOWFLAKE_SCHEMA=INTELLIGENCE
SNOWFLAKE_WAREHOUSE=INTELLIGENCE_WH
SNOWFLAKE_ROLE=YOUR_ROLE

# Google Drive API Configuration
GOOGLE_DRIVE_CREDENTIALS_FILE=config/google_credentials.json
GOOGLE_DRIVE_FOLDER_ID=your_folder_id_from_step_2.4

# Cortex AI Configuration
CORTEX_MODEL=mistral-7b

# Pipeline Configuration
BATCH_SIZE=10
PROCESSING_THREADS=4
```

#### 4.2 Test Configuration

```bash
# Activate virtual environment
source venv/bin/activate

# Test Snowflake connection
python -c "
from src.snowflake.client import SnowflakeClient
import os
from dotenv import load_dotenv

load_dotenv()
config = {
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'role': os.getenv('SNOWFLAKE_ROLE')
}

client = SnowflakeClient(config)
client.connect()
print('✅ Snowflake connection successful!')
"
```

### 5. Sample Data Preparation

#### 5.1 Create Test Documents

Create these sample documents in your Google Drive folder:

**Strategic_Plan_Q4_2024.docx:**
```
EXECUTIVE SUMMARY
Our Q4 2024 strategic initiatives focus on three key areas: market expansion, operational efficiency, and digital transformation. We aim to increase market share by 15%, reduce operational costs by 10%, and launch our new customer engagement platform.

STRATEGIC OBJECTIVES
1. Market Expansion: Target new geographic regions
2. Operational Excellence: Streamline core processes
3. Digital Innovation: Implement AI-driven solutions
4. Customer Experience: Enhance satisfaction metrics

FINANCIAL TARGETS
- Revenue growth: 20% YoY
- Margin improvement: 2 percentage points
- Cost reduction: $2M annually

RISK MITIGATION
Key risks include market competition, regulatory changes, and technology implementation challenges. We have developed comprehensive mitigation strategies for each area.
```

**Financial_Performance_Report.xlsx:**
- Create a spreadsheet with revenue, costs, and profit data
- Include quarterly trends and forecasts
- Add market performance comparisons

### 6. First Pipeline Run

#### 6.1 Initialize Infrastructure

```bash
python -c "
from src.pipeline.orchestrator import PipelineOrchestrator
import os
from dotenv import load_dotenv

load_dotenv()
config = dict(os.environ)

orchestrator = PipelineOrchestrator(config)
orchestrator.initialize_infrastructure()
print('✅ Infrastructure initialized!')
"
```

#### 6.2 Run Complete Pipeline

```bash
python examples/run_pipeline.py
```

Expected output:
```
=== Snowflake Unstructured Data Pipeline Demo ===
Transforming Google Drive documents into actionable strategic intelligence

✓ Infrastructure initialized successfully
Processing documents from Google Drive folder: your_folder_id

Starting pipeline execution...
Stage 1: Discovering business documents from Google Drive...
Stage 2: Processing X documents...
Stage 3: Generating strategic intelligence insights...
Stage 4: Creating search indexes...

PIPELINE EXECUTION RESULTS
Pipeline ID: pipeline_1234567890
Status: completed
Total Duration: XX.XX seconds
...
```

#### 6.3 Test Search Functionality

```bash
python examples/search_intelligence.py
```

## 🔍 Verification Steps

### 1. Database Verification

```sql
-- Check documents were processed
SELECT COUNT(*) as document_count FROM DOCUMENTS;

-- Check content extraction
SELECT COUNT(*) as content_chunks FROM DOCUMENT_CONTENT;

-- Check AI insights generation
SELECT COUNT(*) as insights_count FROM INTELLIGENCE_INSIGHTS;

-- View sample insights
SELECT TITLE, SUMMARY, STRATEGIC_VALUE 
FROM INTELLIGENCE_INSIGHTS 
ORDER BY STRATEGIC_VALUE DESC 
LIMIT 3;
```

### 2. Search Verification

```sql
-- Test Cortex Search (if available)
SELECT * FROM TABLE(
    CORTEX_SEARCH(
        'BUSINESS_INTELLIGENCE_SEARCH',
        'strategic planning objectives',
        {'limit': 5}
    )
);
```

### 3. Dashboard Verification

Check the dashboard shows:
- Total document count
- Category breakdown
- Recent processing activity
- Top strategic insights

## 🚨 Troubleshooting

### Common Issues and Solutions

#### Google Drive Authentication

**Issue**: `google.auth.exceptions.RefreshError`
**Solution**: 
1. Delete `config/token.json`
2. Re-run the pipeline to trigger re-authentication
3. Complete browser OAuth flow

#### Snowflake Connection

**Issue**: `snowflake.connector.errors.DatabaseError`
**Solutions**:
- Verify account URL format: `account.region.snowflakecomputing.com`
- Check user permissions and role assignments
- Ensure warehouse is running and accessible

#### Cortex AI Access

**Issue**: `Cortex function not available`
**Solutions**:
- Verify Cortex AI is enabled in your account
- Check your role has necessary privileges
- Try a different model name (e.g., `llama2-7b-chat`)

#### Document Processing

**Issue**: No documents found or processing failures
**Solutions**:
- Verify Google Drive folder ID is correct
- Check folder contains supported file types
- Ensure files are accessible (not restricted)

### Getting Help

1. **Check Logs**: Review `pipeline_run_*.log` files
2. **Verify Configuration**: Double-check `.env` file
3. **Test Components**: Run individual test scripts
4. **Contact Support**: Create GitHub issue with logs

## 🎯 Next Steps

After successful setup:

1. **Add More Documents**: Upload various business documents to your Google Drive folder
2. **Customize Categories**: Modify strategic categorization logic in `google_drive/client.py`
3. **Enhance AI Prompts**: Improve intelligence generation prompts in `snowflake/client.py`
4. **Build Dashboards**: Create custom visualizations using the processed data
5. **Automate Scheduling**: Set up regular pipeline runs using cron or workflow tools

## 📚 Additional Resources

- [Snowflake Cortex AI Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex)
- [Google Drive API Python Quickstart](https://developers.google.com/drive/api/quickstart/python)
- [Strategic Intelligence Best Practices](docs/STRATEGIC_INTELLIGENCE.md)

---

**Congratulations! Your Google Drive to Snowflake Intelligence pipeline is now ready to transform business documents into actionable insights! 🎉**