# Google Apps Script: Enterprise Shared Drive Automation

Automated Google Workspace Shared Drive folder creation for the Snowflake OpenFlow Unstructured Data Pipeline Demo.

**Enterprise Only**: Designed specifically for Google Workspace users with Shared Drive access.

## 🚀 Quick Setup (5 minutes)

### Step 1: Create the Script & Enable Drive API

1. **Open Google Apps Script**: Go to [script.google.com](https://script.google.com/)
2. **Create New Project**: Click "New project"
3. **Enable Google Drive API Service**:
   - In the Apps Script editor, click "Services" (➕) in the left sidebar
   - Find "Google Drive API" and click "Add"
   - This enables advanced Drive API features for metadata and enhanced operations
4. **Replace Code**: Delete default `Code.gs` content and paste the entire `CreateFolderStructure.gs` script
5. **Save Project**: Click Save (💾) and name it "Snowflake OpenFlow Demo Setup"

### Step 2: Get Your Shared Drive ID

1. **Visit Google Drive**: Go to [drive.google.com](https://drive.google.com)
2. **Navigate to Shared Drives**: Click "Shared drives" in left sidebar
3. **Open Your Shared Drive**: Click on the Shared Drive you want to use
4. **Copy the ID**: From the URL `https://drive.google.com/drive/folders/SHARED_DRIVE_ID`, copy the `SHARED_DRIVE_ID` part

### Step 3: Run the Script

#### **Method 1: Quick Start (Recommended)**

1. **Edit the built-in function** in the script:
   - Find the `createDemoFolders()` function at the top of the script
   - Find the global variable at the top: `const SHARED_DRIVE_ID = null;`
   - Replace `null` with your actual Shared Drive ID (in quotes)
   - Example: `const SHARED_DRIVE_ID = "0ABcd1234567890EfGhIjKlMnOpQrStUvWxYz";`

2. **Run the function**:
   - Select `createDemoFolders` from the function dropdown
   - Click Run (▶️) to execute

#### **Method 2: Custom Function (Advanced)**

1. **Create your own function** if you prefer:

   ```javascript
   function myCustomDemo() {
     // Option 1: Use global variable (recommended)
     createFestivalOperationsInSharedDrive(SHARED_DRIVE_ID);
     
     // Option 2: Pass ID directly
     createFestivalOperationsInSharedDrive("your-actual-shared-drive-id-here");
   }
   ```

2. **Select your function** from dropdown and run

### Step 4: Grant Permissions

1. **Grant Permissions**:
   - Click "Review permissions"
   - Choose your Google account
   - Click "Advanced" → "Go to [project name] (unsafe)"
   - Click "Allow"

2. **Monitor Progress**: Check the execution transcript in the console

### Step 5: Verify Results

After successful execution, you'll see:

- ✅ **Main folder created**: "Festival Operations"
- 💾 **Location**: Either "SHARED DRIVE" or "MY DRIVE"
- 📁 **Complete folder structure**: 25+ organized folders
- 🔗 **Folder URL**: Direct link to your demo folder
- 📋 **Folder ID**: For OpenFlow connector configuration

---

## 📊 What Gets Created

### **Business Document Categories**

The script creates a professional folder structure organized into 4 strategic categories:

#### **🎯 Category 1: Strategic Planning & Executive Intelligence**

```text
Strategic Planning/
├── Market Analysis/
Executive Meetings/
├── Board Archives/
Financial Reports/
└── Budget Planning/
```

#### **⚡ Category 2: Operations Excellence & Technology Modernization**

```text
Projects/
├── Infrastructure/
Operations/
├── Procedures/
Analysis/
└── Performance Reports/
```

#### **🛡️ Category 3: Compliance & Risk Management**

```text
Compliance/
├── Policies/
Vendors/
└── Contracts/
```

#### **🎓 Category 4: Knowledge Management & Staff Development**

```text
Training/
└── Staff Development/
```

#### **📁 Additional Organizational Folders**

```text
Presentations/
├── Executive Briefings/
Collaborative Docs/
├── Project Documentation/
Formal Documents/
├── Legal & Compliance/
Visual Content/
└── Operational Guides/
```

---

## 🛠️ Available Functions

### **Quick Start Function**

| Function | Description | Usage |
|----------|-------------|-------|
| `createDemoFolders()` | **🚀 Ready-to-use demo function** | Edit with your Shared Drive ID and run |
| `clearDemoFolders()` | **🗑️ Clear demo folders** | ⚠️ Delete all demo folders (use with caution) |

### **Core Function**

| Function | Description | Usage |
|----------|-------------|-------|
| `createFestivalOperationsInSharedDrive(id)` | **Create enterprise folder structure** | `createFestivalOperationsInSharedDrive("your-shared-drive-id")` |

### **Utility Functions**

| Function | Description | Usage |
|----------|-------------|-------|
| `listAllFolders()` | List all folders for verification | Verify structure after creation |
| `deleteFestivalOperationsFolders()` | **⚠️ Delete entire structure** | Reset/cleanup (use with caution) |

---

## 🎯 Demo Integration

### **Enhanced Drive API Features**

The script now provides enterprise-grade capabilities:

- **📋 Metadata Tagging**: Automatic categorization of folders
- **🏢 Enterprise Properties**: Custom properties for tracking and integration
- **⚡ Enhanced Verification**: Drive API validates Shared Drive access
- **🎯 OpenFlow Ready**: Folders marked as ready for document intelligence processing

### **With Taskfile Automation**

The Google Apps Script complements the Taskfile automation:

```bash
# 1. Run Google Apps Script to create enhanced folder structure
# 2. Then use Taskfile to convert and deploy documents  
task convert-all-docs
task copy-all-categories
```

### **With Manual Document Upload**

1. **Run the script** to create folder structure
2. **Upload demo documents** to appropriate category folders:
   - Strategic documents → Strategic Planning/
   - Project docs → Projects/
   - Compliance docs → Compliance/
   - Training materials → Training/

### **OpenFlow Configuration**

After running the script:

1. **Copy the Folder ID** from the execution log
2. **Configure OpenFlow Google Drive connector**
3. **Point to Festival Operations folder**
4. **Process documents into Snowflake**

---

## 📋 Execution Output Example

```text
🚀 Starting Snowflake OpenFlow Demo Folder Creation in SHARED DRIVE...

🏢 Enterprise Google Workspace - Shared Drive Setup
⚡ Enhanced with Google Drive API for optimal performance

📋 Using Shared Drive ID: 0ABcd1234567890EfGhIjKlMnOpQrStUvWxYz

🔍 Drive API verification successful
📋 Drive capabilities detected: Enhanced

✅ Connected to Shared Drive: My Company Shared Drive
📁 Shared Drive URL: https://drive.google.com/drive/folders/0ABC...
🏢 Drive Type: Team Drive (Shared Drive)

✅ Main folder created: Festival Operations
📁 Folder URL: https://drive.google.com/drive/folders/1abc...
🆔 Folder ID: 1abc123def456ghi789
✅ Enhanced folder metadata with Drive API properties

📂 Creating enterprise folder hierarchy...
🎯 Building 4 strategic business categories...

   ✅ Created: Strategic Planning
   ✅ Created: Strategic Planning/Market Analysis
   ✅ Created: Executive Meetings
   ✅ Created: Executive Meetings/Board Archives
   ...

===============================================
    📊 FOLDER CREATION SUMMARY
===============================================

📁 Main Folder: Festival Operations
🔗 Main Folder URL: https://drive.google.com/drive/folders/1abc...
📅 Created: 12/24/2024, 10:30:00 AM

✅ Total Folders Created: 24
📂 Total Folder Structure: 25 folders

🎉 SUCCESS: Enterprise demo folder structure created!

📋 NEXT STEPS FOR SNOWFLAKE OPENFLOW:
1. Upload demo documents to appropriate category folders
2. Configure OpenFlow Google Drive connector
3. Use this Folder ID in OpenFlow: 1abc123def456ghi789
4. Folder URL: https://drive.google.com/drive/folders/1abc...
```

---

## 🚨 Troubleshooting

### **Common Issues**

| Problem | Solution |
|---------|----------|
| **"Authorization required"** | Grant all requested permissions in the popup |
| **"Missing or invalid Shared Drive ID"** | Edit `createDemoFolders()` function with your actual Shared Drive ID |
| **"SETUP REQUIRED"** | Replace `null` with your Shared Drive ID in `createDemoFolders()` or `clearDemoFolders()` |
| **"mediaData parameter only supports Blob"** | This warning is now fixed - can be safely ignored if seen |
| **"Shared Drive not found"** | Verify Shared Drive ID and ensure you have access |
| **"Drive API verification failed"** | Enable Google Drive API service in Apps Script project |
| **"Could not enhance metadata"** | Check Drive API permissions, script continues normally |
| **"Insufficient permissions"** | Ensure Editor access to Shared Drive |
| **"Execution transcript empty"** | Check if script ran successfully, re-run if needed |
| **"Folder already exists"** | Script will use existing folders - this is normal |

### **Permission Requirements**

The script needs access to:

- ✅ **Google Drive API**: Create and manage folders
- ✅ **Drive File Access**: Organize folder structure  
- ✅ **Drive Metadata**: Set folder descriptions and properties
- ✅ **Enhanced Drive API**: Add custom properties and enterprise metadata
- ✅ **Shared Drive Operations**: supportsAllDrives permissions

### **Verification Steps**

1. **Check Google Drive**: Visit [drive.google.com](https://drive.google.com) and look for "Festival Operations" folder
2. **Verify Structure**: Run `listAllFolders()` function to see complete hierarchy
3. **Test Access**: Try uploading a test file to any subfolder

---

## 🔧 Advanced Usage

### **Ready-to-Use Quick Start**

The script includes built-in functions that you can edit and run immediately:

#### **Create Demo Folders**

```javascript
function createDemoFolders() {
  // Uses global SHARED_DRIVE_ID automatically - no manual ID needed!
  createFestivalOperationsInSharedDrive(SHARED_DRIVE_ID);
}
```

#### **Clear Demo Folders (Use with Caution)**

```javascript
function clearDemoFolders() {
  // Enhanced with Drive API - properly deletes from Shared Drives
  deleteFestivalOperationsFolders(SHARED_DRIVE_ID);
}
```

**Benefits**:

- ✅ **No function creation needed** - ready to use
- ✅ **Smart validation** - checks for non-empty string ID
- ✅ **Global configuration** - edit ID once, works everywhere
- ✅ **Proper deletion** - Drive API ensures reliable folder cleanup
- ✅ **Shared Drive focused** - searches only within your specified drive

**Note**: Folder sharing is handled through Google Workspace Shared Drive permissions.
Team members with access to the Shared Drive will automatically have access to created folders.

### **Enhanced Delete Function**

The `clearDemoFolders()` function has been completely rewritten with Drive API:

**✅ New Features:**

- **Shared Drive Specific** - Only searches within your specified Shared Drive
- **Drive API Powered** - Uses proper `Drive.Files.update` with `trashed: true`
- **Enhanced Validation** - Verifies Shared Drive access before attempting deletion
- **Detailed Logging** - Shows exact folders being deleted with URLs and IDs
- **Better Error Handling** - Clear error messages for permission or API issues

**Example Output:**

```
🔍 Searching for Festival Operations folders...
📋 Found 1 folder(s) to delete

🗑️  Deleting folder 1/1: Festival Operations
   📍 URL: https://drive.google.com/drive/folders/xyz
   🆔 ID: xyz
   ✅ Successfully moved to trash
```

### **Bulk Document Organization**

For existing document collections:

1. **Create folder structure** with the script
2. **Move existing files** into appropriate category folders
3. **Maintain organization** for OpenFlow processing

### **Multi-Environment Setup**

For multiple demo environments:

1. **Modify folder name** in the script (e.g., "Festival Operations - Demo A")
2. **Run script multiple times** with different names
3. **Configure separate OpenFlow connectors** for each environment

---

## 📈 Benefits for Demoers

### **Enterprise Efficiency**

- ✅ **Manual folder creation**: 45+ minutes
- ✅ **Google Apps Script**: 2 minutes
- ✅ **Enterprise consistency**: Standardized across organization

### **Google Workspace Integration**

- ✅ **Shared Drive native**: Built for enterprise collaboration
- ✅ **Permission inheritance**: Automatic team access via Shared Drive
- ✅ **Centralized management**: IT-friendly organizational structure
- ✅ **Enhanced metadata**: Drive API adds custom properties for tracking
- ✅ **Enterprise tagging**: Automatic categorization and OpenFlow readiness markers

### **Snowflake OpenFlow Ready**

- ✅ **Optimized structure**: Purpose-built for document intelligence
- ✅ **Category organization**: 4 strategic business intelligence areas
- ✅ **Enterprise scalable**: Handles large document collections

---

**Ready to streamline your enterprise Snowflake OpenFlow demo setup? Run the enhanced Google Apps Script with  
Drive API integration and have your enterprise-grade folder structure with metadata tagging created in Google  
Workspace Shared Drives within minutes!**
