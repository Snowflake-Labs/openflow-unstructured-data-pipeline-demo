# Unstructured Document Intelligence Demo

*Powered by Snowflake OpenFlow and Cortex*

Transform your Google Drive business documents into actionable strategic intelligence with the complete OpenFlow → Cortex Search → Snowflake Intelligence pipeline.

## 🚀 **[→ Access Full Documentation Site](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo)**

*Complete setup guides, business-focused demos, and step-by-step tutorials*

> **⚠️ IMPORTANT PREREQUISITE**: This demo requires **Snowflake OpenFlow**, which is currently available only  
> for **Enterprise accounts** as **BYOC (Bring Your Own Cloud)** or **SPCS (Snowpark Container Services)  
> Public Preview**. Contact your Snowflake account team to enable OpenFlow access.

## 🚀 Executive Summary

This demonstration showcases how **Snowflake Intelligence** with **Cortex Search** transforms unstructured business  
documents from **Google Drive** into queryable strategic intelligence through **OpenFlow** data processing.

**Business Impact**: Convert scattered business documents (PDFs, presentations, Word docs, images) into a unified  
intelligence platform that executives can query in natural language to make data-driven decisions.

**ROI Highlight**: Enable non-technical business users to extract insights from documents without SQL knowledge,  
reducing time-to-insight by 90% and democratizing access to organizational knowledge.

---

## 🌟 What This Demo Provides

### **Complete Documentation Site**

📖 **[Professional Documentation](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo)** with:

- **Setup Guides** - Prerequisites, database setup, OpenFlow configuration
- **Business Demos** - 4 category-specific presentations ready for different audiences  
- **AI Integration** - Snowflake Intelligence agent setup for conversational queries
- **Reference Materials** - Sample questions, commands, troubleshooting

### **Business-Ready Demo Categories**

| **Demo Category** | **Target Audience** | **Business Focus** |
|------------------|-------------------|------------------|
| **🎯 Strategic Planning** | C-level executives, board members | Investment decisions, market expansion |
| **🔧 Operations Excellence** | Operations managers, tech leaders | Process optimization, modernization |
| **⚖️ Compliance & Risk** | Compliance officers, audit teams | Policy enforcement, regulatory adherence |
| **📚 Knowledge Management** | HR teams, training managers | Staff development, knowledge sharing |

**[→ Browse All Demo Categories](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/demos/)**

### Competitive Advantages

- **✅ Multi-Format Processing**: PDF, DOCX, PPTX, JPG - all in one platform
- **✅ Natural Language Queries**: "What are our 2025 expansion plans?" vs complex SQL
- **✅ Enterprise Security**: Snowflake's enterprise-grade security for sensitive documents
- **✅ Scalable Intelligence**: Handles thousands of documents with sub-second query response

## 🚀 Quick Start Options

### **Option 1: Full Documentation Experience (Recommended)**

🌐 **[Browse Complete Site](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo)**

- Visual setup guides with screenshots
- Business-focused demo presentations  
- Copy-pasteable sample queries
- AI integration tutorials

### **Option 2: Technical Quick Start**

For experienced users who want immediate setup:

```bash
# Run the provided setup script
snow -f sql/setup.sql
```

**What the setup script creates:**

- ✅ **Role**: `FESTIVAL_DEMO_ROLE` with appropriate permissions
- ✅ **Warehouse**: `FESTIVAL_DEMO_S` for compute resources  
- ✅ **Database**: `OPENFLOW_FESTIVAL_DEMO` for data storage
- ✅ **Schema**: `FESTIVAL_OPS` for organized data structure

**Alternative - Manual SQL:**

```sql
-- Or run these commands individually in your Snowflake worksheet
CREATE ROLE IF NOT EXISTS FESTIVAL_DEMO_ROLE;
CREATE WAREHOUSE IF NOT EXISTS FESTIVAL_DEMO_S;
CREATE DATABASE IF NOT EXISTS OPENFLOW_FESTIVAL_DEMO;
CREATE SCHEMA IF NOT EXISTS OPENFLOW_FESTIVAL_DEMO.FESTIVAL_OPS;
```

