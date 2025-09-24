# Slack Conversation Simulator Scripts

## Token Verification

Before running the conversation simulator, verify your bot tokens work correctly:

### Usage

```bash
# Install dependencies
uv sync

# Verify bot tokens only
python scripts/verify_tokens.py \
  --openflow-token "xoxb-your-openflow-bot-token" \
  --customer-token "xoxb-your-customer-bot-token" \
  --agent-token "xoxb-your-agent-bot-token"

# Verify bot tokens + app token (for Socket Mode apps)
python scripts/verify_tokens.py \
  --openflow-token "xoxb-your-openflow-bot-token" \
  --customer-token "xoxb-your-customer-bot-token" \
  --agent-token "xoxb-your-agent-bot-token" \
  --app-token "xapp-your-app-token"

# With debug logging
python scripts/verify_tokens.py \
  --openflow-token "xoxb-your-openflow-bot-token" \
  --customer-token "xoxb-your-customer-bot-token" \
  --agent-token "xoxb-your-agent-bot-token" \
  --log-level DEBUG
```

### Environment Variables (Alternative)

You can also set environment variables:

```bash
export OPENFLOW_BOT_TOKEN="xoxb-your-openflow-bot-token"
export CUSTOMER_BOT_TOKEN="xoxb-your-customer-bot-token"  
export AGENT_BOT_TOKEN="xoxb-your-agent-bot-token"
export APP_TOKEN="xapp-your-app-token"  # Optional for Socket Mode

python scripts/verify_tokens.py \
  --openflow-token "$OPENFLOW_BOT_TOKEN" \
  --customer-token "$CUSTOMER_BOT_TOKEN" \
  --agent-token "$AGENT_BOT_TOKEN" \
  --app-token "$APP_TOKEN"
```

### Expected Output

```text
14:32:15 | INFO     | 🚀 Festival Operations Token Verification
14:32:15 | INFO     | ==================================================
14:32:15 | INFO     | 🔍 Verifying OpenflowBot...
14:32:16 | INFO     | ✅ OpenflowBot: Authentication successful
14:32:16 | INFO     |    📋 Bot ID: U01ABC123DEF
14:32:16 | INFO     |    🤖 Bot Name: OpenflowBot
14:32:16 | INFO     |    🏢 Team: Festival Operations Demo
14:32:16 | INFO     |    📡 Can access 7 channels
14:32:16 | INFO     |    📋 Channels: festival-operations, tech-support, venue-coordination, weather-updates, customer-escalations, artist-management, festival-analytics
14:32:16 | INFO     | 🔍 Verifying CustomerBot...
14:32:17 | INFO     | ✅ CustomerBot: Authentication successful
14:32:17 | INFO     |    📋 Bot ID: U02XYZ456GHI
14:32:17 | INFO     |    🤖 Bot Name: CustomerBot
14:32:17 | INFO     |    🏢 Team: Festival Operations Demo
14:32:17 | INFO     |    📡 Can access 6 channels
14:32:17 | INFO     |    📋 Channels: festival-operations, tech-support, venue-coordination, weather-updates, customer-escalations, artist-management
14:32:17 | INFO     | 🔍 Verifying AgentBot...
14:32:18 | INFO     | ✅ AgentBot: Authentication successful
14:32:18 | INFO     |    📋 Bot ID: U03JKL789MNO
14:32:18 | INFO     |    🤖 Bot Name: AgentBot
14:32:18 | INFO     |    🏢 Team: Festival Operations Demo
14:32:18 | INFO     |    📡 Can access 6 channels
14:32:18 | INFO     |    📋 Channels: festival-operations, tech-support, venue-coordination, weather-updates, customer-escalations, artist-management
14:32:18 | INFO     | 
14:32:18 | INFO     | 🔍 App Token Verification...
14:32:18 | INFO     | 🔍 Verifying App Token (App Token)...
14:32:19 | INFO     | ✅ App Token: App token authentication successful
14:32:19 | INFO     |    📱 App ID: A01DEF456GHI
14:32:19 | INFO     |    🏢 Team: Festival Operations Demo
14:32:19 | INFO     |    🔌 App token validated - can be used for Socket Mode if configured
14:32:19 | INFO     | ==================================================
14:32:19 | INFO     | 📊 VERIFICATION SUMMARY
14:32:19 | INFO     | ==================================================
14:32:19 | INFO     | OpenflowBot : ✅ VALID
14:32:19 | INFO     | CustomerBot : ✅ VALID
14:32:19 | INFO     | AgentBot    : ✅ VALID
14:32:19 | INFO     | App Token   : ✅ VALID
14:32:19 | INFO     | 🎉 All tokens verified successfully!
14:32:19 | INFO     | 💡 Ready to run the conversation simulator
```

### Log Levels

