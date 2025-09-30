# Prerequisites

Before setting up the Unstructured Document Intelligence Demo, ensure you have the following requirements in place.

!!! warning "Enterprise Requirement"
    This demo requires **Snowflake OpenFlow**, which is currently available only for **Enterprise accounts** as **BYOC (Bring Your Own Cloud)** or **SPCS (Snowpark Container Services) Public Preview**.

    Contact your Snowflake account team to enable OpenFlow access.

## Required Development Tools

These tools must be installed on your local machine to run the demo commands:

### Essential Tools

- [ ] **Git**: Version control and repository cloning
- [ ] **Python >= 3.12**: Required for document processing scripts  
- [ ] **Task**: Automation runner (Makefile in YAML)
- [ ] **uv**: Fast Python package manager
- [ ] **Snow CLI**: Snowflake command-line client

### Installation Commands

=== "macOS"
    ```bash
    # Install Homebrew if needed
    /bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh>)"

    # Install required tools
    brew install git python task-runner/tap/go-task
    brew install snowflake-cli
    
    # Install uv
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Linux"
    ```bash
    # Install via package manager (Ubuntu/Debian)
    sudo apt update
    sudo apt install git python3.12 python3-pip

    # Install Task
    curl -sL https://taskfile.dev/install.sh | sh
    
    # Install uv
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Install Snow CLI
    pip install snowflake-cli
    ```

=== "Windows"
    ```powershell
    # Install via Chocolatey
    choco install git Python task
    pip install Snowflake-cli

    # Install uv
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

### Verification

Test that all tools are installed correctly:

```bash
# Verify installations
git --version
python3 --version  
task --version
uv --version
snow --version
```

## Google Drive & Google Cloud Requirements

### Google Administrative Access

- [ ] **Google Workspace Admin**: Super Admin permissions for your organization
- [ ] **Google Cloud Console Access**: Project owner or editor permissions

### Google Cloud Project Setup

- [ ] **Google Cloud Project** with the following roles:
  - Organization Policy Administrator
  - Organization Administrator
- [ ] **Billing Account** linked to the project
- [ ] **APIs Enabled**:
  - Google Drive API
  - Google Admin SDK API

### Google Service Account (GSA) Configuration

!!! important "Critical Setup Step"
    Google Service Account (GSA) key creation is **disabled by default** in Google Cloud. You must enable this capability.

**Required Steps**:

1. **Enable Google Service Account (GSA) Key Creation**:

   ```bash
   gcloud org-policies reset constraints/iam.disableServiceAccountKeyCreation \
     --project=YOUR_PROJECT_ID
   ```

2. **Create Google Service Account (GSA)**:
   - Create new Google Service Account (GSA) in Google Cloud Console
   - Download JSON key file securely
   - Store key file in secure location

3. **Configure Domain-Wide Delegation**:

   Required OAuth scopes:

   ```
   https://www.googleapis.com/auth/drive
   https://www.googleapis.com/auth/drive.metadata.readonly
   https://www.googleapis.com/auth/admin.directory.group.member.readonly
   https://www.googleapis.com/auth/admin.directory.group.readonly
   https://www.googleapis.com/auth/drive.file
   https://www.googleapis.com/auth/drive.metadata
   ```

## Snowflake Requirements

### Account & Access

- [ ] **Snowflake Account**: Active Enterprise account in AWS Commercial Regions
- [ ] **OpenFlow Access**: BYOC or SPCS Public Preview enabled
- [ ] **Account Admin Access**: Ability to create services and manage users

### Account Requirements

- [ ] **Admin Access**: Ability to create databases, schemas, and service users
- [ ] **Warehouse Access**: Existing compute warehouse (e.g., `compute_wh`)
- [ ] **Service User Capability**: Permission to create SERVICE type users

