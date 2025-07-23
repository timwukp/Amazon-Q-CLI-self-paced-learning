# 90-Minute Amazon Q CLI Live Demo Course

**SDLC Integration with MCP & Advanced Prompting for Principal Engineers**

## 🎯 Course Overview

This 90-minute live demonstration showcases Amazon Q CLI's complete Software Development Lifecycle (SDLC) integration capabilities, specifically designed for principal software engineers familiar with Cursor, GitLab, and GCP who are exploring AWS adoption.

## 📋 Prerequisites

### Required Knowledge:
- Familiarity with Cursor AI-assisted development
- Experience with GitLab CI/CD workflows
- Basic understanding of GCP services (Cloud Run, Cloud Storage, Cloud SQL)
- Principal-level software engineering experience

### Technical Setup:
```bash
# Amazon Q CLI installation
curl -sSL https://amazon-q-cli.dev/install | bash

# Verify installation
q --version

# Configure MCP servers (see mcp-setup-guide.md)
q settings mcp.initTimeout 30000
```

## 🚀 Demo Structure (90 minutes)

### Opening Hook (10 minutes)
**"From Cursor to Cloud Intelligence"**
- Position Amazon Q CLI as Cursor for infrastructure
- Show familiar conversational interface
- Demonstrate context awareness across tools

### Section 1: PLAN & CODE (20 minutes)
**"GCP to AWS Translation with Intelligence"**

#### PLAN Phase (10 minutes)
```bash
# Architecture planning with GCP context
q chat "As a principal engineer familiar with GCP Cloud Functions, help me understand AWS Lambda equivalents and create a serverless image processing API"

# Cost comparison and migration strategy
q chat "I currently use Cloud Run, Cloud Storage, and Cloud SQL. Design equivalent AWS architecture with cost comparison and migration roadmap"
```

#### CODE Phase (10 minutes)
```bash
# Cursor-style code generation
q chat "Create a Lambda function equivalent to my GCP Cloud Function, maintaining the same API contract and error handling patterns"

# GitLab integration patterns
q chat "Generate AWS CDK code that matches my current Terraform patterns for GCP, with GitLab CI/CD integration"
```

### Section 2: BUILD & TEST (20 minutes)
**"GitLab CI/CD Meets AWS Intelligence"**

#### BUILD Phase (10 minutes)
```bash
# GitLab workflow enhancement
q chat "Analyze my existing GitLab CI/CD pipeline and add AWS deployment stages alongside my current GCP deployments"

# Multi-cloud build optimization
q chat "Create parallel deployment strategies for both AWS and GCP while maintaining GitLab best practices"
```

#### TEST Phase (10 minutes)
```bash
# Cross-cloud testing strategy
q chat "Create comprehensive tests for my AWS infrastructure that mirror my existing GCP testing patterns and include cross-cloud integration tests"

# Performance benchmarking
q chat "Generate performance tests that validate AWS response times against my current GCP baselines"
```

### Section 3: REVIEW & DEPLOY (20 minutes)
**"Intelligent Code Review & Multi-Cloud Operations"**

#### REVIEW Phase (10 minutes)
```bash
# Multi-cloud code review
q chat "Review my infrastructure changes comparing AWS resource configurations to GCP equivalents, checking security and cost implications"

# Documentation generation
q chat "Generate documentation that helps my team understand AWS services using our familiar GCP service equivalents"
```

#### DEPLOY Phase (10 minutes)
```bash
# Multi-cloud deployment
q chat "Deploy my application to AWS while maintaining my GCP deployment, with cross-cloud monitoring and intelligent traffic routing"

# Cost optimization across clouds
q chat "Create cost comparison reports and optimization recommendations for both AWS and GCP platforms"
```

### Section 4: MONITOR & MAINTAIN (15 minutes)
**"Cross-Cloud Intelligence & Optimization"**

```bash
# Advanced monitoring
q chat "Create monitoring strategy that correlates performance metrics between AWS and GCP, with unified alerting"

# Intelligent incident response
q chat "Analyze my production system health across both clouds and generate comprehensive optimization recommendations"
```

