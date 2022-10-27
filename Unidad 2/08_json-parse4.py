#Autor: Jessica Quetzali Castillo Aviles
#DEscripción: Agregar la funcionalidad de quit o q para salir del ciclo
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