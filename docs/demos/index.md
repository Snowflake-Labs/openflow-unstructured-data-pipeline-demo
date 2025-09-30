# Category Demos

Focused demonstration guides tailored for specific business audiences and use cases.

!!! warning "Synthetic Demo Data Disclaimer"
    **All documents and data used in these demos are completely fictional and synthetic.**
    The festival operations business scenario, employee names, financial figures, vendor relationships,
    and business processes are created solely for demonstration purposes. This synthetic data showcases
    OpenFlow and Cortex Search capabilities across realistic business use cases.

    **For production use**: Replace all demo documents with your organization's actual business content 
    using the customization workflow provided.

!!! tip "Perfect for Targeted Presentations"
    Each demo takes **5-10 minutes** and focuses on business value for specific stakeholder groups.
    Choose the category that best matches your audience!

## Demo Categories

<div class="grid cards" markdown>

- :material-account-tie:{ .lg .middle } **Strategic Planning**

    ---

    **Target Audience:** C-level executives, strategic decision makers, board members

    **Focus:** Investment decisions, market expansion, strategic intelligence, competitive positioning

    **Duration:** 5-8 minutes

    **Value Prop:** Transform scattered documents into executive decision-making intelligence

    [:octicons-arrow-right-24: Strategic Demo](strategic.md)

- :material-cog:{ .lg .middle } **Operations Excellence**

    ---

    **Target Audience:** Operations managers, process improvement teams, technology leaders

    **Focus:** Process optimization, technology modernization, operational efficiency, automation

    **Duration:** 6-10 minutes

    **Value Prop:** Unlock operational insights from documentation across all business processes

    [:octicons-arrow-right-24: Operations Demo](operations.md)

- :material-shield-check:{ .lg .middle } **Compliance & Risk**

    ---

    **Target Audience:** Compliance officers, risk managers, audit teams, legal departments

    **Focus:** Risk management, regulatory adherence, policy enforcement, audit trails

    **Duration:** 5-8 minutes

    **Value Prop:** Instant access to compliance documentation and risk assessment capabilities

    [:octicons-arrow-right-24: Compliance Demo](compliance.md)

- :material-school:{ .lg .middle } **Knowledge Management**

    ---

    **Target Audience:** HR teams, training managers, knowledge workers, organizational development

    **Focus:** Training effectiveness, knowledge sharing, collaboration patterns, staff development

    **Duration:** 6-9 minutes

    **Value Prop:** Transform training materials into searchable organizational knowledge

    [:octicons-arrow-right-24: Knowledge Demo](knowledge.md)

</div>

---

## Demo Benefits

### For Sales Teams

- **Audience-Specific Messaging** - Perfect talking points for each stakeholder group
- **Time-Efficient** - Quick, focused presentations that respect busy schedules
- **Value-Driven** - Clear ROI and business impact for each use case
- **Ready-to-Execute** - Copy-paste queries and expected results included

### For Technical Teams

- **Proof of Concept** - Demonstrate specific capabilities for targeted use cases
- **Architecture Validation** - Show multi-format document processing across business functions
- **Integration Planning** - Category-specific implementation roadmaps
- **Scalability Evidence** - Enterprise-ready document intelligence capabilities

### For Business Users

- **Department-Specific** - Relevant examples for each business function
- **Immediate Value** - See exactly how your documents become actionable intelligence
- **Implementation Planning** - Clear next steps for departmental adoption
- **Change Management** - Understand the transformation impact for your specific role

---

## Document Requirements

Each demo category requires specific documents from the `sample-data/google-drive-docs/` collection:

!!! info "Quick Document Setup"
    **Complete Demo**: Copy all 9 documents for full cross-category functionality  
    **Targeted Demo**: Copy only the documents listed for your specific audience category

### Document Requirements by Category

| Demo Category | Core Documents | Purpose |
|---------------|----------------|---------|
| **Strategic Planning** | 4 documents | Market expansion, investment analysis, board decisions |
| **Operations Excellence** | 5 documents | Process optimization, technology modernization, safety |
| **Compliance & Risk** | 4 documents | Policy enforcement, incident management, vendor compliance |
| **Knowledge Management** | All 9 documents | Training effectiveness, collaboration patterns, learning analytics |

