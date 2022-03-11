from azure.identity import ClientSecretCredential
import sys
import importlib.util
#from azure.mgmt.compute import ComputeManagementClient

import validate

def azure_auth():

        az_tenantId="583092bd-822c-4643-95c0-3e136d466ad6"
        az_clientId="bf76b7eb-b6a4-4cb5-aa55-b12cdd722133"
        az_clientSecret="jFt7Q~iqls4XXHD6WmXFvNwNJ4.EOhaabRLRE"
       
        credentials = ClientSecretCredential(tenant_id=az_tenantId, client_id=az_clientId, client_secret=az_clientSecret)
        return credentials

if __name__ == "__main__":

        #print(sys.modules)   
        #rsmod = importlib.reload(validate)
        if validate not in sys.modules:
                rsmod = importlib.import_module("validate")
        else:
                rsmod = importlib.reload(validate)

        azure_cred=azure_auth()
        azure_subId="2632f927-9a84-4894-a874-22fff67804aa"
        result=validate.start_tests(azure_cred, azure_subId,"")