"""
Descripción de la API: Generación de nuevas appis
Autor: Castillo Aviles Jessica
Fecha de creación: 08 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""***********************************
Nombre de la API: Newsapi
Descripción de la API: Generación de nuevas apis
API Portal / Home Page: https://newsapi.org/?ref=apilist.fun
***********************************"""

import urllib.parse
import requests


main_api = "https://newsapi.org/v2/everything?q=Apple&from=2022-11-08&sortBy=popularity&apiKey=5b94ced77f8c4b43b1ba1e18b8ebd487"
key ="5b94ced77f8c4b43b1ba1e18b8ebd487"


while True:
     #ciclo para que en cuanto el usuario agregue un "salir" o "s" se termine el ciclo
    orig = input("Starting Location: ")
    if orig == "salir" or orig == "s":
        break
    dest = input("Destination: ")
    if dest == "salir" or dest == "s":
        break

    url = main_api + urllib.parse.urlencode({ "key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    #declaraciones de impresión que muestran las ubicaciones de origen y destino, etc.
    if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("Directions from " + (orig) + " to " + (dest))
       print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
       print("=============================================")

    #Las entradas de usuario no válidas son solo un tipo de error.
    else:
       print("************************************************************************")
       print("For Staus Code: " + str(json_status) + ", Refer to:")
       print("https://developer.mapquest.com/documentation/directions-api/status-codes")
       print("************************************************************************\n")