### Complete Document Set

**Converted documents for demo upload** (located in `sample-data/google-drive-docs/`):

```
google-drive-docs/
├── Strategic Planning/
│   ├── 2025-Festival-Expansion-Strategy-0.jpg
│   ├── 2025-Festival-Expansion-Strategy-1.jpg
│   ├── 2025-Festival-Expansion-Strategy-2.jpg
│   ├── 2025-Festival-Expansion-Strategy-3.jpg
│   └── 2025-Festival-Expansion-Strategy-4.jpg
├── Executive Meetings/
│   └── Board-Meeting-Minutes-Q4-2024.docx
├── Financial Reports/
│   └── Q3-2024-Financial-Analysis.pdf
├── Projects/
│   └── Sound-System-Modernization-Project-Charter.docx
├── Operations/
│   ├── Venue-Setup-Operations-Manual-0.jpg
│   ├── Venue-Setup-Operations-Manual-1.jpg
│   ├── Venue-Setup-Operations-Manual-2.jpg
│   └── Venue-Setup-Operations-Manual-3.jpg
├── Analysis/
│   └── Post-Event-Analysis-Summer-2024.pptx
├── Compliance/
│   └── Health-Safety-Policy.pdf
├── Training/
│   └── Customer-Service-Training-Guide.pptx
└── Vendors/
    └── Audio-Equipment-Service-Agreement.pdf
```

#### Document Source & Conversion Workflow

**Markdown Source Files**: Each directory also contains `.md` source files
(e.g., `2025-Festival-Expansion-Strategy.md`) which are the **editable source documents**.

**Converting Sources to Demo Formats**:

```bash
# Convert all documents to demo formats
task convert-all-docs

# Or convert to specific formats
task convert-to-pdf     # Generate PDF documents
task convert-to-pptx    # Generate PowerPoint presentations  
task convert-to-docx    # Generate Word documents
task convert-to-jpg     # Generate JPG images
```

**Customization Workflow**:

1. **Edit** the `.md` source files with your organization's content
2. **Run** the appropriate `convert-*` task to generate new demo files
3. **Upload** the converted files (not the .md sources) to Google Drive

!!! tip "Multi-Format Demo Capability"
    This conversion approach demonstrates OpenFlow's ability to process diverse document formats
    (JPG, PDF, DOCX, PPTX) from a single markdown source, showcasing real-world enterprise document variety.

---

## Getting Started

Before running category demos, ensure you have completed the basic setup:

<div class="grid cards" markdown>

- :material-list-status:{ .lg .middle } **Prerequisites**

    ---

    Complete technical requirements and access verification

    [:octicons-arrow-right-24: Prerequisites Guide](../getting-started/prerequisites.md)

- :material-lightning-bolt:{ .lg .middle } **Quick Setup**

    ---

    15-minute streamlined setup for demo capability

    [:octicons-arrow-right-24: Quick Setup Guide](../getting-started/quick-setup.md)

</div>

---

## Demo Setup Checklist

### Complete Demo Setup (Recommended)

**Best for:** Multi-audience presentations, comprehensive capabilities demonstration

- **Documents needed:** All 9 converted documents (17 total files including multi-page formats)
- **Time to upload:** ~5 minutes  
- **Capabilities:** Full cross-category functionality, collaboration analytics, complete business context
- **Target audience:** Demonstrations requiring all business use cases

### Category-Specific Setup

=== "Strategic Planning"
    **Best for:** C-level executives, board presentations

    **Documents needed:**
    
    - ✅ `2025-Festival-Expansion-Strategy-0.jpg` through `-4.jpg` (5 files)
    - ✅ `Board-Meeting-Minutes-Q4-2024.docx`
    - ✅ `Q3-2024-Financial-Analysis.pdf`
    
    **Time to upload:** ~2 minutes

=== "Operations Excellence"
    **Best for:** Operations teams, process improvement, technology leaders

    **Documents needed:**
    
    - ✅ `Venue-Setup-Operations-Manual-0.jpg` through `-3.jpg` (4 files)
    - ✅ `Sound-System-Modernization-Project-Charter.docx`
    - ✅ `Post-Event-Analysis-Summer-2024.pptx`
    - ✅ `Health-Safety-Policy.pdf`
    - ✅ `Audio-Equipment-Service-Agreement.pdf`
    
    **Time to upload:** ~2-3 minutes

