# Live Demo Scenarios for Amazon Q CLI

**Real-world scenarios demonstrating SDLC integration with MCP orchestration**

## 🎯 Overview

These scenarios are designed to showcase Amazon Q CLI's capabilities in realistic situations that principal engineers encounter daily, with specific focus on GCP-to-AWS transitions and GitLab workflow integration.

## 🚨 Scenario A: "The 3AM Production Issue"
**Duration**: 15 minutes  
**Demonstrates**: Real-time incident response, cross-cloud correlation, intelligent troubleshooting

### Setup Context:
```bash
# Production API experiencing 500 errors
# Team uses both GCP and AWS services
# GitLab CI/CD recently deployed changes
# Need rapid diagnosis and resolution
```

### Demo Flow:

#### Step 1: Initial Assessment (3 minutes)
```bash
q chat "As an incident commander responding to API 500 errors, help me:
1. Analyze CloudWatch logs for error patterns in the last 2 hours
2. Correlate with recent GitLab deployments from our repository
3. Check AWS resource health and performance metrics
4. Identify potential root causes and affected user impact"
```

**Expected Outcome**: Comprehensive incident overview with specific error patterns and deployment correlation

#### Step 2: Root Cause Analysis (5 minutes)
```bash
q chat "Based on the error patterns found, dive deeper by:
1. Querying CloudWatch Logs Insights for specific error details
2. Analyzing AWS Lambda function performance and timeout issues
3. Checking S3 and RDS connectivity and performance
4. Comparing current metrics with baseline performance from last week"
```

**Expected Outcome**: Specific root cause identification with supporting data

#### Step 3: Immediate Mitigation (4 minutes)
```bash
q chat "Implement immediate mitigation by:
1. Creating emergency rollback plan for recent deployment
2. Scaling up AWS resources to handle current load
3. Implementing circuit breaker patterns for failing services
4. Setting up enhanced monitoring for ongoing incident tracking"
```

**Expected Outcome**: Actionable mitigation steps with implementation commands

#### Step 4: Documentation and Prevention (3 minutes)
```bash
q chat "Create post-incident documentation by:
1. Generating incident timeline with key events and decisions
2. Creating runbook updates for similar future incidents
3. Recommending infrastructure improvements to prevent recurrence
4. Updating GitLab CI/CD pipeline with additional safety checks"
```

**Expected Outcome**: Complete incident documentation and prevention recommendations

### Key Demonstration Points:
- **Multi-MCP Orchestration**: CloudWatch + GitHub + AWS tools working together
- **Context Preservation**: Information flows between different analysis steps
- **Intelligent Correlation**: Connecting deployment events with performance issues
- **Actionable Outputs**: Specific commands and procedures, not just analysis

---

## 🚀 Scenario B: "New Feature Deployment"
**Duration**: 20 minutes  
**Demonstrates**: Complete SDLC workflow, multi-cloud strategy, security integration

### Setup Context:
```bash
# New photo upload feature for existing API
# Currently deployed on GCP, expanding to AWS
# Need security scanning and performance validation
# GitLab CI/CD integration required
```

### Demo Flow:

#### Step 1: Architecture Planning (5 minutes)
```bash
q chat "As a principal engineer planning a new photo upload feature, design architecture that:
1. Extends our current GCP Cloud Storage setup to include AWS S3
2. Implements image processing using AWS Lambda alongside our GCP Cloud Functions
3. Maintains our GitLab CI/CD workflows for both cloud deployments
4. Includes cost optimization and performance benchmarking
5. Ensures GDPR compliance across both platforms"
```

**Expected Outcome**: Multi-cloud architecture diagram with implementation roadmap

#### Step 2: Code Generation (5 minutes)
```bash
q chat "Generate production-ready code for the photo upload feature:
1. Create AWS Lambda function for image processing with error handling
2. Implement S3 integration with proper security policies
3. Add CloudWatch monitoring and alerting
4. Include unit tests covering edge cases and error scenarios
5. Generate AWS CDK infrastructure code matching our patterns"
```

**Expected Outcome**: Complete, deployable code with infrastructure definitions

#### Step 3: Security and Testing (5 minutes)
```bash
q chat "Implement comprehensive security and testing by:
1. Scanning the generated code for security vulnerabilities
2. Creating integration tests for AWS services
3. Setting up performance benchmarks against our GCP baseline
4. Implementing security policies for S3 bucket access
5. Generating load testing scenarios for the new feature"
```

**Expected Outcome**: Security-validated code with comprehensive test suite

#### Step 4: Deployment and Monitoring (5 minutes)
```bash
q chat "Deploy the feature with proper monitoring by:
1. Creating GitLab CI/CD pipeline stages for AWS deployment
2. Setting up blue-green deployment with automatic rollback
3. Configuring CloudWatch dashboards and alerts
4. Implementing cross-cloud monitoring between GCP and AWS
5. Creating operational runbooks for the new feature"
```

