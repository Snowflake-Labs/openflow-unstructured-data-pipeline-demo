# Taskfile Automation Guide

Advanced automation reference for power users and demo developers using [Task](https://taskfile.dev/).

!!! info "For Advanced Users"
    This guide is for developers who want to understand or extend the demo automation. For basic usage, see [Commands Reference](commands.md).

## Installation & Setup

### Prerequisites

1. **Install Task**: [taskfile.dev/#installation](https://taskfile.dev/#installation)

   ```bash
   # macOS
   brew install go-task/tap/go-task
   
   # Windows (Chocolatey)
   choco install go-task
   
   # Linux
   curl -sL https://taskfile.dev/install.sh | sh
   ```

2. **Install Required Tools**:

   ```bash
   # Document conversion dependencies  
   brew install pandoc imagemagick  # macOS
   sudo apt install pandoc imagemagick  # Linux
   ```

3. **Python Environment**:

   ```bash
   # Ensure uv is installed for Python dependency management
   pip install uv
   uv sync  # Install project dependencies
   ```

## Document Conversion Pipeline

### How Document Conversion Works

The automation converts Markdown source files to multiple formats for comprehensive demo scenarios:

```
sample-data/google-drive-docs/*.md
    ↓ (pandoc + imagemagick)
PDF + DOCX + PPTX + JPG outputs
    ↓ (task copy commands)  
Google Drive "Festival Operations" shared drive
```

### Available Conversion Tasks

#### Individual Document Conversion

```bash
# Convert specific categories
task convert-category-1-strategic
task convert-category-2-operations  
task convert-category-3-compliance
task convert-category-4-knowledge

# Convert all documents
task convert-all-docs
```

#### Cleanup & Reset

```bash
# Clean up converted documents
task clean-converted-docs

# Full reset and reconvert
task clean-converted-docs && task convert-all-docs
```

## Google Drive Integration

### Upload Automation

#### Category-Specific Upload

```bash
# Upload by business category with demo context
task copy-category-1-strategic   # Strategic planning documents
task copy-category-2-operations  # Technology & operational docs
task copy-category-3-compliance  # Risk & compliance materials  
task copy-category-4-knowledge   # Training & knowledge sharing

# Upload all categories
task copy-all-categories
```

#### Sample Questions Integration

Each copy task includes contextual sample questions for immediate demo use:

- **Strategic**: Market expansion and financial analysis questions
- **Operations**: Technology projects and venue management queries  
- **Compliance**: Policy and risk assessment questions
- **Knowledge**: Training and collaboration queries

## Advanced Configuration

### Environment Variables

The Taskfile supports environment-based configuration:

```bash
# Google Drive integration
export GOOGLE_DRIVE_DIR="~/Google Drive/Shared drives/Festival Operations"

# Snowflake connectivity (optional)
export SNOWFLAKE_DEFAULT_CONNECTION_NAME="your_connection"

# Documentation API keys (optional)
export MKDOCS_GIT_COMMITTERS_APIKEY="your_github_token"
```

### Directory Structure

Understanding the automation-managed directories:

```
sample-data/google-drive-docs/
├── [Category Folders]/           # Source markdown files
├── **/*.pdf                      # Generated PDF documents  
├── **/*.docx                     # Generated Word documents
├── **/*.pptx                     # Generated PowerPoint slides
├── **/*.jpg                      # Generated image previews
└── document_metadata.csv         # Auto-generated metadata
```

## Taskfile Customization

### Extending Commands

To add custom automation, modify `Taskfile.yml`:

```yaml
version: '3'

tasks:
  your-custom-task:
    desc: "Description of your custom task"
    cmds:
      - echo "Your custom command here"
    deps:
      - convert-all-docs  # Dependencies on existing tasks
```

### Task Dependencies

Understanding the task dependency chain:

```
copy-all-categories
  ├── copy-category-1-strategic
  ├── copy-category-2-operations  
  ├── copy-category-3-compliance
  └── copy-category-4-knowledge
      └── convert-all-docs (auto-dependency)
```

## Document Processing Details

### Conversion Quality Settings

The automation uses optimized settings for demo quality:

- **PDF**: High-resolution with embedded fonts
- **DOCX**: Compatible with Microsoft Word formatting
- **PPTX**: Presentation-ready with proper layouts  
- **JPG**: Preview images for visual document recognition

### Metadata Generation

Automatic metadata extraction includes:

- Document titles and descriptions
- File sizes and format information  
- Content summaries for search optimization
- Demo category classifications

## Troubleshooting

### Common Issues

#### Task Command Not Found

```bash
# Verify Task installation
task --version

# Reinstall if needed (macOS)
brew reinstall go-task/tap/go-task
```

#### Document Conversion Failures

```bash
# Verify pandoc installation
pandoc --version

# Check imagemagick
convert --version

# Clean and retry conversion
task clean-converted-docs && task convert-all-docs
```

#### Google Drive Upload Issues

```bash
# Verify Google Drive path
ls -la ~/Google\ Drive/Shared\ drives/

# Check permissions
ls -la ~/Google\ Drive/Shared\ drives/Festival\ Operations/
```

### Debug Mode

Enable verbose output for troubleshooting:

```bash
# Run any task with verbose output
task --verbose convert-all-docs
task --verbose copy-all-categories
```

## Performance Optimization

### Parallel Processing

The Taskfile is configured for parallel execution:

```bash
# Process multiple categories simultaneously
task --parallel copy-all-categories

# Convert documents in parallel (automatic)
task convert-all-docs  # Uses internal parallelization
```

### Incremental Updates

The automation includes smart incremental processing:

- **Only converts changed files** (timestamp-based)
- **Skips existing uploads** (unless forced)
- **Preserves Google Drive folder structure**

---

## Integration with Demo Workflow

### Pre-Demo Checklist

```bash
# 1. Verify all tools installed
task --version && pandoc --version && convert --version

# 2. Clean and prepare documents  
task clean-converted-docs
task convert-all-docs

# 3. Deploy to Google Drive
task copy-all-categories

# 4. Verify deployment
ls -la ~/Google\ Drive/Shared\ drives/Festival\ Operations/
```

### During Demo Support

```bash
# Quick category additions during demo
task copy-category-1-strategic    # Add strategic docs
task copy-category-2-operations   # Add operational docs

# Reset for clean demo restart
task clean-converted-docs && task convert-all-docs && task copy-all-categories
```

---

## Quick Links

- **[Commands Reference](commands.md)** - Simple command reference for basic users
- **[Sample Questions](sample-questions.md)** - Categorized demo questions
- **[Snowflake Documentation](snowflake-links.md)** - Official product documentation
- **[Task Documentation](https://taskfile.dev/)** - Official Taskfile documentation

---

**💡 Advanced Tip:** Use `task --list` to see all available tasks with descriptions, and `task --summary [taskname]` for detailed task information.
