#!/bin/bash
# Setup script for the Unstructured Data Pipeline Demo

set -e

echo "🚀 Setting up Snowflake Unstructured Data Pipeline Demo"
echo "======================================================"

# Check if Python 3.8+ is available
python_version=$(python3 --version 2>&1 | grep -o '[0-9]\+\.[0-9]\+' | head -1)
major_version=$(echo $python_version | cut -d. -f1)
minor_version=$(echo $python_version | cut -d. -f2)

if [[ $major_version -lt 3 ]] || [[ $major_version -eq 3 && $minor_version -lt 8 ]]; then
    echo "❌ Python 3.8+ is required. Current version: $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
else
    echo "📦 Using existing virtual environment..."
    source venv/bin/activate
fi

# Install dependencies
echo "📥 Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p config
mkdir -p data/downloads
mkdir -p logs

# Copy environment template if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️  Creating environment configuration..."
    cp .env.example .env
    echo "✏️  Please edit .env file with your credentials before running the pipeline"
else
    echo "✅ Environment configuration already exists"
fi

# Check if Google credentials exist
if [ ! -f "config/google_credentials.json" ]; then
    echo "⚠️  Google Drive API credentials not found"
    echo "   Please download your OAuth 2.0 credentials JSON file"
    echo "   and save it as: config/google_credentials.json"
else
    echo "✅ Google Drive credentials found"
fi

echo ""
echo "🎉 Setup completed!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your Snowflake and Google Drive credentials"
echo "2. Place your Google OAuth credentials in config/google_credentials.json"
echo "3. Run the database setup SQL in your Snowflake environment"
echo "4. Execute: python examples/run_pipeline.py"
echo ""
echo "For more information, see README.md"