### Closing & Q&A (5 minutes)
**Key takeaways and next steps**

## 🎭 Live Demo Scenarios

### Scenario A: "The 3AM Production Issue"
**Demonstrate**: Real-time log analysis, cross-cloud correlation, intelligent fix suggestions

### Scenario B: "New Feature Deployment"
**Demonstrate**: Code generation, testing, security scanning, multi-cloud deployment

### Scenario C: "Cost Optimization Discovery"
**Demonstrate**: Cross-cloud cost analysis, optimization recommendations, implementation

## 🧠 Advanced Prompting Techniques Demonstrated

### Global Prompting Rules:
```bash
# Rule 1: Context-Aware Prompting
"Given my current GCP setup and GitLab workflows, [specific AWS request]"

# Rule 2: Role-Based Prompting
"As a principal engineer transitioning from GCP to AWS, [action] considering our team's expertise"

# Rule 3: Constraint-Driven Prompting
"[Request] with constraints: maintain GitLab workflows, budget under $200/month, GDPR compliant"

# Rule 4: Multi-Step Prompting
"First analyze my GCP patterns, then recommend AWS equivalents, finally implement with migration strategy"
```

### MCP Integration Patterns:
```bash
# Multi-tool orchestration
q chat "Use GitHub MCP to analyze my repository patterns, then AWS MCP to create equivalent infrastructure, then CloudWatch MCP to set up monitoring"

# Cross-platform intelligence
q chat "Correlate my GitLab deployment history with AWS CloudWatch metrics to identify optimization opportunities"
```

## 🎯 Value Propositions for Principal Engineers

### Technical Sophistication:
- **"Same AI-first approach as Cursor, but for complete infrastructure lifecycle"**
- **"Maintains your high engineering standards across cloud platforms"**
- **"Intelligent automation that respects your architectural decisions"**

### Strategic Benefits:
- **"Accelerate AWS adoption without abandoning GCP investments"**
- **"Make informed multi-cloud decisions with data-driven insights"**
- **"Reduce context switching between development and operations"**

### Practical Impact:
- **"Deploy to AWS as easily as you deploy to GCP"**
- **"Maintain GitLab workflows while adding AWS capabilities"**
- **"Leverage existing team knowledge for faster cloud adoption"**

## 📊 Demo Success Metrics

### Immediate Indicators:
- Audience asking specific technical questions
- Requests to see particular use cases
- Discussion about integration with current tools
- Questions about enterprise features and security

### Follow-up Opportunities:
- Requests for POC or trial access
- Discussion about team training
- Questions about enterprise support
- Interest in specific MCP server integrations

## 🛠️ Demo Preparation Checklist

### Environment Setup:
```bash
# Verify MCP servers
q settings all | grep mcp
/tools  # List available tools
/prompts  # List available prompts

# Prepare sample data
# - Active GitHub repository
# - AWS account with resources
# - CloudWatch logs with real data
# - Cost data for examples
```

### Demo Materials:
- [ ] Live AWS environment with sample resources
- [ ] GitHub repository with realistic code patterns
- [ ] CloudWatch logs with actual error patterns
- [ ] Cost data for optimization demonstrations
- [ ] Backup scenarios in case of technical issues

## 📚 Supporting Materials

- **MCP Setup Guide**: `mcp-setup-guide.md`
- **Prompting Templates**: `prompting-templates.md`
- **Demo Scenarios**: `demo-scenarios.md`
- **Assessment Guide**: `demo-assessment.md`

## 🎓 Completion Certificate

Upon completing this demo course, participants receive:
- **Amazon Q CLI Demo Completion Certificate**
- **Advanced Prompting Techniques Reference**
- **MCP Integration Quick Start Guide**
- **Pathway to 5-Day Comprehensive Course**

## 📞 Support

- **Demo Questions**: demo-support@amazon-q-cli.dev
- **Technical Issues**: tech-support@amazon-q-cli.dev
- **Next Steps Guidance**: pathway@amazon-q-cli.dev

---

**Ready to Start?** Follow the setup guide in `mcp-setup-guide.md` then review the detailed prompting templates in `prompting-templates.md`.