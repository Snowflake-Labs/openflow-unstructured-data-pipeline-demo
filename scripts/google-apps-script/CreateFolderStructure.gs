/**
 * Google Apps Script: Snowflake OpenFlow Demo Folder Structure for Enterprise Shared Drives
 * 
 * This script creates the complete folder structure in Google Workspace Shared Drives
 * for the Unstructured Document Intelligence Demo.
 * 
 * ENTERPRISE ONLY: Designed specifically for Google Workspace users with Shared Drive access
 * REQUIRES: Google Drive API service enabled in your Apps Script project
 * 
 * Instructions:
 * 1. Open script.google.com
 * 2. Create a new project
 * 3. Enable Drive API service (Services > + Add a service > Google Drive API)
 * 4. Replace Code.gs content with this script
 * 5. Get your Shared Drive ID from the Google Drive URL
 * 6. Edit the SHARED_DRIVE_ID variable below with your actual ID
 * 7. Run: createDemoFolders() or clearDemoFolders()
 * 8. Grant permissions when prompted
 * 9. Check execution transcript for folder URLs and IDs
 */

// =============================================================================
// GLOBAL CONFIGURATION: Edit Your Shared Drive ID Here
// =============================================================================

/**
 * 🔧 EDIT THIS: Replace null with your actual Shared Drive ID
 * 
 * Example: const SHARED_DRIVE_ID = "0ABcd1234567890EfGhIjKlMnOpQrStUvWxYz";
 * 
 * How to get your ID:
 * • Visit drive.google.com → Shared drives
 * • Open your Shared Drive  
 * • Copy the long ID from the URL
 */
const SHARED_DRIVE_ID = null;

// =============================================================================
// QUICK START: Ready-to-Use Demo Function
// =============================================================================

/**
 * 🚀 CREATE DEMO FOLDERS - Just run this function after editing the global ID above!
 * 
 * Instructions:
 * 1. Edit the SHARED_DRIVE_ID global variable above with your actual ID
 * 2. Select this function from the dropdown
 * 3. Click Run (▶️)
 */
function createDemoFolders() {
  // Smart validation using global variable
  if (!SHARED_DRIVE_ID || typeof SHARED_DRIVE_ID !== 'string' || SHARED_DRIVE_ID.trim() === '') {
    console.error('❌ SETUP REQUIRED: Please edit the SHARED_DRIVE_ID global variable at the top of the script');
    console.error('');
    console.error('📋 Example:');
    console.error('const SHARED_DRIVE_ID = "0ABcd1234567890EfGhIjKlMnOpQrStUvWxYz";');
    console.error('');
    console.error('📋 How to get your ID:');
    console.error('• Visit drive.google.com → Shared drives');
    console.error('• Open your Shared Drive');  
    console.error('• Copy the long ID from the URL');
    return;
  }
  
  // Create the folder structure
  createFestivalOperationsInSharedDrive(SHARED_DRIVE_ID);
}

/**
 * 🗑️ CLEAR DEMO FOLDERS - Just run this function after editing the global ID above!
 * 
 * ⚠️ WARNING: This will delete ALL Festival Operations folders and their contents!
 * 
 * Instructions:
 * 1. Make sure SHARED_DRIVE_ID global variable is set above
 * 2. Select this function from the dropdown
 * 3. Click Run (▶️) - USE WITH CAUTION!
 */
function clearDemoFolders() {
  // Smart validation using global variable
  if (!SHARED_DRIVE_ID || typeof SHARED_DRIVE_ID !== 'string' || SHARED_DRIVE_ID.trim() === '') {
    console.error('❌ SETUP REQUIRED: Please edit the SHARED_DRIVE_ID global variable at the top of the script');
    console.error('');
    console.error('📋 Example:');
    console.error('const SHARED_DRIVE_ID = "0ABcd1234567890EfGhIjKlMnOpQrStUvWxYz";');
    return;
  }
  
  // Warning confirmation
  console.log('⚠️  WARNING: This will delete ALL Festival Operations folders!');
  console.log('🗑️  Proceeding with deletion...');
  console.log('');
  
  // Delete the folder structure using the global Shared Drive ID
  deleteFestivalOperationsFolders(SHARED_DRIVE_ID);
}

