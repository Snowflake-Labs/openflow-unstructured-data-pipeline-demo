"""
MkDocs Macros Plugin - Custom macros for the OpenFlow demo documentation
"""


def define_env(env):
    """
    Define custom macros, variables and filters for the MkDocs environment
    """

    # Demo statistics
    env.variables["total_documents"] = 16
    env.variables["document_formats"] = ["PDF", "DOCX", "PPTX", "JPG"]
    env.variables["business_categories"] = 4
    env.variables["demo_duration"] = "15-30 minutes"

    # Business metrics
    env.variables["investment_amount"] = "$2.8M"
    env.variables["revenue_growth"] = "15%"
    env.variables["time_savings"] = "90%"
    env.variables["new_markets"] = 3

    # Technical details
    env.variables["embedding_model"] = "snowflake-arctic-embed-m-v1.5"
    env.variables["search_service"] = "festival_service_improved"
    env.variables["warehouse"] = "compute_wh"

    @env.macro
    def demo_stats():
        """Generate demo statistics summary"""
        return f"""
| Metric | Value |
|--------|-------|
| **Total Documents** | {env.variables["total_documents"]} |
| **Document Formats** | {len(env.variables["document_formats"])} |
| **Business Categories** | {env.variables["business_categories"]} |
| **Demo Duration** | {env.variables["demo_duration"]} |
| **Investment Showcase** | {env.variables["investment_amount"]} |
| **Expected Time Savings** | {env.variables["time_savings"]} |
"""

    @env.macro
    def format_list(items, connector="and"):
        """Format a list with proper grammar"""
        if len(items) <= 1:
            return items[0] if items else ""
        elif len(items) == 2:
            return f"{items[0]} {connector} {items[1]}"
        else:
            return f"{', '.join(items[:-1])}, {connector} {items[-1]}"

    @env.macro
    def business_value_table():
        """Generate business value comparison table"""
        return """
| Capability | Traditional Approach | With Document Intelligence | Improvement |
|------------|---------------------|---------------------------|-------------|
| **Document Search** | 30-60 min manual search | 5-second natural language query | **90% faster** |
| **Cross-format Analysis** | Manual review required | Instant unified insights | **New capability** |
| **Executive Access** | IT support needed | Self-service queries | **100% autonomy** |
| **Compliance Lookup** | Hours of document hunting | Instant policy access | **95% time savings** |
"""

    @env.macro
    def query_example(category, query, description=""):
        """Generate a formatted query example"""
        return f"""
!!! example "{category} Query"
    **Query**: *"{query}"*
    
    {description if description else ""}
    
    ```sql
    SELECT PARSE_JSON(
      SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
          '{env.variables["search_service"]}',
          '{{"query": "{query.lower()}", "limit": 5}}'
      )
    )['results'] as search_results;
    ```
"""
