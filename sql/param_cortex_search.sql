CREATE OR REPLACE CORTEX SEARCH SERVICE #{Destination Database}.#{Destination Schema}.#{Cortex Search Name}
  ON text
  ATTRIBUTES
    channel,
    user_id, 
    username,
    workspace_id,
    ts,
    member_emails,
    thread_ts
  WAREHOUSE = '#{Snowflake Warehouse}'
  TARGET_LAG = '60 minutes'
  EMBEDDING_MODEL = '#{Snowflake Cortex Embedding Model}'
  AS (
    WITH membership_data AS (
        SELECT 
            conversationId AS conversation_id,
            TO_ARRAY(memberemails) AS member_emails
        FROM #{Destination Database}.#{Destination Schema}.SLACK_MEMBERSHIP
    ), 
    filtered_messages AS (
        SELECT 
            text,
            type,
            subtype,
            channel,
            user AS user_id,
            username,
            workspaceId AS workspace_id,
            ts,
            threadTs AS thread_ts
        FROM #{Destination Database}.#{Destination Schema}.SLACK_MESSAGES 
        WHERE subtype IS NULL
    ),
    slack_data AS (
        SELECT 
            fm.text,
            fm.type,
            fm.subtype,
            fm.channel,
            fm.user_id,
            fm.username,
            fm.workspace_id,
            fm.ts,
            fm.thread_ts,
            md.member_emails
        FROM filtered_messages fm
        JOIN membership_data md
          ON fm.channel = md.conversation_id

        UNION ALL

        SELECT 
            docs_chunks.chunk AS text,
            'DOCS_CHUNK' AS type,
            NULL AS subtype,
            docs_chunks.channel,
            docs_chunks.user_id,
            NULL AS username,
            NULL AS workspace_id,
            docs_chunks.event_ts AS ts,
            NULL AS thread_ts,
            md.member_emails
        FROM #{Destination Database}.#{Destination Schema}.DOCS_CHUNKS docs_chunks
        JOIN membership_data md
          ON docs_chunks.channel = md.conversation_id
    )
    SELECT 
        text,
        user_id,
        channel,
        username,
        workspace_id,
        ts,
        member_emails,
        thread_ts
    FROM slack_data
  );
