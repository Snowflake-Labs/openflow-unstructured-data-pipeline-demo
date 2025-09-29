# Snowflake Intelligence Demo: Google Drive Document Intelligence Guide

## Overview

**Objective**: Demonstrate the complete **Google Drive → OpenFlow → Cortex Search → Business Intelligence**  
pipeline using realistic festival operations business documents.

**Duration**: 15-30 minutes (flexible)  
**Audience**: Executive leadership, operations managers, compliance teams, knowledge workers  
**Data**: 16 converted business documents (3 PDF, 2 PPTX, 2 DOCX, 9 JPG) across 4 business categories

## Demo Architecture

```text
📁 Google Shared Drive Documents → 🔄 OpenFlow (Google Drive Connector → 🧠 Cortex Search ) → 📊 Snowflake Intelligence
```

## Pre-Demo Setup

### 📁 Google Shared Drive Structure

**Recommended folder organization for "Festival Operations" shared drive**:

```text
Festival Operations/
├── Strategic Planning/
│   └── Expansion Strategy 2025.jpg (5 image files: 0.jpg, 1.jpg, 2.jpg, 3.jpg, 4.jpg)
├── Executive Meetings/
│   └── Q4 2024 Board Minutes.docx
├── Financial Reports/
│   └── Q3 2024 Analysis.pdf
├── Projects/
│   └── Sound System Upgrade 2024.docx
├── Operations/
│   └── Venue Setup Guide.jpg (4 image files: 0.jpg, 1.jpg, 2.jpg, 3.jpg)
├── Compliance/
│   └── Health Safety Standards.pdf
├── Vendors/
│   └── Audio Service Contract.pdf
├── Training/
│   └── Customer Service Excellence.pptx
└── Analysis/
    └── Summer 2024 Review.pptx
```

#### Document Summary

Total: 16 converted documents across 9 focused business folders

> [!TIP]
> Use the `task create-google-drive-folder-structure` command to create the folder structure in Google Drive.

**Setup Instructions**:

1. Create "Festival Operations" shared drive in Google Drive
2. Establish folder hierarchy as shown above
3. Upload converted documents to appropriate folders
4. Configure OpenFlow Google Drive connector with shared drive access
5. Set appropriate sharing permissions for demo accounts

### ✅ Technical Requirements

#### Google Drive & Google Cloud Prerequisites

- [ ] **Google Admin Access**: Google user with Super Admin permissions
- [ ] **Google Cloud Project** with the following roles:
  - Organization Policy Administrator
  - Organization Administrator
- [ ] **Service Account Configuration**:
  - Enable service account key creation (disabled by default in Google Cloud)
  - Create service account and download JSON key file
  - Configure domain-wide delegation with required OAuth scopes:
    - `https://www.googleapis.com/auth/drive`
    - `https://www.googleapis.com/auth/drive.metadata.readonly`
    - `https://www.googleapis.com/auth/admin.directory.group.member.readonly`
    - `https://www.googleapis.com/auth/admin.directory.group.readonly`
    - `https://www.googleapis.com/auth/drive.file`
    - `https://www.googleapis.com/auth/drive.metadata`

#### Snowflake Account Prerequisites

- [ ] **Snowflake Account**: Active account in AWS Commercial Regions
- [ ] **OpenFlow Setup**: BYOC or Snowflake Deployment configured
- [ ] **Service User Configuration**:
  - Create Snowflake service user with type `SERVICE`
  - Configure key-pair authentication for service user
  - Grant appropriate database privileges
- [ ] **Secrets Management** (Recommended):
  - Configure AWS, Azure, or HashiCorp secrets manager
  - Store public/private keys in secret store
  - Set up Parameter Provider in OpenFlow
- [ ] **Cortex Search**: Enabled for document intelligence queries

#### Demo-Specific Requirements

- [ ] **Document Collection**: 16 converted documents (3 PDF, 2 PPTX, 2 DOCX, 9 JPG)
- [ ] **Google Shared Drive**: "Festival Operations" shared drive with proper folder structure
- [ ] **Multi-format Processing**: OpenFlow configured for PDF, DOCX, PPTX, JPG extraction
- [ ] **Database Setup**: `kamesh_openflow_unstructured_demo.festivals_ops` schema created