- **INFO** (default): Shows verification progress and results
- **DEBUG**: Includes detailed API call information
- **WARNING**: Shows warnings and important notices
- **ERROR**: Only shows errors (minimal output)

### Token Types

#### Bot Tokens (xoxb-)

- **Required**: Used by bots to post messages and interact with channels
- **Permissions**: Channel access, message posting, file uploads
- **Usage**: All bot functionality (CustomerBot, AgentBot, OpenflowBot)

#### App Tokens (xapp-)

- **Optional**: Used for app-level features like Socket Mode
- **Permissions**: Real-time events, app management, connections
- **Usage**: Event subscriptions, interactive components, shortcuts
- **When needed**: If your app uses Socket Mode instead of HTTP endpoints

### Socket Mode vs HTTP Mode

- **HTTP Mode**: Uses bot tokens only, requires public endpoints
- **Socket Mode**: Uses app tokens + bot tokens, works behind firewalls
- **Recommendation**: Use Socket Mode for development/demos

## Reusable Logger Utility

All scripts use the shared `logger_utils.py` for consistent logging:

### Usage in Scripts

```python
from logger_utils import setup_logging, get_log_level_from_string, LOG_LEVEL_CHOICES

# Configure logger
logger = setup_logging(log_level, logger_name=__name__)

# Use throughout your script
logger.info("Information message")
logger.error("Error message")
logger.debug("Debug details")
```

### Features

- **Consistent formatting** with timestamps across all scripts
- **External library suppression** (Slack SDK, urllib3, etc.)
- **Helper functions** for sections, separators, and lists
- **Log level management** with string conversion

### Benefits

- **Uniform output** across all demo scripts
- **Easy debugging** with configurable log levels  
- **Professional logging** for production environments
- **Reusable components** for future scripts

## Conversation Simulator

Generate readable conversation files from CSV data for review before sending to Slack:

### Usage

```bash
# Basic usage - generates markdown files in work/conversations/
python scripts/conversation_simulator.py

# Custom CSV file and output directory
python scripts/conversation_simulator.py \
  --csv-file "sample-data/demo_slack_conversations.csv" \
  --output-dir "work/my-conversations"

# With debug logging
python scripts/conversation_simulator.py --log-level DEBUG
```

### Generated Files

The simulator creates organized conversation files in `work/conversations/`:

```text
work/conversations/
├── channels/              # Individual channel conversations
│   ├── customer_escalations.md
│   ├── festival_operations.md
│   ├── tech_support.md
│   └── ...
├── timeline/              # Chronological timeline views
│   ├── timeline_2025-04-15.md
│   ├── timeline_2025-05-20.md
│   └── ...
└── summary/               # Statistics and insights
    └── conversation_summary.md
```

### Example Channel File

```markdown
# #customer-escalations

**Messages:** 10 | **Generated:** 2024-12-19 14:32:18

---

## 2025-05-19

**👤 CustomerBot** `16:30:00`

Hi there! This is Sarah from LA. I'm having trouble with my VIP access for Beat Valley tomorrow. The app won't let me download my digital pass 😞

**🎧 AgentBot** `16:33:00`

Hi Sarah! I'm Ashley from VIP Services. I see you're customer ID 1001 - let me check your account right away. Can you try logging out and back in?

  ↳ **👤 CustomerBot** `16:35:00`

  I tried that 3 times already 😩 Really worried I won't get in tomorrow. I flew in from LA specifically for Voltage Master!
```

### Benefits

- **Visual Review**: See exactly what conversations will look like before sending
- **Timeline Analysis**: Understand conversation flow and timing
- **Statistics**: Get insights into user activity and channel usage
- **Debug Friendly**: Easy to spot issues in conversation data
- **Git Ignored**: Work folder won't be committed to version control

## Slack Message Sender

Send conversations to actual Slack channels using your bot tokens:

### Prerequisites

1. **Set up Slack workspace** following `sample-data/slack_workspace_setup.md`
2. **Verify bot tokens** work with `scripts/verify_tokens.py`
3. **Create all required channels** and add bots as per setup guide

### Usage

#### Dry Run (Recommended First)

Test without actually sending messages:

```bash
# Dry run to validate everything works
python scripts/slack_message_sender.py \
  --openflow-token "xoxb-your-openflow-token" \
  --customer-token "xoxb-your-customer-token" \
  --agent-token "xoxb-your-agent-token" \
  --dry-run

# Test with first 5 messages only
python scripts/slack_message_sender.py \
  --openflow-token "xoxb-your-openflow-token" \
  --customer-token "xoxb-your-customer-token" \
  --agent-token "xoxb-your-agent-token" \
  --max-messages 5 \
  --dry-run
```

#### Live Sending

Send conversations to actual Slack channels:

