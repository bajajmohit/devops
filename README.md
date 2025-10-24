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
