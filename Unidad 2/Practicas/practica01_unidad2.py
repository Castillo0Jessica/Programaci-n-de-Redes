"""
Descripción de la API: Es acerca de la variedad de alimentos y el id que tienen en el establecimiento
Autor: Castillo Aviles Jessica
Fecha de creación: 08 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""***********************************
Nombre de la API: Nutritionix Appi
Descripción de la API: Acerca de los alimentos de los establecimientos
API Portal / Home Page: https://developer.nutritionix.com/?ref=apilist.fun
***********************************"""
'''Importar módulos existentes para agregar funcionalidad adicional.'''
import urllib.parse
import requests


main_api = "https://api.nutritionix.com/v1_1/search/mcdonalds?"
appId = "a1a2c541"
appKey ="2da8c2b4acd6402730b3ebb16eb0bba3"
q="Starbucks Frappuccino"


while True:
    #ciclo para que en cuanto el usuario agregue un "salir" o "s" se termine el ciclo
    ali= input("Alimento: ")
    if ali == "salir" or ali == "s":
        break
  

    url = main_api + urllib.parse.urlencode({"q":q,"search": ali,"appId": appId, "appKey":appKey})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data['hits'][0]["fields"]["item_name"]
    

    for elem in json_data["hits"]:
        if ali in elem["fields"]["item_name"]:
            print("Alimento: " + str(elem["fields"]["item_name"]) )
            print("ID:   " + str(elem["_id"]))
            print("Brand name:   " + str(elem["fields"]["brand_name"]))
    


    


    
    