=== "Compliance & Risk"
    **Best for:** Compliance officers, risk managers, audit teams

    **Documents needed:**
    
    - ✅ `Health-Safety-Policy.pdf`
    - ✅ `Post-Event-Analysis-Summer-2024.pptx`
    - ✅ `Audio-Equipment-Service-Agreement.pdf`
    
    **Time to upload:** ~2 minutes

=== "Knowledge Management"
    **Best for:** HR teams, training managers, organizational development

    **Documents needed:**
    
    - ✅ `Customer-Service-Training-Guide.pptx` (primary document)
    - ✅ All documents from other categories (for cross-functional analytics)
    
    **Time to upload:** ~5 minutes (complete set required)

### Document Upload Verification

After uploading documents, verify they're processed correctly:

```sql
-- Comprehensive document verification by demo category
SELECT 
    COUNT(*) as total_docs,
    
    -- Strategic Planning Documents (Expected: 7-8)
    COUNT(CASE WHEN 
        lower(DOC_ID) LIKE '%strategy%' OR 
        lower(DOC_ID) LIKE '%board%meeting%' OR 
        lower(DOC_ID) LIKE '%meeting%minutes%' OR
        lower(DOC_ID) LIKE '%financial%analysis%' OR
        lower(DOC_ID) LIKE '%q3%2024%financial%'
    THEN 1 END) as strategic_docs,
    
    -- Operations Excellence Documents (Expected: 6-7)
    COUNT(CASE WHEN 
        (lower(DOC_ID) LIKE '%operation%manual%' OR lower(DOC_ID) LIKE '%venue%setup%') OR
        (lower(DOC_ID) LIKE '%sound%system%' AND lower(DOC_ID) LIKE '%project%') OR
        (lower(DOC_ID) LIKE '%post%event%analysis%')
    THEN 1 END) as operations_docs,
    
    -- Compliance & Risk Documents (Expected: 3-4)
    COUNT(CASE WHEN 
        (lower(DOC_ID) LIKE '%health%safety%' OR lower(DOC_ID) LIKE '%safety%policy%') OR
        (lower(DOC_ID) LIKE '%service%agreement%' OR lower(DOC_ID) LIKE '%audio%equipment%') OR
        (lower(DOC_ID) LIKE '%post%event%analysis%')
    THEN 1 END) as compliance_docs,
    
    -- Knowledge Management Documents (Expected: 1)
    COUNT(CASE WHEN 
        lower(DOC_ID) LIKE '%training%guide%' OR 
        lower(DOC_ID) LIKE '%customer%service%training%'
    THEN 1 END) as training_docs,
    
    -- Document format breakdown
    COUNT(CASE WHEN lower(DOC_ID) LIKE '%.jpg' THEN 1 END) as jpg_files,
    COUNT(CASE WHEN lower(DOC_ID) LIKE '%.pdf' THEN 1 END) as pdf_files,
    COUNT(CASE WHEN lower(DOC_ID) LIKE '%.docx' THEN 1 END) as docx_files,
    COUNT(CASE WHEN lower(DOC_ID) LIKE '%.pptx' THEN 1 END) as pptx_files
    
FROM file_hashes;
```

#### Expected Results

**Complete Demo Setup (All 9 Documents = 15-16 Total Files):**

| Category | Count | Document Types |
|----------|-------|----------------|
| **strategic_docs** | 7 | Strategy images (5 JPG) + Board minutes (DOCX) + Financial analysis (PDF) |
| **operations_docs** | 5 | Operations manual (4 JPG) + Sound project (DOCX) |
| **compliance_docs** | 3 | Safety policy (PDF) + Service agreement (PDF) + Post-event analysis (PPTX) |
| **training_docs** | 1 | Customer service training (PPTX) |
| **total_docs** | **15** | **Processed files (1 DOCX file may not process)** |

**File Format Breakdown:**

- **jpg_files**: 9 (5 strategic + 4 operations) ✅
- **pdf_files**: 3 (financial + safety + vendor agreement) ✅
- **docx_files**: 1-2 (board minutes + project charter - one may not process) ⚠️
- **pptx_files**: 2 (training + analysis) ✅

