'''
The given script is used to perform update (PATCH) operation on containers -
'''

import requests
import json

BASE_URL   = "https://test.openspecimen.org/rest/ng"
LOGIN_NAME = ""
PASSWORD   = ""
DOMAIN     = "openspecimen"

session = requests.Session()
session.headers.update({"Content-Type": "application/json"})

auth_response = session.post(f"{BASE_URL}/sessions", json={ 
    "loginName": LOGIN_NAME,
    "password":  PASSWORD,
    "domain":    DOMAIN
})
    
auth = auth_response.json()
session.headers.update({"X-OS-API-TOKEN": auth["token"]})

if auth_response.status_code == 200:
    print("Auth Successful")
else:
    print("Unauth Access")
    exit()
    
patch_update = session.patch(f"{BASE_URL}/storage-containers/38061",json={
    "noOfRows":3
})

if patch_update.status_code == 200:
    print("Successfull patch")
else:
    print("Failed to Patch")
    print(f"Error Deatils:{patch_update.text}")
    exit()
    
    
'''
Output - 

Auth Successful
Successfull patch

'''

'''
Here in PATCH even if we pass only the attributes we need to update it gets updated without any error
'''