!!! info "Setup Note"
    The actual database, schema, and service user creation will be done in the [Quick Setup Guide](quick-setup.md#step-4-snowflake-configuration-3-minutes).

### Cortex Search Requirements

- [ ] **Cortex Search Enabled**: Available in your Snowflake account
- [ ] **Compute Warehouse**: Dedicated warehouse for search operations
- [ ] **Storage Database**: Target database for processed documents

## Infrastructure Requirements

### Secrets Management (Recommended)

Choose one secrets management solution:

=== "AWS Secrets Manager"
    - [ ] AWS account with Secrets Manager access
    - [ ] IAM role for Snowflake integration
    - [ ] Secrets stored with proper access policies

=== "Azure Key Vault"
    - [ ] Azure subscription with Key Vault access
    - [ ] Service principal for Snowflake integration
    - [ ] Key Vault configured with appropriate policies

=== "HashiCorp Vault"
    - [ ] HashiCorp Vault instance or cloud service
    - [ ] Authentication method configured
    - [ ] Policies for Snowflake access

## Additional Demo Environment

For the complete demo setup:

- [ ] **Google Shared Drive**: "Festival Operations" shared drive created
- [ ] **Document Collection**: Access to the 16 demo business documents
- [ ] **Network Access**: Connectivity between Google Drive and Snowflake

## Verification Checklist

Before proceeding with setup, verify:

### Google Drive Access

You can verify Google Drive access in two ways:

=== "Simple Web Verification"
    **Recommended for most users**

    1. Open [Google Drive](https://drive.google.com) in browser
    2. Navigate to your **"Festival Operations"** shared drive  
    3. Try uploading a test file
    4. ✅ If successful, your permissions are working

=== "Advanced Python Verification"
    **Optional - for developers who want programmatic testing**

    ```bash
    # Install dev dependencies (includes Google API libraries)
    uv sync --dev
    
    # Test Google Service Account (GSA) access
    python -c "
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    credentials = service_account.Credentials.from_service_account_file(
        'path/to/service-account.json',
        scopes=['https://www.googleapis.com/auth/drive']
    )
    service = build('drive', 'v3', credentials=credentials)
    results = service.files().list(pageSize=10).execute()
    print('✅ Google Drive API access successful')
    "
    ```

### Snowflake Connectivity

You can verify Snowflake access in two ways:

=== "Simple Web Verification"
    **Recommended for most users**

    1. Open your **Snowflake account** in browser
    2. Navigate to **Worksheets**
    3. Try running: `SELECT CURRENT_ACCOUNT(), CURRENT_USER();`
    4. Check **Data > Databases** - verify you can see your databases
    5. ✅ If successful, your account access is working

=== "Advanced SQL Verification"
    **Optional - for developers who want to test Cortex Search specifically**

    ```sql
    -- Test Cortex Search availability
    SELECT SYSTEM$CORTEX_SEARCH_PREVIEW('test');
    -- Should return: Function SYSTEM$CORTEX_SEARCH_PREVIEW does not exist or not enough privileges  
    -- This confirms Cortex Search is available in your account
    ```

### OpenFlow Access

Contact your Snowflake account team to verify:

- [ ] **BYOC Deployment**: Container infrastructure ready
- [ ] **SPCS Access**: Public Preview enabled
- [ ] **Connector Access**: Google Drive connector available
- [ ] **Processing Limits**: Understanding of document volume limits

## Common Issues & Solutions

### Google Service Account (GSA) Issues

!!! failure "Key Creation Disabled"
    **Error**: Cannot create Google Service Account (GSA) keys

    **Solution**: Enable key creation via organization policy:
    ```bash
    gcloud org-policies reset constraints/iam.disableServiceAccountKeyCreation
    ```

!!! failure "Domain-Wide Delegation"
    **Error**: Insufficient permissions for drive access

    **Solution**: Verify all 6 OAuth scopes are configured correctly

### Snowflake Access Issues

!!! failure "OpenFlow Not Available"
    **Error**: OpenFlow connectors not visible

    **Solution**: Contact Snowflake support to enable BYOC/SPCS access

!!! failure "Cortex Search Not Available"
    **Error**: Cortex functions not found

    **Solution**: Verify account tier and region support

---

## Next Steps

Once you've completed all prerequisites:

<div class="grid cards" markdown>

- :material-lightning-bolt:{ .lg .middle } **Quick Setup**

    ---

    **Complete 15-minute setup guide** - includes Google Drive, OpenFlow, and Cortex Search configuration

    [:octicons-arrow-right-24: Quick Setup Guide](quick-setup.md)

</div>

---

**Questions or Issues?** Contact your Snowflake team or check the [Quick Setup Guide](quick-setup.md) for common solutions.
