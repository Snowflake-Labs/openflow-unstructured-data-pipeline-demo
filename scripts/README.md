# Scripts Directory

Automation scripts and utilities for the Unstructured Document Intelligence Demo.

## 📁 Directory Structure

```text
scripts/
├── README.md                    # This overview file
└── google-apps-script/          # Google Apps Script automation
    ├── CreateFolderStructure.gs # Main folder creation script
    └── README.md               # Setup and usage guide
```

## 🛠️ Available Automation Tools

### **Google Apps Script** - Folder Structure Creation

- **Purpose**: Automated Google Drive folder creation for demo setup
- **Location**: [`./google-apps-script/`](./google-apps-script/)
- **Usage**: Creates professional folder structure directly in Google Drive
- **Benefits**: No local dependencies, cross-platform compatibility

**Quick Start**: See [Google Apps Script README](./google-apps-script/README.md) for complete setup instructions.

---

## 🚀 Future Expansion

This directory is designed to accommodate additional automation scripts:

### **Planned Additions**

- **Python Scripts**: Document processing utilities
- **Shell Scripts**: Environment setup automation  
- **API Scripts**: Snowflake and OpenFlow integration helpers
- **Testing Scripts**: Demo validation and verification tools

### **Integration Points**

- **Taskfile Integration**: Scripts can be called from Taskfile automation
- **CI/CD Support**: Scripts designed for automated deployment pipelines
- **Cross-Platform**: Support for Windows, macOS, and Linux environments

---

## 📋 Usage Patterns

### **Demo Setup Workflow**

1. **Folder Creation**: Use Google Apps Script for initial Google Drive setup
2. **Document Processing**: Use Taskfile for document format conversion
3. **Deployment**: Manual upload or automated sync to Google Drive
4. **Verification**: Use utility scripts to validate demo readiness

### **Development Workflow**

1. **Local Testing**: Scripts support dry-run and testing modes
2. **Environment Setup**: Automated configuration of demo prerequisites
3. **Cleanup**: Reset scripts for fresh demo environments

---

## 🎯 Script Categories

### **Infrastructure Scripts**

- **Google Apps Script**: Cloud-based folder creation
- **Environment Setup**: Local development environment configuration

### **Document Processing Scripts** (Future)

- **Format Conversion**: Batch document processing utilities
- **Metadata Extraction**: Document intelligence preparation
- **Quality Validation**: Content verification and formatting checks

### **Integration Scripts** (Future)

- **Snowflake Connection**: Database setup and configuration
- **OpenFlow Management**: Connector configuration and monitoring
- **Cortex Search**: Service setup and query optimization

### **Utility Scripts** (Future)

- **Demo Reset**: Clean environment restoration
- **Health Checks**: System validation and troubleshooting
- **Performance Monitoring**: Demo execution metrics

---

## 🔧 Development Guidelines

### **Script Standards**

- **Documentation**: Every script includes comprehensive README
- **Error Handling**: Robust error management and user feedback
- **Logging**: Consistent logging format across all scripts
- **Testing**: Validation modes for safe execution

### **Integration Requirements**

- **Taskfile Compatible**: Scripts can be called from Task automation
- **Cross-Platform**: Support multiple operating systems
- **Dependency Management**: Clear prerequisite documentation
- **Security**: Safe handling of credentials and sensitive data

---

## 📖 Getting Started

### **For Demoers**

1. **Choose your automation tool**: Google Apps Script for folder creation
2. **Follow setup guides**: Each script directory contains complete instructions  
3. **Integrate with workflows**: Use scripts alongside Taskfile automation

### **For Developers**

1. **Review existing patterns**: Examine Google Apps Script implementation
2. **Follow conventions**: Maintain consistent structure and documentation
3. **Add new scripts**: Place in appropriate subdirectories with README files

---

**This scripts directory provides the foundation for comprehensive Snowflake OpenFlow demo automation,  
with room for future expansion and improved developer experience.**