**Next Steps:**

1. 📋 **[Prerequisites](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/getting-started/prerequisites/)** - Technical requirements
2. ⚡ **[Quick Setup](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/getting-started/quick-setup/)** - 15-minute streamlined setup
3. 🔧 **[OpenFlow Setup](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/getting-started/setup-openflow/)** - Connector configuration
4. 🎯 **[Demo Categories](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/demos/)** - Business presentations

---

## 💡 Sample Capabilities

Once your pipeline is set up, you can ask questions like:

```
🎯 Strategic: "What are our 2025 expansion strategies and expected ROI?"
🔧 Operations: "Find all technology modernization projects and their budgets"  
⚖️ Compliance: "Show me current health and safety policies"
📚 Knowledge: "What training materials are available for staff development?"
```

**[→ Browse 50+ Sample Questions](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/reference/sample-questions/)**

## 🏗️ What Gets Built

**End-to-End Architecture:**

```mermaid
graph LR
    A[📁 Google Drive] --> B[🔄 OpenFlow Pipeline]
    B --> C[🔍 Cortex Search Service]  
    C --> D[🤖 Snowflake Intelligence]
    D --> E[💬 Natural Language Queries]
    E --> F[📊 Business Insights]
```

**Core Components:**

- ✅ **Multi-format document processing** (PDF, DOCX, PPTX, JPG)
- ✅ **Automated Cortex Search service** creation and indexing
- ✅ **Business-focused demo categories** for different stakeholders  
- ✅ **Optional AI agent** for conversational document queries
- ✅ **Production-ready setup** with security and authentication

### Executive Use Cases Demonstrated

1. **Strategic Planning**: *"What are our 2025 expansion plans and expected ROI?"*
   - **Result**: Instant access to strategy documents, financial projections, board decisions

2. **Operational Excellence**: *"Show me all technology modernization projects and their budgets"*
   - **Result**: $2.8M sound system upgrade project with complete business case

3. **Compliance & Risk**: *"What health and safety policies are currently in effect?"*
   - **Result**: Complete policy documentation with incident analysis

4. **Knowledge Management**: *"Find all training materials and staff development programs"*
   - **Result**: Cross-department training resources with collaboration insights

### Financial Justification

- **Cost Avoidance**: Eliminate manual document searching (saves 2-3 hours/week per knowledge worker)
- **Revenue Acceleration**: Faster strategic decision-making enables quicker market responses
- **Risk Reduction**: Instant compliance documentation access reduces regulatory risks
- **Scalability**: Framework supports enterprise-wide knowledge management expansion

---

## 🛠️ For Sales Engineers & Solution Architects

### Technical Architecture

```text
📁 Google Shared Drive → 🔄 OpenFlow (Google Drive Connector) → 🧠 Cortex Search → 📊 Snowflake Intelligence
```

### Demo Environment Setup

#### Prerequisites

**Google Drive & Google Cloud Requirements**:

