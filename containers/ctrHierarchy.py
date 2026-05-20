'''
The given script is used to create a container hierarchy -
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

hierarchy = session.post(f"{BASE_URL}/storage-containers/create-hierarchy",json={
    "names":[],
    "noOfRows":5,
    "noOfColumns":3,
    "numOfContainers": 1,
    "siteName":"Sumit Site A",
    "typeId":144,
    "usedFor":"STORAGE"
})

if hierarchy.status_code == 200:
    print("Container Hierarchy Created")
else:
    print("Failed to create container hierarchy")
    print(f"Error details: {hierarchy.text}")
    exit()

''' 
the script returns the following output  - 

Auth Successful
Container Hierarchy Created

'''