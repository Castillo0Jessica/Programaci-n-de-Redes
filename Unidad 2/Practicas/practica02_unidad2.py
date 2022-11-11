"""
Descripción de la API: Detección de articulos con sus titulos y autores correspondientes
Autor: Castillo Aviles Jessica
Fecha de creación: 08 de noviembre 2022
""" 
#DESCRIPCIÓN DE LA API
"""***********************************
Nombre de la API: Newsapi
Descripción de la API: Búsqueda de articulos con su información correspondiente
API Portal / Home Page: https://newsapi.org/?ref=apilist.fun
***********************************"""

import urllib.parse
import requests


main_api = "https://newsapi.org/v2/everything?"
key ="5b94ced77f8c4b43b1ba1e18b8ebd487"
#q= "Apple"
#orig ="2022-11-10"
#sortBy = "popularity"


while True:
     #ciclo para que en cuanto el usuario agregue un "salir" o "s" se termine el ciclo
    q= input("Tittle: ")
    if q == "salir" or q == "s":
        break
    orig= input("Autor: ")
    if orig == "salir" or orig == "s":
        break

    url = main_api + urllib.parse.urlencode({ "q":q, "apiKey":key, "from":orig})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["articles"][0]["title"]
    
   # print(json_status)

    #declaraciones de impresión que muestran los articulos, etc.
    if json_status == q or json_status == orig:
       print ("********************************************")
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("Articulo: " + (q) )
       print("Autor: "+ (orig))
       print("Description:   " + str(json_data["articles"][0]["description"]))
       print("Publicación:   " + str(json_data["articles"][0]["publishedAt"]))
       print("**********************************************")
    else:
       print("**********************************************")
       print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
       print("**********************************************\n")
       print("=============================================")