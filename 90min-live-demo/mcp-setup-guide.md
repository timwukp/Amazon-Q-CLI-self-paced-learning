# MCP Setup Guide for Amazon Q CLI Demo

**Configure Model Context Protocol servers for the live demonstration**

## 🎯 Overview

This guide sets up the MCP servers required for the 90-minute Amazon Q CLI demonstration, specifically configured for principal engineers familiar with Cursor, GitLab, and GCP.

## 📋 Prerequisites

```bash
# Verify Amazon Q CLI installation
q --version
# Should show version 1.0.0 or higher

# Check Node.js version (required for MCP servers)
node --version
# Should show v16.0.0 or higher

# Verify AWS CLI configuration
aws sts get-caller-identity
# Should return your AWS account information
```

## 🔧 MCP Server Configuration

### Step 1: Configure MCP Initialization Timeout
```bash
# Set longer timeout for demo environment
q settings mcp.initTimeout 30000

# Verify setting
q settings mcp.initTimeout
```

### Step 2: Configure GitHub MCP Server
```bash
# GitHub MCP server configuration
q settings mcp.servers.github.command "npx"
q settings mcp.servers.github.args '["@modelcontextprotocol/server-github"]'
q settings mcp.servers.github.env.GITHUB_PERSONAL_ACCESS_TOKEN "your-github-token"
```

**GitHub Token Setup:**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate token with scopes: `repo`, `read:org`, `read:user`
3. Replace `your-github-token` with actual token

### Step 3: Configure AWS MCP Server
```bash
# AWS MCP server configuration
q settings mcp.servers.aws.command "npx"
q settings mcp.servers.aws.args '["@aws-labs/mcp-server-aws"]'
```

### Step 4: Configure CloudWatch MCP Server
```bash
# CloudWatch MCP server configuration
q settings mcp.servers.cloudwatch.command "npx"
q settings mcp.servers.cloudwatch.args '["@aws-labs/mcp-server-cloudwatch"]'
q settings mcp.servers.cloudwatch.env.AWS_REGION "us-east-1"
```

### Step 5: Configure Core MCP Server
```bash
# Core MCP server for prompt understanding
q settings mcp.servers.core.command "npx"
q settings mcp.servers.core.args '["@aws-labs/mcp-server-core"]'
```

### Step 6: Configure Documentation MCP Server
```bash
# AWS Documentation MCP server
q settings mcp.servers.awsdocs.command "npx"
q settings mcp.servers.awsdocs.args '["@aws-labs/mcp-server-aws-documentation"]'
```

## ✅ Verification Steps

### Check MCP Server Status
```bash
# List all configured MCP servers
q settings all | grep mcp

# Check server loading status
/tools
# Should show tools from all configured servers

# Check available prompts
/prompts
# Should show prompts from MCP servers
```

### Test MCP Integration
```bash
# Test GitHub MCP
q chat "List my GitHub repositories"

# Test AWS MCP
q chat "Show my AWS EC2 instances"

# Test CloudWatch MCP
q chat "Get CloudWatch metrics for the last hour"

# Test Documentation MCP
q chat "Search AWS documentation for Lambda best practices"
```

## 🔍 Troubleshooting

### Common Issues and Solutions

#### Issue: MCP servers not loading
```bash
# Check initialization timeout
q settings mcp.initTimeout
# Increase if needed
q settings mcp.initTimeout 60000

# Restart Q CLI session
q quit
q chat
```

#### Issue: GitHub MCP authentication failed
```bash
# Verify token permissions
# Token needs: repo, read:org, read:user scopes

# Test token manually
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```

#### Issue: AWS MCP permissions error
```bash
# Check AWS credentials
aws sts get-caller-identity

# Verify required permissions
# Minimum: EC2:Describe*, CloudWatch:Get*, CloudWatch:List*
```

#### Issue: Tools not appearing
```bash
# Force refresh MCP servers
q settings mcp.initTimeout 0
q settings mcp.initTimeout 30000

# Restart Q CLI
q quit
q chat
/tools
```

## 🎭 Demo-Specific Configuration

### For Live Demo Environment
```bash
# Set demo-friendly timeouts
q settings mcp.initTimeout 45000

# Configure demo AWS region
q settings mcp.servers.cloudwatch.env.AWS_REGION "us-west-2"
q settings mcp.servers.aws.env.AWS_DEFAULT_REGION "us-west-2"

# Enable verbose logging for troubleshooting
q settings debug true
```

### Sample Data Preparation
```bash
# Ensure demo AWS resources exist
# - At least one EC2 instance
# - CloudWatch logs with recent entries
# - S3 buckets with sample data
# - Lambda functions for demonstration

# Verify GitHub repository access
# - Repository with recent commits
# - Pull requests for review demonstration
# - Issues for management demonstration
```

## 📊 MCP Server Capabilities

### GitHub MCP Tools:
- `github___search_repositories`
- `github___get_file_contents`
- `github___create_pull_request`
- `github___get_pull_request_diff`
- `github___create_issue`
- `github___list_notifications`

### AWS MCP Tools:
- `use_aws` (general AWS CLI operations)
- EC2 instance management
- S3 bucket operations
- Lambda function deployment
- IAM policy management

### CloudWatch MCP Tools:
- `awslabscloudwatch_mcp_server___get_metric_data`
- `awslabscloudwatch_mcp_server___execute_log_insights_query`
- `awslabscloudwatch_mcp_server___get_active_alarms`
- `awslabscloudwatch_mcp_server___analyze_log_group`

### Documentation MCP Tools:
- `awslabsaws_documentation_mcp_server___search_documentation`
- `awslabsaws_documentation_mcp_server___read_documentation`
- `awslabsaws_documentation_mcp_server___recommend`

## 🚀 Demo Readiness Checklist

### Pre-Demo Verification:
- [ ] All MCP servers loading successfully
- [ ] GitHub authentication working
- [ ] AWS credentials configured
- [ ] CloudWatch data available
- [ ] Sample repositories accessible
- [ ] Demo scenarios tested
- [ ] Backup plans prepared

### During Demo:
- [ ] Monitor MCP server status with `/tools`
- [ ] Have fallback examples ready
- [ ] Keep troubleshooting commands handy
- [ ] Monitor response times

## 📞 Support During Demo

If issues arise during the live demonstration:

1. **Quick Fixes**: Use troubleshooting commands above
2. **Fallback**: Switch to pre-recorded examples
3. **Support**: Contact demo-support@amazon-q-cli.dev
4. **Escalation**: Use backup demonstration materials

---

**Next Step**: Review `prompting-templates.md` for the specific prompting patterns used in the demonstration.