> [!IMPORTANT]
> **Complete Setup Guide**: For detailed Google Drive connector setup, follow the official  
> [Snowflake OpenFlow Google Drive Connector documentation](https://docs.snowflake.com/user-guide/data-integration/openflow/connectors/google-drive/setup)

## Demo Document Categories (Structured Intelligence Approach)

### 📋 Category 1: Strategic Planning & Executive Intelligence

#### Document Focus

Multi-format executive decision-making and strategic direction

#### Local → Google Shared Drive Mapping

- `sample-data/google-drive-docs/Strategic Planning/2025-Festival-Expansion-Strategy-*.jpg`  
  → `Festival Operations/Strategic Planning/Expansion Strategy 2025.jpg`
- `sample-data/google-drive-docs/Executive Meetings/Board-Meeting-Minutes-Q4-2024.docx`  
  → `Festival Operations/Executive Meetings/Q4 2024 Board Minutes.docx`
- `sample-data/google-drive-docs/Financial Reports/Q3-2024-Financial-Analysis.pdf`  
  → `Festival Operations/Financial Reports/Q3 2024 Analysis.pdf`

> [!TIP]
> **Quick Copy Command**: `task copy-category-1-strategic`
>
> **Copy All Categories**: `task copy-all-categories`

#### Multi-Format Document Intelligence

- **Strategic Expansion (JPG Visual)**: Market analysis diagrams, revenue growth charts, geographic expansion maps
- **Board Minutes (DOCX Collaborative)**: Executive decisions, strategic governance, quarterly reviews
- **Financial Analysis (PDF Formal)**: Revenue performance, cost analysis, investment ROI calculations

#### Business Value

Cross-format strategic intelligence extraction for executive decision support

#### Sample Query

*"What are our 2025 expansion plans across all document formats - show me visual charts, meeting decisions,  
and financial projections?"*

---

### 🎯 Category 2: Operations Excellence & Technology Modernization

#### Document Focus

Multi-format operational procedures and infrastructure investment

#### Local → Google Shared Drive Mapping

- `sample-data/google-drive-docs/Projects/Sound-System-Modernization-Project-Charter.docx`  
  → `Festival Operations/Projects/Sound System Upgrade 2024.docx`
- `sample-data/google-drive-docs/Operations/Venue-Setup-Operations-Manual-*.jpg`  
  → `Festival Operations/Operations/Venue Setup Guide.jpg`
- `sample-data/google-drive-docs/Analysis/Post-Event-Analysis-Summer-2024.pptx`  
  → `Festival Operations/Analysis/Summer 2024 Review.pptx`

> [!TIP]
> **Quick Copy Command**: `task copy-category-2-operations`
>
> **Copy All Categories**: `task copy-all-categories`

#### Multi-Format Document Intelligence

- **Project Charter (DOCX Collaborative)**: $2.8M technology investment, 18-month timeline, stakeholder collaboration
- **Operations Manual (JPG Visual)**: Standardized procedures, safety protocols, equipment management diagrams
- **Post-Event Analysis (PPTX Presentation)**: Performance review, incident analysis, improvement recommendations

#### Business Value

Cross-format operational optimization and technology investment justification

#### Sample Query

*"Show me all technology modernization projects across formats - project documentation, visual procedures,  
and presentation analysis"*

---

### 🛡️ Category 3: Compliance & Risk Management

#### Document Focus

Multi-format regulatory compliance and risk mitigation strategies

#### Local → Google Shared Drive Mapping

- `sample-data/google-drive-docs/Compliance/Health-Safety-Policy.pdf`  
  → `Festival Operations/Compliance/Health Safety Standards.pdf`
- `sample-data/google-drive-docs/Vendors/Audio-Equipment-Service-Agreement.pdf`  
  → `Festival Operations/Vendors/Audio Service Contract.pdf`
- `sample-data/google-drive-docs/Analysis/Post-Event-Analysis-Summer-2024.pptx`  
  → `Festival Operations/Analysis/Summer 2024 Review.pptx`

> [!TIP]
> **Quick Copy Command**: `task copy-category-3-compliance`
>
> **Copy All Categories**: `task copy-all-categories`

#### Multi-Format Document Intelligence

- **Health & Safety Policy (PDF Formal)**: Medical procedures, safety standards, regulatory compliance requirements
- **Audio Service Agreement (PDF Contract)**: Vendor contracts, service level agreements, legal terms, liability coverage
- **Post-Event Analysis (PPTX Presentation)**: Incident reports, risk assessments, mitigation strategies, visual analytics

#### Business Value

Cross-format risk management, regulatory adherence, and compliance documentation

#### Sample Query

*"What health and safety policies are in effect across all formats - show me formal policies, vendor agreements,  
and incident analysis presentations?"*

---

### 🎓 Category 4: Knowledge Management & Staff Development

#### Document Focus

Multi-format training programs and organizational knowledge sharing

#### Local → Google Shared Drive Mapping

- `sample-data/google-drive-docs/Training/Customer-Service-Training-Guide.pptx`  
  → `Festival Operations/Training/Customer Service Excellence.pptx`
- `sample-data/google-drive-docs/Operations/Venue-Setup-Operations-Manual-*.jpg`  
  → `Festival Operations/Operations/Venue Setup Guide.jpg`
- `sample-data/google-drive-docs/Executive Meetings/Board-Meeting-Minutes-Q4-2024.docx`  
  → `Festival Operations/Executive Meetings/Q4 2024 Board Minutes.docx`

> [!TIP]
> **Quick Copy Command**: `task copy-category-4-knowledge`
>
> **Copy All Categories**: `task copy-all-categories`

#### Multi-Format Document Intelligence

- **Training Guide (PPTX Presentation)**: Staff onboarding slides, service excellence frameworks, customer personas
- **Operations Manual (JPG Visual)**: Procedural knowledge diagrams, equipment management visuals, safety protocol charts
- **Board Minutes (DOCX Collaborative)**: Leadership decisions, strategic context, organizational direction, meeting notes

#### Business Value

Cross-format knowledge preservation, staff development, and cross-functional learning

#### Sample Query

*"Find all training materials across formats - show me presentation slides, visual procedures,  
and meeting decisions for staff development"*

## Demo Execution Flows

### 🚀 Option A: Executive Intelligence Demo (30 minutes)

```text
Strategic Documents → Show OpenFlow ingestion → Query strategic insights →
Operations Documents → Query technology investments →
Compliance Documents → Query risk management →
Multi-Format Analysis → Demonstrate comprehensive intelligence extraction
```

### ⚡ Option B: Focused Business Intelligence (15 minutes)

```bash
# Focus on high-value strategic and operational documents
# Key queries: Strategic planning, technology investments, operational excellence
# Emphasize business value and executive decision support
```

### 📊 Option C: Complete Document Intelligence (25 minutes)

```text
Categories 1-2: Strategic + Operations → Business intelligence foundation
Categories 3-4: Compliance + Training → Risk management and knowledge sharing
```

## Interactive Cortex Search Questions

### 📊 Strategic Business Intelligence Queries

#### Executive Decision Support

- *"What are our 2025 expansion plans and target markets?"*
- *"Show me all financial analysis and revenue projections"*
- *"Which strategic initiatives require the largest investments?"*

#### Investment & Technology Planning

- *"Find all technology modernization projects and their budgets"*
- *"What is the business case for our sound system upgrade?"*
- *"Show me ROI analysis for major infrastructure investments"*

#### Market & Competitive Intelligence

- *"What market expansion opportunities are documented?"*
- *"Show me competitive positioning and strategic advantages"*

### 🏢 Operational Excellence Analysis

#### Process Optimization

- *"What operational improvements were implemented after summer 2024?"*
- *"Show me venue setup procedures and safety protocols"*  
- *"Find all standardization initiatives across operations"*

#### Technology & Infrastructure

- *"What technology modernization projects are documented?"*
- *"Find all equipment and infrastructure upgrade plans"*
- *"Show me operational efficiency improvements and their impact"*

### 🛡️ Compliance & Risk Management

#### Policy & Regulatory Compliance

- *"What health and safety policies are currently in effect?"*
- *"Find all incident reports and their resolutions"*
- *"Show me compliance requirements across all business areas"*

#### Vendor & Contract Management

- *"What vendor contracts and service agreements are active?"*
- *"Find all service level agreements and performance metrics"*
- *"Show me vendor relationship documentation and evaluations"*

### 💰 Business Intelligence & ROI

#### Financial Performance Analysis

- *"Show me Q3 2024 financial performance and key metrics"*
- *"What are the ROI projections for our major investments?"*
- *"Find all budget analysis and cost optimization initiatives"*

#### Strategic Planning Intelligence

- *"What expansion opportunities offer the highest revenue potential?"*
- *"Show me market analysis and competitive positioning strategies"*

### 🎓 Knowledge Management & Collaboration

#### Training & Development Intelligence

- *"Find all training materials and staff development programs"*
- *"What knowledge sharing initiatives are documented?"*
- *"Show me cross-functional collaboration patterns"*

#### Document Intelligence Patterns

- *"Which documents have the most collaboration and comments?"*
- *"Find all version control and document evolution patterns"*
- *"Show me knowledge assets across different business functions"*

## Step-by-Step Demo Script

### Phase 1: Setup & Context (2-3 minutes)

**Opening**:
> "Today we'll see how Snowflake Intelligence transforms unstructured business documents  
> into actionable strategic intelligence using real festival operations documentation."

**Show**:

- Google Drive document collection with 16 converted business documents across 4 formats
- OpenFlow document processing pipeline configuration for multi-format extraction
- Cortex Search interface ready for cross-format intelligence processing

### Phase 2: Document Intelligence Pipeline (5-8 minutes)

**Demonstrate**:

1. **Document Collection Overview**
   - Show diverse document formats (PDF, DOCX, PPTX, JPG, MD)
   - Point out business personas: CEO, CFO, Operations Manager, etc.

2. **OpenFlow Document Processing**
   - Show documents being ingested from Google Drive
   - Highlight metadata extraction (authors, versions, collaboration data)

3. **Cortex Search Multi-Format Indexing**
   - Show unstructured content being processed across formats
   - Explain natural language query capability for business intelligence

### Phase 3: Interactive Analytics (8-12 minutes)

**Query Progression**:

1. **Start Simple**: *"What are our 2025 expansion plans?"*
   - Expected: Market expansion strategy, 15% revenue growth targets, 3 new markets
   - **Business Value**: Strategic decision support for executive leadership

2. **Build Complexity**: *"Find all technology modernization projects and their budgets"*
   - Expected: Sound system upgrade ($2.8M), 18-month timeline, ROI analysis
   - **Business Value**: Investment justification and resource allocation planning

3. **Multi-Format Analysis**
   - **Query**: *"Show me health and safety policies across all document formats"*
   - Expected: Health policy (PDF), training guide (PPTX), operations manual (JPG)
   - **Business Value**: Comprehensive compliance documentation and risk management

4. **Cross-Functional Intelligence**
   - **Query**: *"Which documents have the most collaboration and strategic importance?"*
   - Expected: Operations manual (22 comments), expansion strategy (18 comments), board minutes
   - **Business Value**: Knowledge management and organizational decision-making insights

5. **Predictive Business Intelligence**: *"What operational risks and mitigation strategies are documented?"*
   - Expected: Technology risks, safety concerns, financial constraints, strategic solutions
   - **Business Value**: Proactive risk management and business continuity planning

### Phase 4: Business Impact (3-5 minutes)

**Quantified Results**:

- **Document Intelligence**: 16 converted documents across 4 business format categories processed
- **Strategic Planning**: $2.8M technology investment with ROI analysis and business case  
- **Multi-Format Processing**: 4 document formats (PDF, DOCX, PPTX, JPG) unified for comprehensive intelligence

**Scalability Vision**:

- Current: 16 converted business documents, multi-format processing, cross-format analytics
- Enterprise: Thousands of documents, multiple business units, predictive multi-format business intelligence

## Audience-Specific Talking Points

### For C-Level Executives

- **Strategic Intelligence**: "Business documents become actionable strategic intelligence for $2.8M+ investment decisions"
- **Market Expansion**: "Document intelligence reveals 15% revenue growth opportunities across 3 new markets"  
- **Competitive Advantage**: "Multi-format document processing drives executive decision-making excellence"

### For Operations Teams

- **Process Standardization**: "Venue setup procedures and operational manuals drive consistency and efficiency"
- **Technology Modernization**: "Infrastructure upgrade projects with clear timelines and business cases"
- **Risk Mitigation**: "Incident analysis and safety policies provide proactive operational protection"

### For Compliance Teams

- **Regulatory Adherence**: "Health and safety policies ensure comprehensive compliance documentation"
- **Audit Trail**: "Document versioning and collaboration patterns provide complete governance visibility"
- **Risk Management**: "Cross-functional document intelligence identifies and mitigates operational risks"

### For Data/IT Teams

- **Multi-Format Processing**: "Unstructured documents → structured intelligence across PDF, DOCX, PPTX, JPG formats"
- **Integration Capabilities**: "Google Drive document intelligence + Snowflake business systems"
- **Automation Potential**: "Automated document processing and business intelligence extraction"

## Success Metrics & Follow-up

### Engagement Indicators

- **Executive Questions**: Strategic intelligence queries from business leaders
- **Use Case Alignment**: Connecting document intelligence scenarios to organizational challenges
- **Next Steps Interest**: Requests for technical implementation and business case details

### Immediate Follow-up Actions

- **Technical Deep Dive**: Google Drive OpenFlow architecture and implementation planning session
- **Business Case Development**: ROI modeling for document intelligence and multi-format processing
- **Pilot Program Design**: Proof-of-concept with audience's actual business document collection

### Demo Performance Expectations

- **Query Response Time**: < 5 seconds for complex natural language questions
- **Insight Quality**: Specific, actionable business recommendations
- **Business Value Articulation**: Clear ROI and operational impact demonstration

## Troubleshooting & Backup Plans

### Technical Issues

- **Google Drive Connection Problems**: Use pre-loaded document screenshots and metadata displays
- **OpenFlow Pipeline Delays**: Show cached document processing video
- **Cortex Search Latency**: Have key query results pre-captured for business intelligence scenarios

### Audience Engagement

- **Low Participation**: Use backup strategic intelligence questions from specific categories
- **Technical Audience**: Focus on multi-format processing architecture and implementation details  
- **Executive Audience**: Emphasize ROI, strategic intelligence, and competitive advantages

### Time Management

- **Running Short**: Use Option B (focused 15-minute business intelligence demo)
- **Extended Time**: Add advanced document intelligence queries from all categories
- **Audience Specific**: Adjust query selection based on strategic vs operational vs compliance interests

---

## Quick Reference Command Sequence

```bash
# Demo Preparation - All document formats included in Git repository
# Local documents are ready for Google Drive upload per folder structure

# Document Intelligence Demo Flow
# Category 1: Strategic & Executive Intelligence (Multi-Format)
# Category 2: Operations Excellence & Technology (Multi-Format)
# Category 3: Compliance & Risk Management (Multi-Format)
# Category 4: Knowledge Management & Training (Multi-Format)

# Optional: Document Management Commands (if regeneration needed)
# task convert-all-docs            # Regenerate all document formats
# task clean-converted-docs        # Remove converted documents for reset
```

## Expected Business Outcomes

### Strategic Intelligence Impact

- **Investment Decision Support**: $2.8M technology modernization with complete ROI analysis and business case
- **Market Expansion Intelligence**: 15% revenue growth opportunities across 3 new markets documented
- **Executive Decision Acceleration**: Board minutes and financial analysis drive strategic planning

### Operational Excellence

- **Process Standardization**: Venue operations and safety procedures drive 40% efficiency improvement
- **Technology Modernization**: 18-month infrastructure upgrade timeline with clear milestones
- **Cross-Functional Collaboration**: Document intelligence enables automated knowledge sharing

### Risk Management & Compliance

- **Regulatory Adherence**: Health policies and safety documentation ensure complete compliance coverage
- **Operational Risk Mitigation**: Incident analysis and mitigation strategies prevent business disruption
- **Audit Trail Completion**: Document versioning and collaboration provide comprehensive governance visibility

---

**This complete demo execution guide provides everything needed to demonstrate how unstructured business  
documents become actionable strategic intelligence through Snowflake Intelligence and Cortex Search.**