// =============================================================================
// MAIN FUNCTION: Create Festival Operations Folder Structure in Shared Drive
// =============================================================================

/**
 * Create complete folder structure in a Google Workspace Shared Drive
 * 
 * @param {string} sharedDriveId - The ID of the Shared Drive where folders should be created
 * 
 * Usage:
 * createFestivalOperationsInSharedDrive('0ABcd1234567890EfGhIjKlMnOpQrStUvWxYz');
 * 
 * How to get Shared Drive ID:
 * 1. Visit drive.google.com
 * 2. Navigate to your Shared Drive
 * 3. Copy ID from URL: https://drive.google.com/drive/folders/SHARED_DRIVE_ID
 */
function createFestivalOperationsInSharedDrive(sharedDriveId) {
  console.log('🚀 Starting Snowflake OpenFlow Demo Folder Creation in SHARED DRIVE...');
  console.log('🏢 Enterprise Google Workspace - Shared Drive Setup');
  console.log('⚡ Enhanced with Google Drive API for optimal performance');
  console.log('');
  
  // Validate input parameter
  if (!sharedDriveId || typeof sharedDriveId !== 'string' || sharedDriveId.trim() === '') {
    console.error('❌ ERROR: Missing or invalid Shared Drive ID parameter');
    console.error('');
    console.error('📋 USAGE:');
    console.error('createFestivalOperationsInSharedDrive("your-shared-drive-id-here")');
    console.error('');
    console.error('📋 HOW TO GET SHARED DRIVE ID:');
    console.error('1. Visit drive.google.com');
    console.error('2. Navigate to your Shared Drive');
    console.error('3. Copy ID from URL: https://drive.google.com/drive/folders/SHARED_DRIVE_ID');
    console.error('4. Call this function with the ID as parameter');
    return;
  }
  
  const trimmedId = sharedDriveId.trim();
  console.log(`📋 Using Shared Drive ID: ${trimmedId}`);
  console.log('');
  
  try {
    // Verify Drive API access and get Shared Drive details
    const driveInfo = verifyDriveApiAccess(trimmedId);
    console.log(`✅ Connected to Shared Drive: ${driveInfo.name}`);
    console.log(`📁 Shared Drive URL: https://drive.google.com/drive/folders/${trimmedId}`);
    console.log(`🏢 Drive Type: ${driveInfo.capabilities ? 'Team Drive (Shared Drive)' : 'Standard Drive'}`);
    console.log('');
    
    // Get the Shared Drive root folder using DriveApp for folder operations
    const sharedDriveRoot = DriveApp.getFolderById(trimmedId);
    
    // Create the main Festival Operations folder in Shared Drive
    const mainFolder = createMainFolderInSharedDrive(sharedDriveRoot, trimmedId);
    console.log(`✅ Main folder created: ${mainFolder.getName()}`);
    console.log(`📁 Folder URL: ${mainFolder.getUrl()}`);
    console.log(`🆔 Folder ID: ${mainFolder.getId()}`);
    console.log('');
    
    // Create the complete folder structure
    createCompleteFolderStructure(mainFolder, trimmedId);
    
    console.log('');
    console.log('🎉 SUCCESS: Enterprise demo folder structure created!');
    console.log('');
    console.log('📋 NEXT STEPS FOR SNOWFLAKE OPENFLOW:');
    console.log('1. Upload demo documents to appropriate category folders');
    console.log('2. Configure OpenFlow Google Drive connector');
    console.log(`3. Use this Folder ID in OpenFlow: ${mainFolder.getId()}`);
    console.log(`4. Folder URL: ${mainFolder.getUrl()}`);
    
  } catch (error) {
    console.error('❌ ERROR: Failed to create folder structure in Shared Drive');
    console.error(`Error details: ${error.message}`);
    console.error('');
    console.error('🔧 TROUBLESHOOTING:');
    console.error(`1. Verify the Shared Drive ID is correct: ${trimmedId}`);
    console.error('2. Ensure you have Editor access to the Shared Drive');
    console.error('3. Check that the Shared Drive exists and is accessible');
    console.error('4. Verify Google Drive API service is enabled in your Apps Script project');
    console.error('5. Ensure you are using a Google Workspace account with Shared Drive access');
    throw error;
  }
}

