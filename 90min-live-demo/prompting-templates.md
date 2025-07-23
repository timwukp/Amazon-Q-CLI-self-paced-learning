# Advanced Prompting Templates for Amazon Q CLI Demo

**Structured prompting patterns for consistent, high-quality demonstrations**

## 🎯 Overview

This guide provides the specific prompting templates and patterns used in the 90-minute Amazon Q CLI demonstration, designed for principal engineers familiar with Cursor, GitLab, and GCP.

## 🧠 Global Prompting Rules

These rules are applied consistently throughout the demonstration:

### Rule 1: Context-Aware Prompting
```bash
# Pattern
"Given my current [CONTEXT] and [ENVIRONMENT], [specific request]"

# Examples
"Given my current GCP Cloud Functions setup and GitLab CI/CD workflows, create equivalent AWS Lambda architecture"
"Given my current project structure and AWS environment, optimize my deployment pipeline"
```

### Rule 2: Role-Based Prompting
```bash
# Pattern
"As a [ROLE] with [EXPERTISE], [action] considering [CONSTRAINTS]"

# Examples
"As a principal engineer familiar with GCP, design AWS architecture considering our team's current expertise"
"As a senior software engineer, refactor this code considering security, performance, and maintainability"
```

### Rule 3: Constraint-Driven Prompting
```bash
# Pattern
"[Request] with the following constraints: [CONSTRAINT1], [CONSTRAINT2], [CONSTRAINT3]"

# Examples
"Create serverless API with constraints: budget under $200/month, sub-200ms response time, GDPR compliant"
"Deploy application with constraints: maintain GitLab workflows, zero downtime, multi-region support"
```

### Rule 4: Multi-Step Prompting
```bash
# Pattern
"First analyze [X], then recommend [Y], finally implement [Z] with [CONSIDERATIONS]"

# Examples
"First analyze my GCP usage patterns, then recommend AWS equivalents, finally implement migration strategy with cost optimization"
"First review security implications, then suggest improvements, finally generate implementation with proper error handling"
```

## 📋 Section-Specific Templates

### PLAN Phase Templates

#### Architecture Planning Template
```bash
# Template: GCP_TO_AWS_ARCHITECTURE
q chat "As a principal engineer experienced with [GCP_SERVICES], help me design AWS architecture for [PROJECT_TYPE] by:
1. Mapping my current GCP services to optimal AWS equivalents
2. Explaining key differences and advantages of each AWS service
3. Estimating costs compared to my current GCP spend of [BUDGET]
4. Identifying migration strategies that minimize risk and downtime
5. Providing implementation roadmap with milestones
Context: Current setup uses [CURRENT_STACK], team expertise in [SKILLS], compliance needs [REQUIREMENTS]"

# Live Demo Example
q chat "As a principal engineer experienced with GCP Cloud Run, Cloud Storage, and Cloud SQL, help me design AWS architecture for a photo-sharing API by:
1. Mapping my current GCP services to optimal AWS equivalents
2. Explaining key differences and advantages of each AWS service  
3. Estimating costs compared to my current GCP spend of $150/month
4. Identifying migration strategies that minimize risk and downtime
5. Providing implementation roadmap with milestones
Context: Current setup uses Node.js microservices, team expertise in containerization, GDPR compliance required"
```

#### Project Structure Template
```bash
# Template: PROJECT_SCAFFOLDING
q chat "Given my GitHub organization's existing repositories and our established patterns, create a [PROJECT_TYPE] project structure that:
- Integrates with our current GitLab CI/CD workflows
- Uses our established AWS account structure and naming conventions
- Follows our team's coding standards from recent commits
- Includes proper documentation and testing frameworks
- Estimates resource costs based on our current usage patterns"
```

### CODE Phase Templates

