#Autor: Jessica Quetzali Castillo Aviles
#DEscripción: Extracción de datos
#25 octubre 2022
# je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY

'''Importar módulos existentes para agregar funcionalidad adicional.'''
import urllib.parse
import requests

#Crear variables para la API REQUEST
main_api = "http://www.mapquestapi.com/directions/v2/route?key=je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY&from=Clarendon%20Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA"
orig = "Washington"
dest = "Baltimaore"
key  = "je9lRmco1yvS0pmm3gDpt3Rcs77LdgBY"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

#Usar el metodo get para solicitar datos de la direccion enviada
json_data = requests.get(url).json()
print(json_data) 