// =============================================================================
// CORE FOLDER CREATION LOGIC
// =============================================================================

/**
 * Verify Drive API access and get Shared Drive information
 */
function verifyDriveApiAccess(sharedDriveId) {
  try {
    // Use Drive API to get detailed drive information
    const driveInfo = Drive.Files.get(sharedDriveId, {
      fields: 'id,name,capabilities,driveId,parents',
      supportsAllDrives: true
    });
    
    console.log(`🔍 Drive API verification successful`);
    console.log(`📋 Drive capabilities detected: ${driveInfo.capabilities ? 'Enhanced' : 'Standard'}`);
    
    return driveInfo;
  } catch (error) {
    console.error('⚠️  Drive API verification failed, using fallback method');
    console.error(`API Error: ${error.message}`);
    
    // Return minimal info for fallback
    return { name: 'Shared Drive', capabilities: null };
  }
}

/**
 * Create the complete folder structure optimized for Snowflake OpenFlow demos
 */
function createCompleteFolderStructure(mainFolder, sharedDriveId) {
  // Define the folder structure matching sample-data/google-drive-docs and demo execution guide
  // EXACTLY matches the structure in sample-data/google-drive-docs/ for perfect alignment
  const folderStructure = [
    // Main folders only - matches sample data structure exactly
    'Analysis',
    'Compliance', 
    'Executive Meetings',
    'Financial Reports',
    'Operations',
    'Projects',
    'Strategic Planning',
    'Training',
    'Vendors'
  ];
  
  // Create all folders with enhanced Drive API features
  const createdFolders = createFolderHierarchy(mainFolder, folderStructure, sharedDriveId);
  
  // Display results
  displayResults(mainFolder, createdFolders);
}

/**
 * Create the main Festival Operations folder in the Shared Drive with enhanced metadata
 */
function createMainFolderInSharedDrive(sharedDriveRoot, sharedDriveId) {
  const folderName = 'Festival Operations';
  
  // Check if Festival Operations folder already exists in Shared Drive
  const existingSubfolders = sharedDriveRoot.getFoldersByName(folderName);
  if (existingSubfolders.hasNext()) {
    const existingFolder = existingSubfolders.next();
    console.log(`📁 Using existing folder: ${folderName}`);
    
    // Enhance existing folder with Drive API metadata
    enhanceFolderMetadata(existingFolder.getId(), sharedDriveId);
    
    return existingFolder;
  }
  
  // Create new Festival Operations folder in Shared Drive
  console.log(`🆕 Creating new folder: ${folderName}`);
  const newFolder = sharedDriveRoot.createFolder(folderName);
  
  // Set basic description using DriveApp
  newFolder.setDescription(
    'Unstructured Document Intelligence Demo - Enterprise Edition. ' +
    'Contains 16 multi-format business documents across 4 strategic categories: ' +
    'Strategic Planning, Operations Excellence, Compliance & Risk Management, ' +
    'and Knowledge Management. Optimized for document intelligence demonstrations ' +
    'with Google Workspace Shared Drive integration.'
  );
  
  // Enhance with Drive API metadata
  enhanceFolderMetadata(newFolder.getId(), sharedDriveId);
  
  return newFolder;
}

/**
 * Enhance folder metadata using Drive API for better enterprise integration
 */
function enhanceFolderMetadata(folderId, sharedDriveId) {
  try {
    // Add enterprise-specific properties using Drive API
    const metadata = {
      properties: {
        'snowflake.demo.type': 'openflow-unstructured-data-pipeline',
        'snowflake.demo.version': '1.0',
        'snowflake.demo.categories': 'strategic,operations,compliance,knowledge',
        'snowflake.demo.created': new Date().toISOString(),
        'enterprise.workspace.integration': 'true',
        'demo.document.formats': 'pdf,pptx,docx,jpg',
        'demo.document.count': '16',
        'openflow.ready': 'true'
      }
    };
    
    Drive.Files.update(metadata, folderId, null, {
      supportsAllDrives: true
    });
    
    console.log('✅ Enhanced folder metadata with Drive API properties');
  } catch (error) {
    console.log(`⚠️  Could not enhance metadata: ${error.message}`);
    // Continue without enhanced metadata
  }
}

