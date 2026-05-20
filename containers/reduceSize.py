'''
The given script is used to perform update (PUT) operation on containers to reducing the dimensions of it -
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

update_size_reduce = session.put(f"{BASE_URL}/storage-containers/65050",json={
    "name":"SSA.F2.S1",
    "typeName":"-20shelf_1x4",
    "siteName":"Sumit Site A",
    "noOfRows":1,
    "noOfColumns":2,
})

if update_size_reduce.status_code == 200:
    print("Successfull update")
else:
    print("Failed to update details")
    print(f"Error Details:{update_size_reduce.text}")
    exit()
    
'''    

Output - 

Failed to update details
Error Details:[{"code":"STORAGE_CONTAINER_CANNOT_SHRINK_CONTAINER","message":"Storage container capacity can not be reduced."}]

'''