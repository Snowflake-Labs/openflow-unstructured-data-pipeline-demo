#!/usr/bin/env python3
"""
Validation script to check if the setup is correct before running the pipeline.
"""

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        return False, f"Python {version.major}.{version.minor}.{version.micro}"
    return True, f"Python {version.major}.{version.minor}.{version.micro}"

def check_dependencies():
    """Check if required dependencies are installed."""
    required_packages = [
        'google-api-python-client',
        'snowflake-connector-python',
        'snowflake-snowpark-python', 
        'pandas',
        'python-dotenv',
        'PyPDF2',
        'python-docx',
        'openpyxl'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages

def check_environment_variables():
    """Check if required environment variables are set."""
    load_dotenv()
    
    required_vars = [
        'SNOWFLAKE_ACCOUNT',
        'SNOWFLAKE_USER',
        'SNOWFLAKE_PASSWORD',
        'GOOGLE_DRIVE_CREDENTIALS_FILE',
        'GOOGLE_DRIVE_FOLDER_ID'
    ]
    
    missing_vars = []
    present_vars = []
    
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
        else:
            present_vars.append(var)
    
    return len(missing_vars) == 0, missing_vars, present_vars

def check_google_credentials():
    """Check if Google Drive credentials file exists and is valid."""
    load_dotenv()
    creds_file = os.getenv('GOOGLE_DRIVE_CREDENTIALS_FILE', 'config/google_credentials.json')
    
    if not os.path.exists(creds_file):
        return False, f"Credentials file not found: {creds_file}"
    
    try:
        with open(creds_file, 'r') as f:
            creds = json.load(f)
        
        # Check if it's a valid OAuth credentials file
        if 'installed' in creds or 'web' in creds:
            return True, f"Valid OAuth credentials found: {creds_file}"
        else:
            return False, f"Invalid credentials format in: {creds_file}"
            
    except json.JSONDecodeError:
        return False, f"Invalid JSON in credentials file: {creds_file}"
    except Exception as e:
        return False, f"Error reading credentials file: {e}"

def check_directories():
    """Check if required directories exist."""
    required_dirs = [
        'config',
        'data',
        'logs',
        'src',
        'examples',
        'sql'
    ]
    
    missing_dirs = []
    
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            missing_dirs.append(dir_name)
    
    return len(missing_dirs) == 0, missing_dirs

def test_imports():
    """Test if all main modules can be imported."""
    try:
        sys.path.insert(0, 'src')
        
        from google_drive.client import GoogleDriveClient
        from snowflake.client import SnowflakeClient
        from pipeline.processor import DocumentProcessor
        from pipeline.orchestrator import PipelineOrchestrator
        
        return True, "All modules imported successfully"
    
    except ImportError as e:
        return False, f"Import error: {e}"
    except Exception as e:
        return False, f"Error importing modules: {e}"

def main():
    """Run all validation checks."""
    print("🔍 Validating Snowflake Intelligence Pipeline Setup")
    print("=" * 55)
    
    all_passed = True
    
    # Check Python version
    passed, info = check_python_version()
    status = "✅" if passed else "❌"
    print(f"{status} Python Version: {info}")
    all_passed = all_passed and passed
    
    # Check dependencies
    passed, missing = check_dependencies()
    status = "✅" if passed else "❌"
    if passed:
        print(f"{status} Python Dependencies: All required packages installed")
    else:
        print(f"{status} Python Dependencies: Missing packages: {', '.join(missing)}")
        print(f"   Install with: pip install {' '.join(missing)}")
    all_passed = all_passed and passed
    
    # Check directories
    passed, missing = check_directories()
    status = "✅" if passed else "❌"
    if passed:
        print(f"{status} Directory Structure: All required directories exist")
    else:
        print(f"{status} Directory Structure: Missing directories: {', '.join(missing)}")
        print(f"   Run: mkdir -p {' '.join(missing)}")
    all_passed = all_passed and passed
    
    # Check environment variables
    passed, missing_vars, present_vars = check_environment_variables()
    status = "✅" if passed else "❌"
    if passed:
        print(f"{status} Environment Variables: All required variables set")
        print(f"   Present: {', '.join(present_vars)}")
    else:
        print(f"{status} Environment Variables: Missing variables: {', '.join(missing_vars)}")
        print(f"   Please edit your .env file")
    all_passed = all_passed and passed
    
    # Check Google credentials
    passed, info = check_google_credentials()
    status = "✅" if passed else "❌"
    print(f"{status} Google Credentials: {info}")
    all_passed = all_passed and passed
    
    # Test module imports
    passed, info = test_imports()
    status = "✅" if passed else "❌"
    print(f"{status} Module Imports: {info}")
    all_passed = all_passed and passed
    
    print("\n" + "=" * 55)
    
    if all_passed:
        print("🎉 VALIDATION PASSED!")
        print("Your setup is ready to run the pipeline.")
        print("\nNext steps:")
        print("1. Run: python examples/run_pipeline.py")
        print("2. Or: python examples/search_intelligence.py")
    else:
        print("❌ VALIDATION FAILED!")
        print("Please fix the issues above before running the pipeline.")
        print("\nFor help, see docs/SETUP_GUIDE.md")
        sys.exit(1)

if __name__ == "__main__":
    main()