```bash
# Send all conversations immediately
python scripts/slack_message_sender.py \
  --openflow-token "xoxb-your-openflow-token" \
  --customer-token "xoxb-your-customer-token" \
  --agent-token "xoxb-your-agent-token"

# Live demo mode with 2-second stagger between messages
python scripts/slack_message_sender.py \
  --openflow-token "xoxb-your-openflow-token" \
  --customer-token "xoxb-your-customer-token" \
  --agent-token "xoxb-your-agent-token" \
  --stagger 2.0

# Send first 10 messages with stagger for controlled demo
python scripts/slack_message_sender.py \
  --openflow-token "xoxb-your-openflow-token" \
  --customer-token "xoxb-your-customer-token" \
  --agent-token "xoxb-your-agent-token" \
  --max-messages 10 \
  --stagger 3.0
```

#### Environment Variables (Recommended)

For security, use environment variables:

```bash
# Set your tokens
export OPENFLOW_BOT_TOKEN="xoxb-your-openflow-token"
export CUSTOMER_BOT_TOKEN="xoxb-your-customer-token"  
export AGENT_BOT_TOKEN="xoxb-your-agent-token"

# Send conversations
python scripts/slack_message_sender.py \
  --openflow-token "$OPENFLOW_BOT_TOKEN" \
  --customer-token "$CUSTOMER_BOT_TOKEN" \
  --agent-token "$AGENT_BOT_TOKEN" \
  --stagger 1.5
```

### Key Features

#### Smart Bot Selection

- **CustomerBot**: Posts as customer personas (Sarah, Michael, Emma, etc.)
- **AgentBot**: Responds as company staff (Ashley VIP Services, Ryan Tech Support, etc.)
- **OpenflowBot**: Extracts conversation data for Snowflake OpenFlow processing

#### Thread Support

- **Automatic threading**: Replies are posted as Slack threads
- **Conversation context**: Maintains discussion flow and relationships
- **Thread timestamp tracking**: Ensures proper reply structure

#### Demo-Friendly Options

- **Staggered loading**: `--stagger 2.0` waits 2 seconds between messages
- **Message limits**: `--max-messages 10` for controlled demos
- **Dry run mode**: `--dry-run` to test without sending
- **Channel validation**: Checks channel exists and bot has access

#### Error Handling

- **Rate limiting**: Respects Slack API limits
- **Permission checks**: Validates bot access to channels
- **Graceful failures**: Continues processing even if some messages fail
- **Detailed logging**: Shows exactly what's happening

### Expected Output

```text
14:32:18 | INFO     | 🚀 Slack Message Sender
14:32:18 | INFO     | 🤖 Initialized Slack clients (LIVE MODE)
14:32:18 | INFO     | 📂 Loading conversations from sample-data/demo_slack_conversations.csv
14:32:18 | INFO     |    📊 Loaded 26 messages
14:32:18 | INFO     |    ✅ Conversation data validated
14:32:18 | INFO     | ===================================================
14:32:18 | INFO     | 📤 Sending Conversations to Slack
14:32:18 | INFO     | ===================================================
14:32:18 | INFO     | 📊 Processing all 26 messages
14:32:19 | INFO     | 📡 Processing channel: #customer-escalations
14:32:21 | INFO     | 📡 Processing channel: #festival-operations
14:32:23 | INFO     | 📡 Processing channel: #tech-support
14:32:24 | INFO     | ===================================================
14:32:24 | INFO     | 📊 Sending Complete
14:32:24 | INFO     | ===================================================
14:32:24 | INFO     | ✅ Messages sent: 26
14:32:24 | INFO     | ❌ Messages failed: 0
14:32:24 | INFO     | 📡 Channels processed: 7
14:32:24 | INFO     | 🎉 All conversations sent to Slack channels!
```

### Testing

Test the sender without tokens:

```bash
# Run the test script (safe dry run)
python scripts/test_slack_sender.py
```

### Troubleshooting

#### Common Issues

1. **Channel not found**
   - Ensure channels are created as per `slack_workspace_setup.md`
   - Check channel names match CSV data exactly

2. **Bot permissions denied**
   - Verify bots are added to all required channels
   - Check OAuth scopes in bot manifests

3. **Token invalid**
   - Run `scripts/verify_tokens.py` to validate tokens
   - Ensure tokens start with `xoxb-` for bot tokens

4. **Rate limiting**
   - Use `--stagger` option to slow down sending
   - Reduce `--max-messages` for testing

## Resume System & Progress Tracking

### Advanced Message Control

The `slack_message_sender.py` includes a powerful resume system for controlled demo scenarios:

#### Key Features

🔄 **Progress Tracking**: Automatically saves position after each successful message  
📄 **State Persistence**: Resume across script runs using JSON progress file  
🎯 **Batch Control**: Send messages in controlled chunks for live demos  
⏭️  **Flexible Positioning**: Start from any position or resume from last  

#### Demo Scenarios

