#Autor: Jessica Quetzali Castillo Aviles
#DEscripción: Check for Invalid User Input
#25 octubre 2022

import urllib.parse
import requests

#Crear variables para la API REQUEST
main_api = "http://www.mapquestapi.com/directions/v2/route?key=je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY&from=Clarendon%20Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA"
key  = "je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY"

# The "while true" construct creates an endless loop.
while True:
     #ciclo para que en cuanto el usuario agregue un "quit" o "q" se termine el ciclo
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    #declaraciones de impresión que muestran las ubicaciones de origen y destino, etc.
    if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("Directions from " + (orig) + " to " + (dest))
       print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
       print("Miles:           " + str(json_data["route"]["distance"]))
       print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"])) 
       print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
       print("=============================================")

       #el bucle for itera a través de cada lista de maniobras, imprime la descripción 
        # e imprime la distancia en kilómetros con formato de 2 decimales.
       for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
       print("=============================================\n")
    #para responder al usuario cuando json_status no es igual a 0.   
    elif json_status == 402:
       print("**********************************************")
       print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
       print("**********************************************\n")
       print("=============================================")
    #Las entradas de usuario no válidas son solo un tipo de error.
    else:
       print("************************************************************************")
       print("For Staus Code: " + str(json_status) + ", Refer to:")
       print("https://developer.mapquest.com/documentation/directions-api/status-codes")
       print("************************************************************************\n")