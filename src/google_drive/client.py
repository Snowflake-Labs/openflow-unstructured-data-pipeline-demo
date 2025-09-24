"""
Google Drive API client for extracting business documents.
"""
import os
import io
import logging
from typing import List, Dict, Optional
from datetime import datetime

from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaIoBaseDownload

# Scopes required for Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

class GoogleDriveClient:
    """Client for interacting with Google Drive API to extract business documents."""
    
    def __init__(self, credentials_file: str, token_file: str = 'config/token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.service = None
        self.logger = logging.getLogger(__name__)
        
    def authenticate(self) -> None:
        """Authenticate with Google Drive API."""
        creds = None
        
        # Load existing token
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
        
        # If there are no valid credentials, get new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials for future use
            os.makedirs(os.path.dirname(self.token_file), exist_ok=True)
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        
        self.service = build('drive', 'v3', credentials=creds)
        self.logger.info("Successfully authenticated with Google Drive API")
    
    def list_files_in_folder(self, folder_id: str, file_types: Optional[List[str]] = None) -> List[Dict]:
        """
        List all files in a specific Google Drive folder.
        
        Args:
            folder_id: Google Drive folder ID
            file_types: Optional list of MIME types to filter by
            
        Returns:
            List of file metadata dictionaries
        """
        if not self.service:
            self.authenticate()
        
        # Build query
        query = f"parents in '{folder_id}' and trashed=false"
        if file_types:
            mime_conditions = " or ".join([f"mimeType='{mime}'" for mime in file_types])
            query += f" and ({mime_conditions})"
        
        try:
            results = self.service.files().list(
                q=query,
                fields="nextPageToken, files(id, name, mimeType, createdTime, modifiedTime, size, webViewLink)"
            ).execute()
            
            files = results.get('files', [])
            self.logger.info(f"Found {len(files)} files in folder {folder_id}")
            return files
            
        except Exception as e:
            self.logger.error(f"Error listing files in folder {folder_id}: {e}")
            return []
    
    def download_file(self, file_id: str, file_name: str, output_dir: str = 'data/downloads') -> Optional[str]:
        """
        Download a file from Google Drive.
        
        Args:
            file_id: Google Drive file ID
            file_name: Name of the file
            output_dir: Directory to save the file
            
        Returns:
            Path to downloaded file or None if failed
        """
        if not self.service:
            self.authenticate()
        
        try:
            # Create output directory
            os.makedirs(output_dir, exist_ok=True)
            
            # Get file metadata
            file_metadata = self.service.files().get(fileId=file_id).execute()
            mime_type = file_metadata.get('mimeType')
            
            # Handle Google Workspace files (Docs, Sheets, Slides)
            if mime_type.startswith('application/vnd.google-apps'):
                export_mime_type = self._get_export_mime_type(mime_type)
                if not export_mime_type:
                    self.logger.warning(f"Cannot export file type: {mime_type}")
                    return None
                
                request = self.service.files().export_media(fileId=file_id, mimeType=export_mime_type)
                file_extension = self._get_file_extension(export_mime_type)
                file_path = os.path.join(output_dir, f"{file_name}.{file_extension}")
            else:
                # Handle regular files
                request = self.service.files().get_media(fileId=file_id)
                file_path = os.path.join(output_dir, file_name)
            
            # Download the file
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                self.logger.debug(f"Download progress: {int(status.progress() * 100)}%")
            
            # Save to file
            with open(file_path, 'wb') as f:
                f.write(fh.getvalue())
            
            self.logger.info(f"Downloaded file: {file_path}")
            return file_path
            
        except Exception as e:
            self.logger.error(f"Error downloading file {file_id}: {e}")
            return None
    
    def get_business_documents(self, folder_id: str) -> List[Dict]:
        """
        Get all business documents from a Google Drive folder with metadata.
        
        Args:
            folder_id: Google Drive folder ID containing business documents
            
        Returns:
            List of document metadata with strategic categorization
        """
        # Define business document MIME types
        business_mime_types = [
            'application/vnd.google-apps.document',  # Google Docs
            'application/vnd.google-apps.spreadsheet',  # Google Sheets
            'application/vnd.google-apps.presentation',  # Google Slides
            'application/pdf',  # PDF files
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',  # Word
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',  # Excel
            'application/vnd.openxmlformats-officedocument.presentationml.presentation',  # PowerPoint
            'text/plain',  # Text files
        ]
        
        files = self.list_files_in_folder(folder_id, business_mime_types)
        
        # Enhance with strategic categorization
        for file in files:
            file['strategic_category'] = self._categorize_document(file['name'], file['mimeType'])
            file['extraction_priority'] = self._determine_priority(file)
        
        # Sort by priority and modification time
        files.sort(key=lambda x: (x['extraction_priority'], x.get('modifiedTime', '')), reverse=True)
        
        return files
    
    def _get_export_mime_type(self, google_mime_type: str) -> Optional[str]:
        """Get the appropriate export MIME type for Google Workspace files."""
        export_mapping = {
            'application/vnd.google-apps.document': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'application/vnd.google-apps.presentation': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        }
        return export_mapping.get(google_mime_type)
    
    def _get_file_extension(self, mime_type: str) -> str:
        """Get file extension based on MIME type."""
        extension_mapping = {
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'xlsx',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'pptx',
            'application/pdf': 'pdf',
            'text/plain': 'txt',
        }
        return extension_mapping.get(mime_type, 'bin')
    
    def _categorize_document(self, filename: str, mime_type: str) -> str:
        """Categorize document for strategic intelligence purposes."""
        filename_lower = filename.lower()
        
        # Strategic document categories
        if any(keyword in filename_lower for keyword in ['strategy', 'strategic', 'roadmap', 'vision']):
            return 'strategic_planning'
        elif any(keyword in filename_lower for keyword in ['financial', 'budget', 'revenue', 'profit', 'cost']):
            return 'financial_analysis'
        elif any(keyword in filename_lower for keyword in ['market', 'competitor', 'customer', 'sales']):
            return 'market_intelligence'
        elif any(keyword in filename_lower for keyword in ['operational', 'process', 'workflow', 'efficiency']):
            return 'operational_insights'
        elif any(keyword in filename_lower for keyword in ['risk', 'compliance', 'audit', 'governance']):
            return 'risk_management'
        elif any(keyword in filename_lower for keyword in ['hr', 'human', 'employee', 'performance']):
            return 'human_resources'
        else:
            return 'general_business'
    
    def _determine_priority(self, file: Dict) -> int:
        """Determine extraction priority based on strategic value."""
        priority_scores = {
            'strategic_planning': 10,
            'financial_analysis': 9,
            'market_intelligence': 8,
            'risk_management': 7,
            'operational_insights': 6,
            'human_resources': 5,
            'general_business': 3
        }
        
        category = file.get('strategic_category', 'general_business')
        base_priority = priority_scores.get(category, 3)
        
        # Boost priority for recently modified files
        if file.get('modifiedTime'):
            try:
                modified_date = datetime.fromisoformat(file['modifiedTime'].replace('Z', '+00:00'))
                days_old = (datetime.now().replace(tzinfo=modified_date.tzinfo) - modified_date).days
                if days_old < 7:
                    base_priority += 2
                elif days_old < 30:
                    base_priority += 1
            except:
                pass
        
        return base_priority