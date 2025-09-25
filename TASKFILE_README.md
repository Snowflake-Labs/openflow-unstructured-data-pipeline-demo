# Taskfile Reference Guide

Complete automation toolkit for the Snowflake OpenFlow Unstructured Data Pipeline Demo using [Task](https://taskfile.dev/).

## 🚀 Quick Start

### Prerequisites

1. **Install Task**: [taskfile.dev/#installation](https://taskfile.dev/#installation)

   ```bash
   # macOS
   brew install go-task/tap/go-task
   
   # Or download binary from releases
   ```

2. **Install Required Tools**:

   ```bash
   # Document conversion dependencies
   brew install pandoc imagemagick  # macOS
   ```

3. **Python Environment**:

   ```bash
   # Ensure uv is installed for Python dependency management
   pip install uv
   ```

### Basic Usage

```bash
# List all available tasks
task --list

# Run default task (sync environment)
task

# Run specific task
task convert-all-docs
```

---

## 📋 Available Tasks

### 🛠️ Environment & Setup

| Task | Description | Usage |
|------|-------------|-------|
| `default` | Default task - sync Python environment | `task` |
| `sync-env` | Synchronize Python environment with uv | `task sync-env` |
| `create-google-drive-folder-structure` | Create organized folder structure in Google Drive | `task create-google-drive-folder-structure` |
| `clean-work` | Clean up work directory files | `task clean-work` |

### 📄 Document Format Conversion

| Task | Description | Dependencies | Usage |
|------|-------------|--------------|-------|
| `check-pandoc` | Verify pandoc installation | None | `task check-pandoc` |
| `convert-to-pdf` | Convert markdown to PDF (3 formal documents) | pandoc | `task convert-to-pdf` |
| `convert-to-pptx` | Convert markdown to PowerPoint (2 presentations) | pandoc | `task convert-to-pptx` |
| `convert-to-docx` | Convert markdown to Word (2 collaborative docs) | pandoc | `task convert-to-docx` |
| `convert-to-jpg` | Convert markdown to JPG images (2 visual guides) | pandoc, imagemagick | `task convert-to-jpg` |
| `convert-all-docs` | **Convert all documents to optimized formats** | All above | `task convert-all-docs` |
| `clean-converted-docs` | Remove all converted files (keep .md originals) | None | `task clean-converted-docs` |

### 📁 Google Drive Deployment

| Task | Description | Prerequisites | Usage |
|------|-------------|---------------|-------|
| `copy-category-1-strategic` | Copy Strategic Planning & Executive docs | Converted documents | `task copy-category-1-strategic` |
| `copy-category-2-operations` | Copy Operations Excellence & Technology docs | Converted documents | `task copy-category-2-operations` |
| `copy-category-3-compliance` | Copy Compliance & Risk Management docs | Converted documents | `task copy-category-3-compliance` |
| `copy-category-4-knowledge` | Copy Knowledge Management & Training docs | Converted documents | `task copy-category-4-knowledge` |
| `copy-all-categories` | **Deploy all 16 documents to Google Drive** | All categories | `task copy-all-categories` |

---

## 🎯 Demo Workflows

### **Complete Demo Setup (Recommended)**

```bash
# Option A: Full local automation (requires Google Drive sync)
task convert-all-docs
task copy-all-categories

# Option B: Use Google Apps Script for folder creation (recommended)
# 1. Run Google Apps Script to create folder structure in Google Drive
# 2. Convert and manually upload documents
task convert-all-docs
# Then manually upload to Google Drive folders

# Result: 16 multi-format business documents ready for Snowflake OpenFlow
```

### **Development & Testing Workflow**

```bash
# Clean slate
task clean-converted-docs
task clean-work

# Convert specific format for testing
task convert-to-pdf

# Test deployment of single category
task copy-category-1-strategic
```

### **Demo Reset Workflow**

```bash
# Reset everything for fresh demo
task clean-converted-docs

# Quick rebuild for demo
task convert-all-docs
task copy-all-categories
```

---

## 📊 Document Categories & Formats

The demo organizes 16 business documents across 4 strategic categories:

### **Category 1: Strategic Planning & Executive Intelligence**

- **2025 Festival Expansion Strategy** (JPG) - Multi-page strategic overview
- **Board Meeting Minutes Q4 2024** (DOCX) - Collaborative executive documentation
- **Q3 2024 Financial Analysis** (PDF) - Formal financial reporting

### **Category 2: Operations Excellence & Technology Modernization**

- **Sound System Modernization Project Charter** (DOCX) - Project collaboration document
- **Venue Setup Operations Manual** (JPG) - Visual operational procedures
- **Post-Event Analysis Summer 2024** (PPTX) - Executive presentation format

### **Category 3: Compliance & Risk Management**

- **Health & Safety Policy** (PDF) - Formal policy documentation
- **Audio Equipment Service Agreement** (PDF) - Legal contract format

### **Category 4: Knowledge Management & Staff Development**

- **Customer Service Training Guide** (PPTX) - Training presentation materials

---

## ⚙️ Configuration & Variables

### **Environment Variables**

```yaml
vars:
  DOCS_DIR: "./sample-data/google-drive-docs"           # Source documents location
  GOOGLE_DRIVE_DIR: "~/Google Drive/Shared drives/Festival Operations"  # Target location
```

### **Google Drive Folder Structure**

**Recommended**: Use the [Google Apps Script](../scripts/google-apps-script/) for reliable folder creation.

**Alternative**: The `create-google-drive-folder-structure` task creates (requires local Google Drive sync):

```text
Festival Operations/
├── Strategic Planning/
├── Executive Meetings/  
├── Financial Reports/
├── Projects/
├── Operations/
├── Compliance/
├── Vendors/
├── Training/
└── Analysis/
```

---

## 🔧 Advanced Usage

### **Selective Document Processing**

```bash
# Convert only presentations
task convert-to-pptx

# Deploy only strategic documents  
task copy-category-1-strategic
```

### **Custom Document Conversion**

The conversion tasks support professional formatting:

- **PDF**: XeLaTeX engine, 1-inch margins, 11pt font
- **PPTX**: Custom template, slide-level 4, overflow protection
- **DOCX**: Standard Word format for collaboration
- **JPG**: 200 DPI, high quality, clean intermediate files

### **Template Management**

```bash
# Regenerate PowerPoint template
task create-pptx-template
```

---

## 🚨 Troubleshooting

### **Common Issues**

| Problem | Solution | Command |
|---------|----------|---------|
| "pandoc not found" | Install pandoc | `brew install pandoc` |
| "convert not found" | Install ImageMagick | `brew install imagemagick` |
| "Google Drive folder not found" | Create shared drive first | `task create-google-drive-folder-structure` |
| "No converted files to copy" | Run document conversion first | `task convert-all-docs` |

### **Verification Commands**

```bash
# Check tool installation
task check-pandoc

# Verify document conversion
ls sample-data/google-drive-docs/**/*.{pdf,pptx,docx,jpg}

# Check Google Drive deployment
ls ~/Google\ Drive/Shared\ drives/Festival\ Operations/
```

---

## 🎯 Demo Execution Tips

### **For Sales Engineers**

1. **Pre-Demo**: `task convert-all-docs copy-all-categories`
2. **During Demo**: Show organized Google Drive structure
3. **Post-Demo**: `task clean-converted-docs` to reset

### **For Solution Architects**

1. **Architecture Review**: Examine document formats and metadata
2. **Custom Scenarios**: Use selective category deployment
3. **Technical Deep-Dive**: Show conversion process and file optimization

### **For Product Managers**

1. **Business Value**: Focus on 4 strategic categories
2. **Use Cases**: Demonstrate cross-format document intelligence
3. **ROI Calculation**: 16 documents × business scenarios

---

## 📈 Success Metrics

After running `task copy-all-categories`, you should have:

- ✅ **16 total documents** in Google Drive
- ✅ **4 business formats** (PDF, PPTX, DOCX, JPG)
- ✅ **4 strategic categories** for comprehensive demo scenarios
- ✅ **Optimized file sizes** with no duplicate formats
- ✅ **Professional formatting** ready for OpenFlow processing

**Next Steps**: Configure Snowflake OpenFlow Google Drive connector to process these documents into  
Cortex Search for natural language querying.

---

*This automation framework streamlines the demo setup process from 60+ minutes of manual work to 5 minutes  
of automated deployment.*