**Expected Outcome**: Deployed feature with comprehensive monitoring and operational procedures

### Key Demonstration Points:
- **End-to-End SDLC**: From planning through deployment and monitoring
- **Multi-Cloud Intelligence**: Seamless integration between GCP and AWS
- **Security Integration**: Built-in security scanning and policy enforcement
- **GitLab Workflow Respect**: Enhancing existing workflows rather than replacing

---

## 💰 Scenario C: "Cost Optimization Discovery"
**Duration**: 15 minutes  
**Demonstrates**: Cross-cloud cost analysis, intelligent optimization, automated implementation

### Setup Context:
```bash
# Monthly cloud costs increasing beyond budget
# Using both GCP and AWS services
# Need optimization without performance impact
# Require implementation roadmap
```

### Demo Flow:

#### Step 1: Cost Analysis (4 minutes)
```bash
q chat "As a platform engineer managing multi-cloud costs, analyze our spending by:
1. Reviewing AWS cost data for the last 3 months by service
2. Identifying cost trends and usage patterns
3. Comparing AWS costs with equivalent GCP services
4. Highlighting the top 5 cost drivers and optimization opportunities
5. Estimating potential savings from right-sizing and optimization"
```

**Expected Outcome**: Comprehensive cost analysis with specific optimization opportunities

#### Step 2: Optimization Recommendations (4 minutes)
```bash
q chat "Generate specific optimization recommendations by:
1. Analyzing EC2 instance utilization and right-sizing opportunities
2. Reviewing S3 storage classes and lifecycle policies
3. Identifying unused or underutilized resources
4. Recommending Reserved Instance purchases based on usage patterns
5. Suggesting architectural changes for cost efficiency"
```

**Expected Outcome**: Prioritized list of optimization actions with estimated savings

#### Step 3: Implementation Planning (4 minutes)
```bash
q chat "Create implementation plan for cost optimizations by:
1. Prioritizing optimizations by impact and implementation complexity
2. Generating scripts for automated resource right-sizing
3. Creating S3 lifecycle policies and storage class transitions
4. Planning Reserved Instance purchases with ROI analysis
5. Scheduling optimization activities to minimize service disruption"
```

**Expected Outcome**: Detailed implementation plan with automation scripts

#### Step 4: Monitoring and Governance (3 minutes)
```bash
q chat "Establish ongoing cost governance by:
1. Setting up AWS Budget alerts and cost anomaly detection
2. Creating cost optimization dashboards for stakeholders
3. Implementing automated policies for resource tagging and lifecycle
4. Generating monthly cost reports with optimization recommendations
5. Creating cost review processes for new deployments"
```

**Expected Outcome**: Automated cost governance framework with ongoing monitoring

### Key Demonstration Points:
- **Data-Driven Decisions**: Real cost data analysis with specific recommendations
- **Automated Implementation**: Scripts and policies for hands-off optimization
- **Cross-Cloud Intelligence**: Comparing costs and efficiency across platforms
- **Governance Integration**: Building optimization into ongoing processes

---

## 🎭 Demo Execution Guidelines

### Pre-Demo Preparation:
```bash
# Ensure realistic demo data
- AWS account with actual resources and costs
- CloudWatch logs with real error patterns
- GitHub repository with recent commits
- Cost data spanning multiple months
```

### During Demo Execution:

#### Timing Management:
- **Scenario A**: 15 minutes (incident response)
- **Scenario B**: 20 minutes (feature deployment)  
- **Scenario C**: 15 minutes (cost optimization)
- **Buffer**: 10 minutes for questions and transitions

#### Audience Engagement:
- Ask: "How would you typically handle this situation?"
- Highlight: "Notice how this compares to your current workflow"
- Emphasize: "This maintains your existing GitLab patterns"

#### Technical Demonstration:
- Show actual commands and responses
- Highlight MCP server orchestration
- Demonstrate context preservation
- Emphasize practical, actionable outputs

### Fallback Strategies:

#### If MCP Servers Fail:
- Use pre-recorded command outputs
- Explain what would normally happen
- Focus on prompting techniques and patterns

#### If AWS Services Are Slow:
- Switch to cached examples
- Demonstrate with sample data
- Emphasize the approach over specific results

#### If Audience Questions Derail Timing:
- Acknowledge questions and defer detailed answers
- Provide follow-up resources
- Stay focused on demonstration objectives

## 🎯 Success Metrics

### Immediate Indicators:
- Audience asking specific technical questions
- Requests to see particular use cases
- Discussion about integration with current tools
- Questions about enterprise features and security

### Engagement Signals:
- Note-taking during demonstrations
- Questions about implementation details
- Requests for follow-up meetings
- Interest in trial or POC access

### Follow-up Opportunities:
- Requests for team demonstrations
- Questions about training and enablement
- Discussion about enterprise support
- Interest in specific MCP integrations

---

**Next Step**: Review `demo-assessment.md` for evaluation criteria and completion requirements.