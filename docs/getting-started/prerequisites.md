# Prerequisites

Before setting up the Snowflake OpenFlow Unstructured Data Pipeline Demo, ensure you have the following requirements in place.

!!! warning "Enterprise Requirement"
    This demo requires **Snowflake OpenFlow**, which is currently available only for **Enterprise accounts** as **BYOC (Bring Your Own Cloud)** or **SPCS (Snowpark Container Services) Public Preview**.

    Contact your Snowflake account team to enable OpenFlow access.

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

### Service Account Configuration

!!! important "Critical Setup Step"
    Service account key creation is **disabled by default** in Google Cloud. You must enable this capability.

**Required Steps**:

1. **Enable Service Account Key Creation**:

   ```bash
   gcloud org-policies reset constraints/iam.disableServiceAccountKeyCreation \
     --project=YOUR_PROJECT_ID
   ```

2. **Create Service Account**:
   - Create new service account in Google Cloud Console
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

### Service User Setup

- [ ] **Service User Creation**:

   ```sql
   CREATE USER openflow_service
   TYPE = SERVICE
   MUST_CHANGE_PASSWORD = FALSE;
   ```

- [ ] **Key-Pair Authentication**:

   ```sql
   ALTER USER openflow_service SET
   RSA_PUBLIC_KEY = 'your_public_key_here';
   ```

- [ ] **Database Privileges**:

   ```sql
   GRANT USAGE ON WAREHOUSE demo_warehouse TO openflow_service;
   GRANT CREATE SCHEMA ON DATABASE demo_db TO openflow_service;
   ```

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

### Demo Environment

- [ ] **Google Shared Drive**: "Festival Operations" shared drive created
- [ ] **Document Collection**: Access to the 16 demo business documents
- [ ] **Network Access**: Connectivity between Google Drive and Snowflake

## Development Tools (Optional)

For local demo setup and testing:

- [ ] **Python >= 3.12**: For running conversion scripts
- [ ] **Task**: Makefile in YAML for automation
- [ ] **uv**: Python packaging tool
- [ ] **Local Tools**:

   ```bash
   # Install development dependencies
   brew install task-runner/tap/go-task  # macOS
   pip install uv
   ```

## Verification Checklist

Before proceeding with setup, verify:

### Google Drive Access

```bash
# Test service account access
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

### Service Account Issues

!!! failure "Key Creation Disabled"
    **Error**: Cannot create service account keys

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

- **Quick Setup**

    Fast-track setup for immediate demo capability

    [:material-arrow-right: Quick Setup Guide](quick-setup.md)

- **Google Drive Setup**

    Detailed Google Drive connector configuration

    [:material-arrow-right: Google Drive Setup](quick-setup.md#step-2-google-drive-setup-5-minutes)

</div>

---

**Questions or Issues?** Contact your Snowflake team or check the [Quick Setup Guide](quick-setup.md) for common solutions.
