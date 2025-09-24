# Festival Operations Analytics Documentation

This directory contains comprehensive analysis and demo guidance for the Snowflake Intelligence and Cortex Search demonstration using festival operations conversation data.

## Documentation Overview

### 📊 [Document Intelligence Analysis](./document_intelligence_analysis.md)

**Comprehensive data analysis and business intelligence opportunities**

- **Data Foundation**: 24 conversations across 6 channels, 9 cities
- **Key Insights**: Customer experience, operational performance, service excellence
- **Business Value**: Revenue protection, efficiency gains, risk mitigation
- **Query Opportunities**: 16+ Cortex Search query scenarios

**Use this for**: Understanding what insights are available in the data, preparing business cases, identifying specific analytics opportunities.

### 🎬 [Demo Execution Guide](./demo_execution_guide.md)

**Complete presenter-friendly guide consolidating demo execution, questions, and conversation blocks**

- **6 Conversation Blocks**: Strategic start-resume pattern (messages 1-24)
- **50+ Interactive Questions**: Customer experience, operations, business intelligence, predictive analytics
- **3 Demo Flow Options**: 15, 20, and 30-minute complete pipeline demonstrations
- **Step-by-Step Script**: Phase-by-phase execution with expected results and business value
- **Audience-Specific**: Talking points for C-level, operations, and technical teams
- **Command Reference**: Complete `task` commands for live demonstrations

**Use this for**: All demo activities - preparation, execution, audience engagement, and follow-up.

## Quick Reference

### Top 5 Demo Queries

1. **Customer Personas**: `"Show me all conversations from VIP customers"`
2. **Customer Journey**: `"Show me customers who went from frustrated to grateful"`
3. **Venue Intelligence**: `"Which venues generated the most customer complaints?"`
4. **Agent Performance**: `"How quickly do our agents respond to different types of issues?"`
5. **Business Impact**: `"Which customers received compensation and why?"`

### Demo Flow Overview

**6 Conversation Blocks** demonstrate complete Slack → OpenFlow → Cortex Search pipeline:

1. **Emergency Response** (5 msgs): Emma transportation + Connor weather concerns
2. **VIP Service Excellence** (4 msgs): Sarah Johnson digital pass complete resolution  
3. **Real-Time Operations** (3 msgs): Michael Circuit Zone sound issue immediate fix
4. **Crowd Management** (3 msgs): David Main Arena congestion creative solution
5. **Technical Support** (3 msgs): Tyler app crash + proactive IT solution
6. **Service Recovery** (6 msgs): Multiple scenarios showing resolution variety

**Commands**: `task send-demo-batch MAX_MESSAGES=5` → `task resume-demo` → continue blocks

### Key Business Value Props

- **Customer Experience**: 6 negative → 6 positive sentiment conversions
- **Operational Efficiency**: 2-5 minute average response times
- **Geographic Reach**: 9 cities, national customer base
- **VIP Revenue Protection**: 9 VIP interactions with high satisfaction

### Technical Foundation

- **Dataset**: 24 realistic customer service conversations
- **Channels**: customer-escalations, tech-support, venue-coordination, etc.
- **Technology**: Snowflake Intelligence + Cortex Search
- **Query Method**: Natural language, no SQL required

## Next Steps

### Phase 1: Implementation Preparation

1. Review both analysis documents thoroughly
2. Set up Snowflake environment with Cortex Search
3. Load conversation data and test sample queries
4. Practice demo flow with stakeholders

### Phase 2: Demo Delivery

1. Use execution guide for structured presentation
2. Focus on business value over technical details
3. Encourage audience interaction with queries
4. Capture follow-up requirements and next steps

### Phase 3: Expansion Planning

1. Identify additional data sources for integration
2. Scale to larger conversation datasets
3. Implement advanced analytics (predictive modeling)
4. Connect to operational business systems

## Support Resources

### Data Files

- `../sample-data/demo_slack_conversations.csv` - Core conversation dataset
- `../sample-data/slack_users.csv` - User/bot definitions
- `../sample-data/slack_channels.csv` - Channel metadata

### Demo Tools

- `../Taskfile.yml` - Automated demo setup and testing commands

### Configuration

- `../slack-manifests/` - Bot configuration for Slack integration
- `../sample-data/slack_workspace_setup.md` - Complete setup guide

---

**Ready to demonstrate how unstructured conversation data becomes actionable business intelligence with Snowflake Intelligence and Cortex Search!** 🚀
