#Autor: Jessica Quetzali Castillo Aviles
#DEscripción: Add User Input for Address
#25 octubre 2022

import urllib.parse
import requests

#Crear variables para la API REQUEST
main_api = "http://www.mapquestapi.com/directions/v2/route?key=je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY&from=Clarendon%20Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA"
key  = "je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY"


# The "while true" construct creates an endless loop.
while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

    #Cree una instrucción if que imprima el estado de la 
    #solicitud si la clave del código de estado se establece en el valor 0

    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       