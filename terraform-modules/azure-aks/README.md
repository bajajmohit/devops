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