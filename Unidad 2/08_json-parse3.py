#Autor: Jessica Quetzali Castillo Aviles
#DEscripción: Print the URL and Check the Status of the JSON Request
#25 octubre 2022

import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?key=je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY&from=Clarendon%20Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA"
key  = "je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY"


# The "while true" construct creates an endless loop.
while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       