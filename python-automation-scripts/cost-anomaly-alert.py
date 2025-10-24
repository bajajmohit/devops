import requests
import os

tenant_id = os.getenv("AZURE_TENANT_ID")
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

print(f"Checking cost anomaly alerts for subscription: {subscription_id}")
# Demo endpoint (replace with Azure Cost Management API in production)
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())
