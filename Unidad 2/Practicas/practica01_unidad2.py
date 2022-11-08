"""
Descripción de la API: Es acerca de la nutrición de los establecimientos
Autor: Castillo Aviles Jessica
Fecha de creación: 08 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""***********************************
Nombre de la API: Nutritionix Appi
Descripción de la API: Acerca de la nutrición de los establecimientos
API Portal / Home Page: https://developer.nutritionix.com/?ref=apilist.fun
***********************************"""
'''Importar módulos existentes para agregar funcionalidad adicional.'''
import urllib.parse
import requests


main_api = "https://api.nutritionix.com/v1_1/search/mcdonalds?results=0:20&fields=item_name,brand_name,item_id,nf_calories&appId=a1a2c541&appKey=2da8c2b4acd6402730b3ebb16eb0bba3"
appId = "a1a2c541"
appKey ="2da8c2b4acd6402730b3ebb16eb0bba3"


while True:
     #ciclo para que en cuanto el usuario agregue un "salir" o "s" se termine el ciclo
    orig = input("Starting Location: ")
    if orig == "salir" or orig == "s":
        break
    dest = input("Destination: ")
    if dest == "salir" or dest == "s":
        break

    url = main_api + urllib.parse.urlencode({"id": appId, "key":appKey, "from":orig, "to":dest})
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
