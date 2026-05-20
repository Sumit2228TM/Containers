'''
The given script is used to perform update (PUT) operation on Containers -
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


update_size_normally = session.put(f"{BASE_URL}/storage-containers/38061",json={
    "name":"Sample Container updated (F-1)",
    "typeName":"-80 freezer 1",
    "siteName":"Sumit Site A",
    "noOfRows":3,
    "noOfColumns":5,
})

if update_size_normally.status_code == 200:
    print("Successfull update")
else:
    print("Failed to update details")
    print(f"Error Details:{update_size_normally.text}")
    exit()
    
'''
Output -

Auth Successful
Successfull update

'''

    
'''
If you pass only the attributes you want to update it will fail as PUT needs all mandatory attributes

Failed to update details

Error Details:

[{"code":"STORAGE_CONTAINER_NAME_REQUIRED","message":"Storage container name is required."},
{"code":"STORAGE_CONTAINER_REQUIRED_SITE_OR_PARENT_CONT","message":"Site or parent container detail is required."}]

'''
