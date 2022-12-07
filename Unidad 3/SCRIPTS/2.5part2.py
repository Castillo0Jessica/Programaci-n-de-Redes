import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback98"

headers = {
            "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          }
basicauth = ("developer", "C1sco12345")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback98",
        "description": "WHATEVER98",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "98.98.98.98",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))

    
