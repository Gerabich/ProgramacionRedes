'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 23 de octubre 2023
Descripcion: Invocando REST API MapQuest
'''
import urllib.parse
import requests
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    print("Hasta luego")
    
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "X9btyYVwX5x7N14HjBm9E3jCURxVIc9S"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

