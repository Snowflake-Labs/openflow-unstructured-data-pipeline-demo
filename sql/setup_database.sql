-- Snowflake database setup for Unstructured Data Pipeline Demo
-- This script creates the necessary database, schema, and tables for the intelligence pipeline

-- Create database and schema
CREATE DATABASE IF NOT EXISTS UNSTRUCTURED_DEMO;
USE DATABASE UNSTRUCTURED_DEMO;

CREATE SCHEMA IF NOT EXISTS INTELLIGENCE;
USE SCHEMA INTELLIGENCE;

-- Create documents table to store metadata about processed documents
CREATE OR REPLACE TABLE DOCUMENTS (
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
);

-- Create document content table to store extracted text content
CREATE OR REPLACE TABLE DOCUMENT_CONTENT (
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
);

-- Create intelligence insights table to store Cortex AI generated insights
CREATE OR REPLACE TABLE INTELLIGENCE_INSIGHTS (
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
);

-- Create search index table for Cortex Search functionality
CREATE OR REPLACE TABLE SEARCH_INDEX (
    INDEX_ID VARCHAR(255) PRIMARY KEY,
    DOC_ID VARCHAR(255),
    CONTENT_CHUNK TEXT,
    EMBEDDINGS VECTOR(FLOAT, 768),
    CHUNK_METADATA VARIANT,
    INDEXED_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (DOC_ID) REFERENCES DOCUMENTS(DOC_ID)
);

-- Create views for easier querying and dashboard creation

-- Strategic overview view
CREATE OR REPLACE VIEW V_STRATEGIC_OVERVIEW AS
SELECT 
    d.STRATEGIC_CATEGORY,
    COUNT(*) as DOCUMENT_COUNT,
    AVG(ii.STRATEGIC_VALUE) as AVG_STRATEGIC_VALUE,
    AVG(ii.CONFIDENCE_SCORE) as AVG_CONFIDENCE,
    MAX(d.PROCESSED_TIME) as LAST_PROCESSED
FROM DOCUMENTS d
LEFT JOIN INTELLIGENCE_INSIGHTS ii ON d.DOC_ID = ii.DOC_ID
GROUP BY d.STRATEGIC_CATEGORY
ORDER BY AVG_STRATEGIC_VALUE DESC;

-- Recent insights view
CREATE OR REPLACE VIEW V_RECENT_INSIGHTS AS
SELECT 
    ii.INSIGHT_ID,
    ii.TITLE,
    ii.SUMMARY,
    ii.STRATEGIC_VALUE,
    ii.CONFIDENCE_SCORE,
    d.FILE_NAME,
    d.STRATEGIC_CATEGORY,
    ii.GENERATED_TIME
FROM INTELLIGENCE_INSIGHTS ii
JOIN DOCUMENTS d ON ii.DOC_ID = d.DOC_ID
WHERE ii.GENERATED_TIME >= CURRENT_DATE - 30
ORDER BY ii.STRATEGIC_VALUE DESC, ii.GENERATED_TIME DESC;

-- Document processing status view
CREATE OR REPLACE VIEW V_PROCESSING_STATUS AS
SELECT 
    d.DOC_ID,
    d.FILE_NAME,
    d.STRATEGIC_CATEGORY,
    d.PROCESSED_TIME,
    dc.PROCESSING_STATUS,
    COUNT(dc.CONTENT_ID) as CONTENT_CHUNKS,
    COUNT(ii.INSIGHT_ID) as INSIGHTS_GENERATED
FROM DOCUMENTS d
LEFT JOIN DOCUMENT_CONTENT dc ON d.DOC_ID = dc.DOC_ID
LEFT JOIN INTELLIGENCE_INSIGHTS ii ON d.DOC_ID = ii.DOC_ID
GROUP BY d.DOC_ID, d.FILE_NAME, d.STRATEGIC_CATEGORY, d.PROCESSED_TIME, dc.PROCESSING_STATUS
ORDER BY d.PROCESSED_TIME DESC;

-- Create stored procedures for common operations

-- Procedure to get strategic dashboard metrics
CREATE OR REPLACE PROCEDURE SP_GET_DASHBOARD_METRICS()
RETURNS VARIANT
LANGUAGE SQL
AS
$$
DECLARE
    metrics VARIANT;
BEGIN
    SELECT OBJECT_CONSTRUCT(
        'total_documents', (SELECT COUNT(*) FROM DOCUMENTS),
        'categories', (SELECT COUNT(DISTINCT STRATEGIC_CATEGORY) FROM DOCUMENTS),
        'insights_generated', (SELECT COUNT(*) FROM INTELLIGENCE_INSIGHTS),
        'avg_strategic_value', (SELECT AVG(STRATEGIC_VALUE) FROM INTELLIGENCE_INSIGHTS),
        'recent_processed', (SELECT COUNT(*) FROM DOCUMENTS WHERE PROCESSED_TIME >= CURRENT_DATE - 7),
        'completion_rate', (
            SELECT 
                ROUND(
                    COUNT(CASE WHEN dc.PROCESSING_STATUS = 'COMPLETED' THEN 1 END) * 100.0 / COUNT(*), 2
                )
            FROM DOCUMENT_CONTENT dc
        )
    ) INTO metrics;
    
    RETURN metrics;