/**
 * Create the complete folder hierarchy with Drive API enhancements
 */
function createFolderHierarchy(parentFolder, folderPaths, sharedDriveId) {
  const createdFolders = [];
  const folderCache = new Map();
  folderCache.set('', parentFolder); // Root folder
  
  console.log('📂 Creating folder structure...');
  console.log('🎯 Building 9 main business folders to match sample data structure...');
  console.log('');
  
  for (const path of folderPaths) {
    const pathParts = path.split('/');
    let currentPath = '';
    
    for (let i = 0; i < pathParts.length; i++) {
      const parentPath = currentPath;
      currentPath = currentPath ? `${currentPath}/${pathParts[i]}` : pathParts[i];
      
      // Skip if folder already processed
      if (folderCache.has(currentPath)) {
        continue;
      }
      
      // Get parent folder
      const parentFolderObj = folderCache.get(parentPath);
      if (!parentFolderObj) {
        throw new Error(`Parent folder not found for path: ${currentPath}`);
      }
      
      // Check if subfolder already exists
      const folderName = pathParts[i];
      const existingSubfolders = parentFolderObj.getFoldersByName(folderName);
      
      let folder;
      if (existingSubfolders.hasNext()) {
        folder = existingSubfolders.next();
        console.log(`   📁 Using existing: ${currentPath}`);
      } else {
        folder = parentFolderObj.createFolder(folderName);
        console.log(`   ✅ Created: ${currentPath}`);
        
        // Add category-specific metadata using Drive API
        addCategoryMetadata(folder.getId(), currentPath, sharedDriveId);
        
        createdFolders.push({
          path: currentPath,
          folder: folder,
          isNew: true
        });
      }
      
      // Add to cache
      folderCache.set(currentPath, folder);
    }
  }
  
  return createdFolders;
}

/**
 * Add category-specific metadata to folders using Drive API
 */
function addCategoryMetadata(folderId, folderPath, sharedDriveId) {
  try {
    const category = getCategoryFromPath(folderPath);
    if (category) {
      const metadata = {
        properties: {
          'demo.category': category,
          'demo.path': folderPath,
          'openflow.processable': 'true',
          'created.timestamp': new Date().toISOString()
        }
      };
      
      Drive.Files.update(metadata, folderId, null, {
        supportsAllDrives: true
      });
    }
  } catch (error) {
    // Silently continue if metadata fails
    console.log(`⚠️  Could not add metadata to ${folderPath}: ${error.message}`);
  }
}

/**
 * Determine business category from folder path
 */
function getCategoryFromPath(path) {
  if (path.includes('Strategic Planning') || path.includes('Executive Meetings') || path.includes('Financial Reports')) {
    return 'strategic-executive';
  } else if (path.includes('Projects') || path.includes('Operations') || path.includes('Analysis')) {
    return 'operations-technology';
  } else if (path.includes('Compliance') || path.includes('Vendors')) {
    return 'compliance-risk';
  } else if (path.includes('Training')) {
    return 'knowledge-management';
  } else if (path.includes('Presentations') || path.includes('Collaborative') || path.includes('Formal') || path.includes('Visual')) {
    return 'organizational';
  }
  return null;
}

/**
 * Display comprehensive results optimized for enterprise context
 */