#### Intelligent Code Generation Template
```bash
# Template: CURSOR_STYLE_CODING
q chat "As a senior developer familiar with [TECH_STACK] and experienced with Cursor AI assistance, create [COMPONENT] that:
- Follows our established coding standards and patterns
- Includes comprehensive error handling and logging
- Implements [SECURITY_PATTERN] for authentication/authorization
- Optimizes for [PERFORMANCE_METRIC] performance requirements
- Includes proper monitoring hooks and health checks
- Maintains compatibility with our existing [INTEGRATION_POINTS]"

# Live Demo Example
q chat "As a senior developer familiar with Node.js and experienced with Cursor AI assistance, create a Lambda function for image processing that:
- Follows our established coding standards and patterns
- Includes comprehensive error handling and logging
- Implements JWT authentication for API security
- Optimizes for sub-200ms response time requirements
- Includes proper CloudWatch monitoring hooks and health checks
- Maintains compatibility with our existing S3 and RDS integrations"
```

#### GCP-to-AWS Translation Template
```bash
# Template: SERVICE_TRANSLATION
q chat "I currently use [GCP_SERVICE] with [CONFIGURATION]. Create equivalent AWS implementation that:
- Maintains the same API contract and behavior
- Uses AWS best practices and native services
- Provides cost optimization opportunities
- Includes migration strategy with minimal downtime
- Explains key differences and new capabilities available"
```

### BUILD Phase Templates

#### GitLab CI/CD Enhancement Template
```bash
# Template: GITLAB_AWS_INTEGRATION
q chat "As a DevOps engineer using GitLab CI/CD, enhance my pipeline by:
1. Analyzing my existing .gitlab-ci.yml configuration
2. Adding AWS deployment stages that complement my current GCP deployments
3. Implementing AWS security scanning equivalent to my GCP security checks
4. Creating environment promotion workflows for both clouds
5. Optimizing build times with AWS-specific caching strategies
6. Generating comprehensive deployment documentation"
```

#### Build Optimization Template
```bash
# Template: MULTI_CLOUD_BUILD_OPTIMIZATION
q chat "Review my build process and optimize for multi-cloud deployment by:
- Analyzing current build performance metrics from GitLab
- Identifying dependency bottlenecks affecting deployment speed
- Recommending AWS-specific caching and optimization strategies
- Creating parallel build strategies for AWS and GCP
- Setting up security scanning integration for both platforms
- Generating updated CI/CD configuration with best practices"
```

### TEST Phase Templates

#### Comprehensive Testing Template
```bash
# Template: MULTI_CLOUD_TESTING
q chat "As a QA engineer with GCP testing experience, create comprehensive AWS test suite that:
- Covers [COVERAGE_PERCENTAGE]% of code paths with realistic edge cases
- Includes performance benchmarks comparing AWS vs GCP response times
- Mocks AWS services properly (S3, Lambda, RDS) equivalent to GCP mocks
- Generates load testing scenarios for AWS infrastructure scaling
- Includes security test cases for AWS IAM and resource policies
- Provides cross-cloud integration testing strategies"
```

#### Production-Based Testing Template
```bash
# Template: PRODUCTION_INFORMED_TESTING
q chat "Based on my production CloudWatch logs and error patterns, create tests that:
- Cover the failure scenarios I've seen in production
- Include edge cases from actual user behavior
- Test performance under realistic load conditions
- Validate error handling for common failure modes
- Include security tests for vulnerabilities found in audits
- Generate automated regression tests for critical paths"
```

### REVIEW Phase Templates

#### Multi-Cloud Code Review Template
```bash
# Template: INTELLIGENT_CODE_REVIEW
q chat "As a senior code reviewer experienced with both GCP and AWS, analyze this infrastructure code for:
- Security vulnerabilities using AWS Security Best Practices
- Performance implications compared to equivalent GCP services
- Code quality and maintainability standards
- Compliance with [COMPLIANCE_FRAMEWORK] requirements
- Integration risks with existing GCP services during migration
- Cost optimization opportunities and recommendations
- Generate specific, actionable review comments with examples"
```

#### Documentation Generation Template
```bash
# Template: MIGRATION_DOCUMENTATION
q chat "As a technical writer documenting cloud migration, generate documentation that:
- Explains AWS services for teams familiar with GCP equivalents
- Includes practical examples comparing AWS and GCP implementations
- Covers troubleshooting scenarios specific to AWS services
- Follows our established documentation standards and templates
- Integrates with existing GitLab documentation repository
- Provides decision trees for service selection"
```