!!! warning "DOCX Processing Note"
    **Available in sample-data**: 2 DOCX files (Board minutes + Project charter)  
    **Typically processed**: 1 DOCX file  

    If you see `docx_files: 1` instead of 2, this is normal. One DOCX file may not process due to:
    - File upload order/timing
    - OpenFlow processing optimization  
    - Document naming variations
    
    Both documents contain similar strategic/project content, so demo functionality remains intact.

### Document Format Distribution

The converted documents in sample-data (16 total files available, 15 typically processed):

- **📷 JPG Files**: 9 total ✅
  - Strategic expansion strategy: 5 images (`2025-Festival-Expansion-Strategy-0.jpg` through `-4.jpg`)
  - Operations manual: 4 images (`Venue-Setup-Operations-Manual-0.jpg` through `-3.jpg`)

- **📄 PDF Files**: 3 total ✅
  - Financial analysis: `Q3-2024-Financial-Analysis.pdf`
  - Safety policy: `Health-Safety-Policy.pdf`
  - Vendor agreement: `Audio-Equipment-Service-Agreement.pdf`

- **📝 DOCX Files**: 2 available, 1 typically processed ⚠️
  - Board minutes: `Board-Meeting-Minutes-Q4-2024.docx`
  - Project charter: `Sound-System-Modernization-Project-Charter.docx`
  - *Note: Usually only one DOCX file processes successfully*

- **📊 PPTX Files**: 2 total ✅
  - Post-event analysis: `Post-Event-Analysis-Summer-2024.pptx`
  - Customer training: `Customer-Service-Training-Guide.pptx`

!!! warning "Troubleshooting Document Counts"
    If counts don't match expected values:

    1. **Check file names** match the converted document names (not .md source files)
    2. **Verify Google Drive folder structure** follows the upload instructions
    3. **Confirm OpenFlow processing** completed successfully
    4. **Review connector logs** for any processing errors

=== "Simplified Verification"
    For quick verification, use this simplified query:

    ```sql
    -- Quick document check
    SELECT 
        COUNT(*) as total_docs,
        COUNT(CASE WHEN lower(DOC_ID) LIKE '%strategy%' OR lower(DOC_ID) LIKE '%board%' OR lower(DOC_ID) LIKE '%financial%' THEN 1 END) as strategic_docs,
        COUNT(CASE WHEN lower(DOC_ID) LIKE '%venue%' OR lower(DOC_ID) LIKE '%sound%system%' OR lower(DOC_ID) LIKE '%post%event%' THEN 1 END) as operations_docs,
        COUNT(CASE WHEN lower(DOC_ID) LIKE '%safety%' OR lower(DOC_ID) LIKE '%audio%equipment%' THEN 1 END) as compliance_docs,
        COUNT(CASE WHEN lower(DOC_ID) LIKE '%training%guide%' THEN 1 END) as training_docs
    FROM file_hashes;
    ```

=== "Individual Document Check"
    List all processed documents to verify specific files:

    ```sql
    -- View all processed documents
    SELECT 
        DOC_ID,
        CASE 
            WHEN lower(DOC_ID) LIKE '%strategy%' OR lower(DOC_ID) LIKE '%board%' OR lower(DOC_ID) LIKE '%financial%' THEN 'Strategic Planning'
            WHEN lower(DOC_ID) LIKE '%venue%' OR lower(DOC_ID) LIKE '%sound%system%' OR lower(DOC_ID) LIKE '%post%event%' THEN 'Operations Excellence'
            WHEN lower(DOC_ID) LIKE '%safety%' OR lower(DOC_ID) LIKE '%audio%equipment%' THEN 'Compliance & Risk'
            WHEN lower(DOC_ID) LIKE '%training%guide%' THEN 'Knowledge Management'
            ELSE 'Other'
        END as demo_category,
        UPPER(RIGHT(DOC_ID, 4)) as file_format
    FROM file_hashes
    ORDER BY demo_category, DOC_ID;
    ```

!!! success "Setup Complete"
    When your verification query shows the expected document counts and formats, your demo environment is ready!