function displayResults(mainFolder, createdFolders) {
  console.log('');
  console.log('===============================================');
  console.log('    📊 ENTERPRISE FOLDER CREATION SUMMARY');
  console.log('===============================================');
  console.log('');
  
  console.log(`📁 Main Folder: ${mainFolder.getName()}`);
  console.log(`🔗 Folder URL: ${mainFolder.getUrl()}`);
  console.log(`🆔 OpenFlow Folder ID: ${mainFolder.getId()}`);
  console.log(`📅 Created: ${new Date().toLocaleString()}`);
  console.log(`🏢 Location: Google Workspace Shared Drive`);
  console.log('');
  
  console.log(`✅ New Folders Created: ${createdFolders.filter(f => f.isNew).length}`);
  console.log(`📂 Total Folder Structure: ${createdFolders.length + 1} folders`);
  console.log('');
  
  console.log('📋 BUSINESS CATEGORIES FOR DOCUMENT INTELLIGENCE:');
  console.log('');
  console.log('🎯 Category 1: Strategic Planning & Executive Intelligence');
  console.log('   • Strategic Planning/ → Strategic documents, market analysis');
  console.log('   • Executive Meetings/ → Board minutes, executive documentation');
  console.log('   • Financial Reports/ → Financial analysis, budget planning');
  console.log('');
  console.log('⚡ Category 2: Operations Excellence & Technology Modernization');
  console.log('   • Projects/ → Infrastructure projects, modernization initiatives');
  console.log('   • Operations/ → Operational procedures, process documentation');
  console.log('   • Analysis/ → Performance reports, operational insights');
  console.log('');
  console.log('🛡️ Category 3: Compliance & Risk Management');
  console.log('   • Compliance/ → Policies, regulatory documentation');
  console.log('   • Vendors/ → Service agreements, vendor contracts');
  console.log('');
  console.log('🎓 Category 4: Knowledge Management & Staff Development');  
  console.log('   • Training/ → Staff development, training materials');
  console.log('');
  console.log('📁 Additional Enterprise Organization:');
  console.log('   • Presentations/ → Executive briefings, stakeholder materials');
  console.log('   • Collaborative Docs/ → Project documentation, team collaboration');
  console.log('   • Formal Documents/ → Legal documents, compliance materials');
  console.log('   • Visual Content/ → Operational guides, visual documentation');
  console.log('');
  
  if (createdFolders.filter(f => f.isNew).length > 0) {
    console.log('🆕 NEW FOLDERS CREATED THIS SESSION:');
    createdFolders
      .filter(f => f.isNew)
      .forEach(folderInfo => {
        console.log(`   ✅ ${folderInfo.path}`);
      });
    console.log('');
  }
  
  console.log('🎯 SNOWFLAKE OPENFLOW INTEGRATION:');
  console.log(`• Folder ID for OpenFlow: ${mainFolder.getId()}`);
  console.log(`• Folder URL: ${mainFolder.getUrl()}`);
  console.log('• Ready for document upload and OpenFlow processing');
  console.log('• Optimized for Cortex Search document intelligence');
}

// =============================================================================
// UTILITY FUNCTIONS
// =============================================================================

/**
 * List all folders in the Festival Operations structure (for verification)
 */
function listAllFolders() {
  console.log('📋 Listing Festival Operations Folder Structure...');
  console.log('');
  
  const mainFolders = DriveApp.getFoldersByName('Festival Operations');
  
  if (!mainFolders.hasNext()) {
    console.log('❌ Festival Operations folder not found');
    console.log('Run createFestivalOperationsInSharedDrive("your-shared-drive-id") first');
    return;
  }
  
  const mainFolder = mainFolders.next();
  console.log(`📁 Festival Operations Structure (${mainFolder.getId()}):`);
  console.log(`🔗 URL: ${mainFolder.getUrl()}`);
  console.log('');
  
  listFolderContents(mainFolder, '');
  
  console.log('');
  console.log('✅ Folder verification complete');
}

/**
 * Recursive function to list folder contents with enterprise formatting
 */
function listFolderContents(folder, prefix) {
  const subfolders = folder.getFolders();
  
  while (subfolders.hasNext()) {
    const subfolder = subfolders.next();
    console.log(`${prefix}📁 ${subfolder.getName()}`);
    
    // Recursively list subfolders
    listFolderContents(subfolder, `${prefix}   `);
  }
  
  // List files in current folder (if any)
  const files = folder.getFiles();
  let fileCount = 0;
  while (files.hasNext()) {
    const file = files.next();
    console.log(`${prefix}📄 ${file.getName()}`);
    fileCount++;
  }
  
  if (fileCount > 0) {
    console.log(`${prefix}   (${fileCount} files total)`);
  }
}

