'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 23 de octubre 2023
Descripcion: Invocando REST API MapQuest
'''
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimore"
key = "X9btyYVwX5x7N14HjBm9E3jCURxVIc9S"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data['route']['sessionId'])
#Extrae la distancia y tiempo
print(json_data['route']['distance'])
print(json_data['route']['time'])
#Extrae del primer elemento Legs el campo formattedTime
formatted_time = json_data['route']['legs'][0]['formattedTime']
print(formatted_time)

