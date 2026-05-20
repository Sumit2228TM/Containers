'''
The given script is used to perform update (PUT) operation on containers to increasing the dimensions of it -
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
    
update_size_increase = session.put(f"{BASE_URL}/storage-containers/38061",json={
    "name":"Sample Container (F-1)",
    "typeName":"-80 freezer",
    "siteName":"Sumit Site A",
    "noOfRows":5,
    "noOfColumns":2,
})

if update_size_increase.status_code == 200:
    print("Successfull update")
else:
    print("Failed to update details")
    print(f"Error Details:{update_size_increase.text}")
    exit()
    
'''
Output - 

Auth Successful
Successfull update

'''
