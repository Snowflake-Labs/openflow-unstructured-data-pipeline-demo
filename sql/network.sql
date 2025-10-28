-- Copyright 2025 Snowflake Inc.
-- SPDX-License-Identifier: Apache-2.0
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
-- http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.

-- Create schema for network rules
USE ROLE ACCOUNTADMIN;
USE DATABASE OPENFLOW_FESTIVAL_DEMO;
CREATE SCHEMA IF NOT EXISTS NETWORKS;
USE SCHEMA NETWORKS;

CREATE OR REPLACE NETWORK RULE google_network_rule
  MODE = EGRESS
  TYPE= HOST_PORT
  VALUE_LIST = (
                 'admin.googleapis.com',
                 'oauth2.googleapis.com',
                 'www.googleapis.com',
                 'google.com'
                );

DESC NETWORK RULE google_network_rule;

-- Create network rule for your Google Workspace domain
-- Replace 'your-domain.com' with your actual Google Workspace domain
CREATE OR REPLACE NETWORK RULE your_workspace_domain_network_rule
  MODE = EGRESS
  TYPE = HOST_PORT
  VALUE_LIST = ('your-domain.com');

-- Example: For a domain like kamesh.dev
-- CREATE OR REPLACE NETWORK RULE kameshs_dev_network_rule
--   MODE = EGRESS
--   TYPE = HOST_PORT
--   VALUE_LIST = ('kameshs.dev');

-- Verify the domain network rule was created successfully
DESC NETWORK RULE your_workspace_domain_network_rule;

-- Create external access integration with Google API access
-- If you created a workspace domain rule, add it to ALLOWED_NETWORK_RULES
CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION festival_ops_access_integration
  ALLOWED_NETWORK_RULES = (
    OPENFLOW_FESTIVAL_DEMO.NETWORKS.google_network_rule
    -- Add your workspace domain rule if created:
    -- , OPENFLOW_FESTIVAL_DEMO.NETWORKS.your_workspace_domain_network_rule
  )
  ENABLED = TRUE
  COMMENT = 'Used for Openflow SPCS runtime to access Google Drive';

-- Verify the external access integration was created with correct settings
DESC EXTERNAL ACCESS INTEGRATION festival_ops_access_integration;

-- Grant access to the external access integration
-- Grant access to the external access integration
GRANT USAGE ON DATABASE OPENFLOW_FESTIVAL_DEMO TO ROLE OPENFLOW_ADMIN;
GRANT USAGE ON SCHEMA OPENFLOW_FESTIVAL_DEMO.NETWORKS TO ROLE OPENFLOW_ADMIN;
GRANT USAGE ON INTEGRATION festival_ops_access_integration TO ROLE OPENFLOW_ADMIN;

GRANT USAGE ON INTEGRATION festival_ops_access_integration To ROLE FESTIVAL_DEMO_ROLE

-- Verify grants
SHOW GRANTS TO ROLE OPENFLOW_ADMIN;
  