```bash
# Scenario 1: Controlled Demo Batches
./slack_message_sender.py --max-messages 5 --tokens...     # Send 1-5
./slack_message_sender.py --max-messages 5 --resume        # Send 6-10  
./slack_message_sender.py --max-messages 10 --resume       # Send 11-20

# Scenario 2: Skip to Specific Position  
./slack_message_sender.py --max-messages 3 --start-offset 15   # Send 16-18

# Scenario 3: Complete Remaining Messages
./slack_message_sender.py --max-messages 50 --resume       # Send all remaining
```

#### Progress File Structure

```json
{
  "sent_count": 15,
  "last_processed_index": 14,
  "sent_message_ids": ["MSG101", "MSG102", ...],
  "failed_message_ids": [],
  "timestamp": "2025-08-10 18:32:00+00:00"
}
```

#### Resume Arguments

- `--resume`: Continue from last successful position
- `--start-offset N`: Skip first N messages, start from N+1  
- `--progress-file FILE`: Custom progress tracking file (default: `work/message_progress.json`)
- `--max-messages N`: Limit messages per run (required for control)

## Complete Demo Workflow

1. **Set up Slack workspace**: `slack_workspace_setup.md`
2. **Verify tokens work**: `python scripts/verify_tokens.py --openflow-token ... --customer-token ... --agent-token ...`
3. **Generate readable conversations**: `python scripts/conversation_simulator.py`
4. **Test message sender**: `python scripts/slack_message_sender.py --dry-run --max-messages 3`
5. **Send in batches**: `python scripts/slack_message_sender.py --max-messages 5 --stagger 2.0 --tokens...`
6. **Resume demo**: `python scripts/slack_message_sender.py --resume --max-messages 5 --stagger 2.0 --tokens...`
7. **Demo Snowflake OpenFlow** processing the conversations from Slack channels

This creates a comprehensive demonstration of unstructured data processing with complete control over message
timing and batching for live demos.

## Taskfile Integration

All resume system features are available as convenient Taskfile tasks for easy execution:

### Demo Tasks (with test tokens)

```bash
# Test demo sequence with dry run
task demo-dry-run                          # Send 3 messages (default)
task demo-dry-run MAX_MESSAGES=5           # Send 5 messages  
task demo-dry-run-resume                   # Resume from last position

# Test comprehensive resume system
task test-resume-system                    # Full end-to-end test
task reset-progress                        # Clean up progress files
```

### Live Demo Tasks (requires environment variables)

```bash
# Set your bot tokens first
export OPENFLOW_BOT_TOKEN="xoxb-your-openflow-token"
export CUSTOMER_BOT_TOKEN="xoxb-your-customer-token"
export AGENT_BOT_TOKEN="xoxb-your-agent-token"

# Live demo execution
task send-demo-batch                       # Send 5 messages with 2s stagger (default)
task send-demo-batch MAX_MESSAGES=3 STAGGER=1  # Custom batch size and timing
task resume-demo                           # Resume from last position
task resume-demo MAX_MESSAGES=10 STAGGER=3     # Custom resume parameters

# Manual positioning  
task send-from-offset START_OFFSET=10 MAX_MESSAGES=5  # Start from message 11, send 5
```

### Available Tasks

| Task | Description | Key Parameters |
|------|-------------|----------------|
| `demo-dry-run` | Test demo with fake tokens | `MAX_MESSAGES` (default: 3) |
| `demo-dry-run-resume` | Test resume with fake tokens | `MAX_MESSAGES` (default: 3) |
| `send-demo-batch` | Live demo batch sending | `MAX_MESSAGES` (5), `STAGGER` (2) |
| `resume-demo` | Resume live demo | `MAX_MESSAGES` (5), `STAGGER` (2) |
| `send-from-offset` | Start from specific position | `START_OFFSET` (0), `MAX_MESSAGES` (3), `STAGGER` (1) |
| `test-resume-system` | Comprehensive test suite | None |
| `reset-progress` | Clean progress files | None |

### Example Demo Sequence

```bash
# 1. Test your demo flow first
task reset-progress
task demo-dry-run MAX_MESSAGES=5
task demo-dry-run-resume MAX_MESSAGES=5

# 2. Set environment variables for live tokens
export OPENFLOW_BOT_TOKEN="xoxb-..."
export CUSTOMER_BOT_TOKEN="xoxb-..." 
export AGENT_BOT_TOKEN="xoxb-..."

# 3. Execute live demo
task send-demo-batch MAX_MESSAGES=5 STAGGER=3    # Start with 5 messages, 3s between
task resume-demo MAX_MESSAGES=5 STAGGER=2        # Continue with 5 more, 2s between
task resume-demo MAX_MESSAGES=10                 # Finish remaining quickly
```

This Taskfile integration makes the resume system extremely convenient for live presentations and testing scenarios.
