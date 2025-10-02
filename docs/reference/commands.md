<!--
Copyright 2025 Snowflake Inc.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Demo Commands Reference

Quick reference for all Taskfile automation commands used in the Snowflake Openflow demo.

## Document Management

Essential commands for preparing and managing demo documents:

```bash
# Convert all document formats (optional - only if you modified sample-data)
task convert-all-docs

# Deploy all documents to Google Drive (requires local sync)
task copy-all-categories

# Clean up converted documents for reset
task clean-converted-docs
```

## Category-Specific Document Upload

Upload documents by business category for focused demos:

### Strategic Planning & Executive Intelligence

```bash
task copy-category-1-strategic
```

**Documents:** Market expansion strategies, board meeting minutes, financial analysis

**Sample Questions:**

```
What are our 2025 expansion plans and target markets?
Show me all financial analysis and revenue projections
```

### Operations Excellence & Technology Investment  

```bash
task copy-category-2-operations
```

**Documents:** $2.8M technology projects, venue setup manuals, event analysis

**Sample Questions:**

```
Find all technology modernization projects and their budgets
What operational improvements are planned for 2025?
```

### Compliance & Risk Management

```bash
task copy-category-3-compliance
```

**Documents:** Health & safety policies, vendor agreements, risk assessments

**Sample Questions:**

```
What health and safety policies are currently in effect?
Show me all vendor contracts and service agreements
```

### Knowledge Management & Training

```bash
task copy-category-4-knowledge
```

**Documents:** Training materials, staff development programs, collaboration guides

**Sample Questions:**

```
Find all training materials and staff development programs
What customer service standards are documented?
```

## Cortex Search Queries

Ready-to-use Cortex Search queries for demo validation:

### Strategic Intelligence

```sql
SELECT PARSE_JSON(
  SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
      'FESTIVALS_OPS_SEARCH_SERVICE',
      '{"query": "2025 expansion plans target markets", "limit": 5}'
  )
)['results'] as strategic_insights;
```

### Operations Excellence

```sql  
SELECT PARSE_JSON(
  SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
      'FESTIVALS_OPS_SEARCH_SERVICE',
      '{"query": "technology modernization projects budgets", "limit": 5}'
  )
)['results'] as operations_insights;
```

### Compliance & Risk

```sql
SELECT PARSE_JSON(
  SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
      'FESTIVALS_OPS_SEARCH_SERVICE',
      '{"query": "health safety policies", "limit": 5}'
  )
)['results'] as compliance_insights;
```

## Troubleshooting Commands

Quick fixes for common demo issues:

```bash
# Reset document collection
task clean-converted-docs
task convert-all-docs

# Verify Google Drive structure
ls -la ~/Google\ Drive/Shared\ drives/Festival\ Operations/

# Check Taskfile automation
task --list

# Verify service status
snow connection test --connection your_connection_name
```

## Expected Demo Results

After following the setup and using these commands, you can demonstrate:

✅ **Natural Language Queries**: Ask questions like "What are our 2025 expansion plans?"  
✅ **Multi-Format Search**: Find insights across PDF, DOCX, PPTX, JPG documents  
✅ **Business Intelligence**: Strategic, operational, compliance, and training insights  
✅ **Executive Decision Support**: Instant access to investment analysis (demo figures)  
✅ **Cross-Category Analysis**: Unified view across all business functions  

---

## Quick Links

- **[Sample Questions](sample-questions.md)** - Categorized questions for demo presenters
- **[Taskfile Guide](taskfile.md)** - Advanced automation for power users
- **[Prerequisites](../getting-started/prerequisites.md){target="_blank"}** - Tool requirements and access setup
- **[Quick Setup](../getting-started/quick-setup.md){target="_blank"}** - Complete 15-minute setup guide  
- **[Getting Started](../getting-started/index.md){target="_blank"}** - Complete setup and prerequisites guide

---

**💡 Pro Tip:** Bookmark this page for quick command reference during demos!
