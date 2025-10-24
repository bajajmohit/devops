from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient

subscription_id = "<your-subscription-id>"
client = AuthorizationManagementClient(DefaultAzureCredential(), subscription_id)

print("Scanning for orphaned role assignments...")
for role in client.role_assignments.list():
    if not role.principal_id:
        print(f"⚠️ Orphaned role assignment found: {role.name}")
