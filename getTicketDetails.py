import requests
from requests.auth import HTTPBasicAuth

'''
This module retrieves the EPIC ID information from ADO. 

In order to retrieve the data, the module requires the 
CORE_ID, TOEKN, Project, and expansion options to properly 
execute.
'''

def get_ticket_details(cid,CORE_ID,TOKEN,ORG_URL,PROJECT,EXPAND_OPT,API_VERSION):
    headers     = {'Content_Type': 'application/json'}
    auth        = HTTPBasicAuth(CORE_ID, TOKEN)

    try:
        url=f'{ORG_URL}/{PROJECT}/_apis/wit/workitems?ids={str(cid)}&expand={EXPAND_OPT}&api-version={API_VERSION}'
        return requests.get(url, headers=headers, auth=auth).json()
    except Exception as e:
       print(f"There was an exception in '{get_ticket_details.__module__}' : ", e)