END;
$$;

-- Procedure to search documents with advanced filtering
CREATE OR REPLACE PROCEDURE SP_SEARCH_DOCUMENTS(SEARCH_TERM VARCHAR, CATEGORY VARCHAR DEFAULT NULL, LIMIT_RESULTS INTEGER DEFAULT 10)
RETURNS TABLE(DOC_ID VARCHAR, FILE_NAME VARCHAR, CONTENT VARCHAR, STRATEGIC_CATEGORY VARCHAR, RELEVANCE_SCORE FLOAT)
LANGUAGE SQL
AS
$$
BEGIN
    LET query_filter VARCHAR := CASE 
        WHEN CATEGORY IS NOT NULL THEN ' AND d.STRATEGIC_CATEGORY = ''' || CATEGORY || ''''
        ELSE ''
    END;
    
    LET search_query VARCHAR := 
        'SELECT 
            d.DOC_ID,
            d.FILE_NAME,
            dc.RAW_CONTENT as CONTENT,
            d.STRATEGIC_CATEGORY,
            1.0 as RELEVANCE_SCORE
        FROM DOCUMENTS d
        JOIN DOCUMENT_CONTENT dc ON d.DOC_ID = dc.DOC_ID
        WHERE CONTAINS(UPPER(dc.RAW_CONTENT), UPPER(\'' || SEARCH_TERM || '\'))' ||
        query_filter ||
        ' ORDER BY d.PROCESSED_TIME DESC
        LIMIT ' || LIMIT_RESULTS;
    
    LET res RESULTSET := EXECUTE IMMEDIATE search_query;
    RETURN TABLE(res);
END;
$$;

-- Create sample data for testing (optional)
-- This can be used to verify the setup works correctly

-- Insert sample document metadata
INSERT INTO DOCUMENTS (
    DOC_ID, FILE_NAME, FILE_TYPE, STRATEGIC_CATEGORY, EXTRACTION_PRIORITY,
    DOWNLOAD_PATH, METADATA
) VALUES 
(
    'sample_001', 'Q4_Strategic_Plan.docx', 
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'strategic_planning', 10,
    '/sample/Q4_Strategic_Plan.docx',
    '{"sample": true, "created_for": "demo"}'
),
(
    'sample_002', 'Financial_Analysis_2024.xlsx', 
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'financial_analysis', 9,
    '/sample/Financial_Analysis_2024.xlsx',
    '{"sample": true, "created_for": "demo"}'
);

-- Insert sample content
INSERT INTO DOCUMENT_CONTENT (
    CONTENT_ID, DOC_ID, RAW_CONTENT, CONTENT_TYPE, PROCESSING_STATUS
) VALUES 
(
    'sample_001_content_1', 'sample_001', 
    'Executive Summary: Our Q4 strategic initiatives focus on market expansion, operational efficiency, and digital transformation. Key objectives include increasing market share by 15%, reducing operational costs by 8%, and implementing new customer engagement platforms.',
    'text', 'COMPLETED'
),
(
    'sample_002_content_1', 'sample_002',
    'Q4 Financial Performance: Revenue increased 12% year-over-year. Operating margins improved to 18.5%. Key growth drivers: new product launches, market expansion, operational efficiency gains.',
    'text', 'COMPLETED'
);

-- Insert sample insights
INSERT INTO INTELLIGENCE_INSIGHTS (
    INSIGHT_ID, DOC_ID, INSIGHT_TYPE, TITLE, SUMMARY, STRATEGIC_VALUE, CONFIDENCE_SCORE, MODEL_USED
) VALUES 
(
    'sample_insight_001', 'sample_001', 'strategic_analysis',
    'Q4 Strategic Growth Opportunities',
    'Analysis reveals strong potential for market expansion with focus on operational efficiency and digital transformation initiatives.',
    8, 0.92, 'sample_model'
),
(
    'sample_insight_002', 'sample_002', 'financial_analysis',
    'Strong Financial Performance Indicators',
    'Financial metrics show healthy growth trajectory with improved margins and revenue diversification opportunities.',
    7, 0.88, 'sample_model'
);

-- Grant necessary permissions (adjust roles as needed for your organization)
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA INTELLIGENCE TO ROLE DATA_ANALYST;
-- GRANT USAGE ON SCHEMA INTELLIGENCE TO ROLE DATA_ANALYST;
-- GRANT USAGE ON DATABASE UNSTRUCTURED_DEMO TO ROLE DATA_ANALYST;

COMMIT;