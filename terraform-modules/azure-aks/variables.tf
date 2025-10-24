variable "resource_group_name" {
  description = "Name of the resource group."
  type        = string
}

variable "location" {
  description = "Azure region."
  type        = string
  default     = "eastus"
}

variable "cluster_name" {
  description = "AKS cluster name."
  type        = string
}

variable "node_count" {
  description = "Number of nodes in the default pool."
  type        = number
  default     = 2
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "dev"
}
