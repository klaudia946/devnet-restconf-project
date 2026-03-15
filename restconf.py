import requests
import json

url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Content-Type": "application/yang-data+json"
}

auth = ("developer", "C1sco12345")

data = {
 "ietf-interfaces:interface": [
  {
   "name": "Loopback100",
   "type": "iana-if-type:softwareLoopback",
   "enabled": True,
   "ietf-ip:ipv4": {
    "address": [
     {
      "ip": "10.100.100.1",
      "netmask": "255.255.255.0"
     }
    ]
   }
  }
 ]
}

response = requests.post(
    url,
    headers=headers,
    auth=auth,
    data=json.dumps(data),
    verify=False
)

print(response.status_code)
print(response.text)