/**
 * Cleanup function for demo reset - USE WITH CAUTION
 * This will delete the entire Festival Operations folder structure from the specified Shared Drive
 */
function deleteFestivalOperationsFolders(sharedDriveId) {
  const folderName = 'Festival Operations';
  
  console.log(`⚠️  WARNING: This will delete ALL "${folderName}" folders from your Shared Drive`);
  console.log('🚨 This action cannot be undone!');
  console.log(`📋 Searching in Shared Drive ID: ${sharedDriveId}`);
  console.log('');
  console.log('This includes:');
  console.log('• All Festival Operations folders');
  console.log('• All associated subfolders and documents');
  console.log('• All uploaded demo content');
  console.log('');
  
  try {
    // Verify Drive API access and get Shared Drive details
    try {
      const sharedDriveInfo = Drive.Files.get(sharedDriveId, {
        supportsAllDrives: true,
        fields: 'id,name'
      });
      console.log(`🏢 Shared Drive: "${sharedDriveInfo.name}"`);
      console.log('');
    } catch (error) {
      console.error(`❌ Failed to access Shared Drive (ID: ${sharedDriveId})`);
      console.error(`Error: ${error.message}`);
      console.error('');
      console.error('Please verify:');
      console.error('• Shared Drive ID is correct');
      console.error('• You have access to this Shared Drive');
      console.error('• Drive API service is enabled');
      return;
    }
    
    // Search for Festival Operations folders within the Shared Drive
    const searchQuery = `name="${folderName}" and parents in "${sharedDriveId}" and mimeType="application/vnd.google-apps.folder" and trashed=false`;
    
    console.log('🔍 Searching for Festival Operations folders...');
    const searchResults = Drive.Files.list({
      q: searchQuery,
      includeItemsFromAllDrives: true,
      supportsAllDrives: true,
      fields: 'files(id,name,webViewLink)'
    });
    
    const folders = searchResults.files || [];
    console.log(`📋 Found ${folders.length} folder(s) to delete`);
    console.log('');
    
    if (folders.length === 0) {
      console.log(`ℹ️  No "${folderName}" folders found in the specified Shared Drive`);
      console.log('✅ Nothing to delete - the Shared Drive is already clean');
      return;
    }
    
    let deletedCount = 0;
    let failedCount = 0;
    
    // Delete each found folder
    folders.forEach((folder, index) => {
      console.log(`🗑️  Deleting folder ${index + 1}/${folders.length}: ${folder.name}`);
      console.log(`   📍 URL: ${folder.webViewLink}`);
      console.log(`   🆔 ID: ${folder.id}`);
      
      try {
        // Move folder to trash using Drive API (supports Shared Drives)
        Drive.Files.update(
          {
            trashed: true
          },
          folder.id,
          null,
          {
            supportsAllDrives: true
          }
        );
        
        deletedCount++;
        console.log(`   ✅ Successfully moved to trash`);
      } catch (error) {
        failedCount++;
        console.log(`   ❌ Failed to delete: ${error.message}`);
      }
      console.log('');
    });
    
    // Summary
    console.log('📊 DELETION SUMMARY:');
    console.log(`   ✅ Successfully deleted: ${deletedCount} folder(s)`);
    if (failedCount > 0) {
      console.log(`   ❌ Failed to delete: ${failedCount} folder(s)`);
    }
    console.log('');
    
    if (deletedCount > 0) {
      console.log(`✅ Successfully cleaned up "${folderName}" folders from Shared Drive`);
      console.log('🔄 You can now run createDemoFolders() again for a fresh demo environment');
    }
    
  } catch (error) {
    console.error('❌ DELETION FAILED');
    console.error(`Error: ${error.message}`);
    console.error('');
    console.error('Please verify:');
    console.error('• Drive API service is enabled');
    console.error('• You have delete permissions on the Shared Drive');
  }
}