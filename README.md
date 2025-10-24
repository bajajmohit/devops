# ☁️ Azure AKS Terraform Module

This module deploys a secure and production-ready Azure Kubernetes Service (AKS) cluster with:
- System-assigned managed identity  
- Configurable node pool  
- Tagging and environment separation  

### 🔧 Usage Example
```hcl
module "aks" {
  source              = "github.com/bajajmohit/terraform-modules//azure-aks"
  cluster_name        = "aks-demo-dev"
  resource_group_name = "rg-demo-dev"
  location            = "eastus"
  node_count          = 2
}

# ⚙️ GitHub Actions CI/CD Pipelines

A collection of reusable workflows to improve DevOps automation.

### 🧠 Included Pipelines
- **CodeQL Security Scan** – Detect code vulnerabilities.
- **Trivy Scan** – Container vulnerability scanning.
- **Helm Deployment** – Deploy microservices to AKS or EKS.

Use `workflow_call` to import these templates into your own pipelines.

# 🐳 Kubernetes Examples

Collection of Kubernetes deployment and security examples.

### 📦 Includes
- **Blue-Green Deployments** – Controlled rollout using Helm
- **Pod SecurityContext** – Enforcing least privilege containers
- **Liveness & Readiness Probes**

Each folder contains practical manifests to test secure and resilient deployments.

# 🤖 Python Automation Scripts

A set of lightweight automation tools for cloud governance and DevOps tasks.

### Scripts
- `azure-role-cleanup.py` → Detects orphaned Azure role assignments
- `job-scraper-devops.py` → Fetches DevOps jobs from job portals
- `cost-anomaly-alert.py` → Monitors Azure cost anomaly alerts

All scripts are self-contained and use Python standard libraries + REST APIs.