### DEPLOY Phase Templates

#### Multi-Cloud Deployment Template
```bash
# Template: PARALLEL_CLOUD_DEPLOYMENT
q chat "As a platform engineer managing multi-cloud infrastructure, deploy [APPLICATION] with:
- Blue-green deployment strategy using AWS CodeDeploy
- Monitoring and alerting via CloudWatch equivalent to our GCP setup
- Automated rollback mechanisms for Lambda and container services
- Security configurations for production AWS environment
- Cost optimization settings and budget alerts
- Cross-cloud failover and traffic routing strategies"
```

#### Infrastructure as Code Template
```bash
# Template: IAC_GENERATION
q chat "Create infrastructure as code that:
- Uses AWS CDK/CloudFormation based on our existing Terraform patterns
- Implements our established security and compliance policies
- Includes proper resource tagging and cost allocation
- Sets up monitoring and alerting equivalent to current setup
- Provides disaster recovery and backup strategies
- Generates deployment runbooks and operational procedures"
```

### MONITOR Phase Templates

#### Cross-Cloud Monitoring Template
```bash
# Template: UNIFIED_MONITORING
q chat "As an SRE managing multi-cloud infrastructure, create monitoring strategy that:
- Correlates AWS CloudWatch metrics with our existing GCP monitoring
- Identifies performance bottlenecks across both cloud platforms
- Provides unified alerting for our incident response team
- Generates cost optimization recommendations for both clouds
- Creates actionable dashboards for different stakeholder groups
- Implements intelligent anomaly detection and automated responses"
```

#### Incident Response Template
```bash
# Template: INTELLIGENT_INCIDENT_RESPONSE
q chat "As an incident commander responding to [INCIDENT_TYPE], help me:
1. Analyze CloudWatch logs and metrics for root cause identification
2. Correlate with recent deployments and configuration changes
3. Identify affected systems and estimate user impact
4. Implement immediate mitigation strategies
5. Create post-incident documentation and prevention recommendations
6. Generate runbook updates for similar future incidents"
```

## 🔄 MCP Integration Patterns

### Multi-Tool Orchestration Template
```bash
# Template: CROSS_PLATFORM_ORCHESTRATION
q chat "Orchestrate across platforms by:
1. Using GitHub MCP to analyze my repository for [CRITERIA]
2. Correlating with AWS MCP resource usage and cost data
3. Querying CloudWatch MCP for performance and error patterns
4. Generating comprehensive optimization plan with specific actions
5. Implementing changes across GitHub, AWS, and monitoring systems"
```

### Context-Aware MCP Usage
```bash
# Template: CONTEXTUAL_MCP_CHAIN
q chat "Given my current project context:
- Analyze my GitHub repository structure and recent changes
- Map to appropriate AWS services and estimate costs
- Set up CloudWatch monitoring based on application patterns
- Create documentation linking all components
- Generate deployment and maintenance procedures"
```

## 🎯 Demo-Specific Adaptations

### For Principal Engineers from GCP
```bash
# Emphasize familiar concepts
"This is similar to your GCP [SERVICE], but with these AWS advantages..."
"Using the same patterns you know from [GCP_PATTERN], but optimized for AWS..."
```

### For Cursor Users
```bash
# Highlight familiar interaction patterns
"Just like Cursor understands your code context, Q CLI understands your infrastructure context..."
"Same conversational approach you use in Cursor, but for cloud operations..."
```

### For GitLab Teams
```bash
# Respect existing workflows
"This enhances your existing GitLab workflows rather than replacing them..."
"Maintains your current GitLab CI/CD patterns while adding AWS capabilities..."
```

## 📊 Success Indicators

### Effective Prompting Results In:
- Specific, actionable responses
- Code that follows established patterns
- Architecture that respects constraints
- Documentation that matches team standards
- Solutions that integrate with existing tools

### Quality Metrics:
- Response relevance to context
- Technical accuracy and best practices
- Integration with existing workflows
- Cost-effectiveness of recommendations
- Security and compliance adherence

---

**Next Step**: Review `demo-scenarios.md` for specific demonstration scenarios using these templates.