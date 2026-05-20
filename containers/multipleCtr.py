'''
The given script is used to create multiple containers -
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

multiple = session.post(f"{BASE_URL}/storage-containers/multiple",json=[
    {
        "name":"Sumit -20Freezer1",
        "noOfRows":2,
        "noOfColumns":2,
        "siteName":"Sumit Site A",
        "positionAssignment":"HZ_TOP_DOWN_RIGHT_LEFT",
        "typeID":83,
        "usedFor":"STORAGE"
    },
    {
        "name":"Sumit -20Freezer2",
        "noOfRows":2,
        "noOfColumns":2,
        "siteName":"Sumit Site A",
        "positionAssignment":"HZ_TOP_DOWN_RIGHT_LEFT",
        "typeID":83,
        "usedFor":"STORAGE"
    }
])

if multiple.status_code == 200:
    print("Multiple Containers Created")
else:
    print("Failed to create muliple containers")
    print(f"Error details: {multiple.text}")
    exit()

''' 
the script returns the following output  - 

Auth Successful
Multiple Containers Created

'''