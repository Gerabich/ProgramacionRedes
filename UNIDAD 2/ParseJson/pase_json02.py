'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 23 de octubre 2023
Descripcion: Invocando REST API MapQuest
'''
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Ocote"
dest = "San Miguel de allende"
key = "X9btyYVwX5x7N14HjBm9E3jCURxVIc9S"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
#Codificar para manejar el error distinto a 0
else:
    print("API Status: " + str(json_status) + " = Tienes un error, Verifica tu code.")

