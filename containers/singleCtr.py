'''
The given script is used to create a single container -
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


container = session.post(f"{BASE_URL}/storage-containers",json={
    "name":"Sumit -80Freezer",
    "siteName":"Sumit Site A",
    "noOfRows":4,
    "noOfColumns":1
})

if container.status_code == 200:
    print("Container Created")
else:
    print("Failed to create container")
    print(f"Error details: {container.text}")
    exit()
    
    
''' 
the script returns the following output  - 

Auth Successful
Container Created

'''
