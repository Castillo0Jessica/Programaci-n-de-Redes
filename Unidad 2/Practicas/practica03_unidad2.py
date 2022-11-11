"""
Descripción de la API: ES servicio para la creación de key y documentación
Autor: Castillo Aviles Jessica
Fecha de creación: 08 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""***********************************
Nombre de la API: OPENFDA
API Portal / Home Page: https://open.fda.gov/apis/authentication/
***********************************"""

import urllib.parse
import requests



main_api = "https://api.fda.gov/drug/event.json?"
api_key ="SBakUBm2jEFCtAwaLeQAzc8F398KYEdEWn9hcVo1"
search ="CANADA"




while True:
   #ciclo para que en cuanto el usuario agregue un "salir" o "s" se termine el ciclo
   search= input("LUGAR: ")
   if search== "salir" or search == "s":
      break

   url = main_api + urllib.parse.urlencode({"api_key":api_key, "search":search})
   print("URL: " + (url))
    
   json_data = requests.get(url).json()
   json_status = json_data["results"][0]["primarysource"]["reportercountry"]
   #print(json_status)
    

   for elem in json_data["results"]:
        if search in elem["primarysource"]["reportercountry"]:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("Receiptdate: "  + str(elem["receiptdate"]) )
            print("Companynumb: "+ (elem["companynumb"]))
            print("receiver:   " + str(elem["receiver"]))