- **Google Admin Access**: Super Admin permissions for your organization
- **Google Cloud Project** with Organization Policy Administrator & Organization Administrator roles
- **Service Account Setup**:
  - Enable service account key creation (disabled by default)
  - Create service account with JSON key download
  - Configure domain-wide delegation with 6 required OAuth scopes
  - Full setup guide: [Google Drive connector documentation](https://docs.snowflake.com/user-guide/data-integration/openflow/connectors/google-drive/setup)

**Snowflake Requirements**:

- **Account**: **Enterprise Snowflake account** in AWS Commercial Regions  
- **OpenFlow**: **Available only for Enterprise accounts as BYOC (Bring Your Own Cloud) or SPCS  
  (Snowpark Container Services) Public Preview**
  - This demo requires Snowflake OpenFlow which is currently in Public Preview
  - Contact your Snowflake account team to enable OpenFlow access
- **Service User**: SERVICE type user with key-pair authentication
- **Secrets Manager**: AWS/Azure/HashiCorp recommended for production
- **Cortex Search**: Enabled for document intelligence queries

**Quick Start** (5 minutes):

1. Clone repository (all document formats included)
2. **Create Google Drive structure**: Use [Google Apps Script](./scripts/google-apps-script/) for automated folder creation
3. Upload 16 demo documents per [folder structure](./sample-data/google-drive-docs/README.md)
4. Configure OpenFlow Google Drive connector
5. Execute natural language queries

### Document Collection Overview

**16 Multi-Format Business Documents**:

- **3 PDF**: Formal contracts, policies, financial reports
- **2 PPTX**: Training materials, executive presentations  
- **2 DOCX**: Collaborative meeting minutes, project documentation
- **9 JPG**: Visual operational manuals, strategic planning diagrams

**4 Business Intelligence Categories**:

1. **Strategic & Executive Intelligence** (25%)
2. **Operations Excellence & Technology** (25%)
3. **Compliance & Risk Management** (25%)  
4. **Knowledge Management & Training** (25%)

### Sample Demo Queries

**Natural language queries for Snowflake Intelligence after OpenFlow-Cortex Search integration**:

```sql
-- Strategic Intelligence
"What are our 2025 expansion plans across all document formats?"

-- Operational Excellence  
"Find all technology modernization projects and their business cases"

-- Cross-Format Analysis
"Show me comprehensive insights across all 16 documents - what patterns emerge?"
```

*These queries become available once Google Drive documents are processed through the OpenFlow  
data pipeline and indexed by Cortex Search for intelligent document retrieval.*

### Technical Implementation Details

- **Multi-Format Processing**: Handles PDF text extraction, PPTX content parsing, DOCX collaboration data, JPG OCR
- **Metadata Extraction**: Document authors, versions, collaboration patterns, business categories
- **Natural Language Processing**: Cortex Search enables business user queries without SQL knowledge
- **Scalability**: Architecture supports thousands of documents with enterprise-grade performance

---

## 📁 Repository Structure & Resources

### 📊 Analytics & Demo Materials

- **[Analytics Documentation](./analytics/README.md)** - Complete business intelligence analysis and demo  
  execution guide
- **[Demo Execution Guide](./analytics/demo_execution_guide.md)** - Step-by-step presenter guide with  
  Google Drive setup
- **[Document Intelligence Analysis](./analytics/document_intelligence_analysis.md)** - Comprehensive analytics  
  opportunities and Cortex Search scenarios

### 📄 Sample Business Documents  

- **[Google Drive Document Collection](./sample-data/google-drive-docs/README.md)** - 16 realistic business documents  
  across 4 formats
- **[Document Metadata & Personas](./sample-data/google-drive-docs/document_metadata.md)** - Business context  
  and author personas

### 🛠️ Technical Resources

- **[SQL & Database](./sql/)** - Cortex Search service definitions and supporting queries
- **[Configuration](./Taskfile.yml)** - Automated tasks for document processing and demo setup  
- **[Taskfile Guide](./TASKFILE_README.md)** - Complete automation toolkit reference for demoers
- **[Scripts & Automation](./scripts/)** - Automated setup tools and utilities for demo preparation

### 🎯 Quick Navigation

| **Audience** | **Start Here** | **Key Resource** |
|-------------|---------------|-----------------|
| **Product Marketing** | [Business Use Cases](#-for-product-marketing-managers) | [Analytics Overview](./analytics/README.md) |
| **Executives** | [Business Impact](#-for-interested-executives) | [Demo Execution Guide](./analytics/demo_execution_guide.md) |
| **Technical Teams** | [Architecture](#technical-architecture) | [Document Collection](./sample-data/google-drive-docs/README.md) |

---

## 📚 Documentation & Resources

### **Complete Documentation Site**

🌐 **[Snowflake-labs.GitHub.io/OpenFlow-unstructured-data-pipeline-demo](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo)**

The documentation site provides:

- 🔧 **Technical Setup** - Prerequisites, database setup, connector configuration
- 🎯 **Business Demos** - Ready-to-present category demonstrations  
- 🤖 **AI Integration** - Snowflake Intelligence agent setup
- 📋 **Reference Guides** - Commands, sample questions, troubleshooting

### **Key Documentation Sections**

- **[Getting Started](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/getting-started/)** - Complete setup workflow
- **[Demo Categories](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/demos/)** - Business-focused presentations
- **[AI Integration](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/setup/snowflake-intelligence/)** - Snowflake Intelligence setup
- **[Reference](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/reference/)** - Sample questions and commands

### For Business Analysis

1. **Explore** [Document Intelligence Analysis](./analytics/document_intelligence_analysis.md) for analytics  
   opportunities
2. **Review** [Sample Queries](./analytics/document_intelligence_analysis.md#cortex-search-query-opportunities)  
   for business scenarios
3. **Understand**  
   [Business Value Propositions](./analytics/document_intelligence_analysis.md#business-value-propositions)  
   for stakeholder conversations

### For Technical Implementation

1. **Review** [Architecture](#technical-architecture) and technical requirements
2. **Examine** [Sample Documents](./sample-data/google-drive-docs/) for data understanding
3. **Configure** [Cortex Search Service](./sql/cortex_search.sql) per Snowflake requirements
4. **Implement** OpenFlow Google Drive connector with provided document collection

---

## 📈 Business Value Summary

| **Metric** | **Current State** | **With Document Intelligence** | **Improvement** |
|-----------|------------------|-------------------------------|-----------------|
| **Document Search Time** | 30-60 minutes manual search | 5-second natural language query | **90% reduction** |
| **Cross-Format Analysis** | Impossible without manual review | Instant insights across all formats | **New capability** |
| **Executive Insight Access** | Requires IT/analyst support | Self-service natural language queries | **100% democratization** |
| **Compliance Documentation** | Hours of manual document location | Instant policy and regulation access | **95% time savings** |

---

## 🎯 Next Steps

### Immediate Actions

1. **Schedule Demo**: Contact solution architect for live demonstration
2. **Assess Documents**: Identify your organization's Google Drive document collection
3. **Plan Implementation**: Review technical requirements and integration points
4. **ROI Planning**: Calculate business value using provided metrics and your document volumes

### Enterprise Implementation  

1. **Pilot Program**: Start with one department's document collection
2. **Scale Planning**: Design enterprise-wide document intelligence architecture  
3. **Integration Strategy**: Connect with existing business systems and workflows
4. **Change Management**: Train business users on natural language query capabilities

---

## 🎯 **Get Started Today**

### **[→ Access Complete Documentation](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo)**

**Ready to transform your unstructured business documents into strategic intelligence?**

1. 📖 **[Start with Prerequisites](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/getting-started/prerequisites/)**
2. ⚡ **[Follow Quick Setup](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/getting-started/quick-setup/)**
3. 🎯 **[Run Your First Demo](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/demos/)**
4. 🤖 **[Add AI Integration](https://snowflake-labs.github.io/openflow-unstructured-data-pipeline-demo/setup/snowflake-intelligence/)**

---

## 📞 Support & Resources

- 📖 **[Snowflake OpenFlow Docs](https://docs.snowflake.com/en/user-guide/data-load/openflow)**
- 🔍 **[Cortex Search Docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search)**  
- 🤖 **[Snowflake Intelligence Docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/snowflake-intelligence)**

---

⚠️ **Note**: This demo uses synthetic festival operations data for demonstration purposes. All business scenarios, names, and data are fictional and created specifically for showcasing Snowflake capabilities.
