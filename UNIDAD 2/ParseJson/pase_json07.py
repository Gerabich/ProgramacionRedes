'''
    Descripcion: Consumiendo API con python
    Autor: Gerardo Antonio Garcia Vazquez  
    Fecha: 20 de ocutubre 2023
'''

import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
   #Agregar condicion para dest
   #un mensaje hasta luego
    if dest == "quit" or dest == "q":
      break
    print("Hasta luego ")
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "X9btyYVwX5x7N14HjBm9E3jCURxVIc9S"
    
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()

    #imprimir la URL
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
      print("API Status: " + str(json_status) + " = A successful route call.\n")
      print("=============================================")
      print("Directions from " + (orig) + " to " + (dest))
      print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
      print("Miles:           " + str(json_data["route"]["distance"]))
      #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
      print("=============================================")
      print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
      print("=============================================")
      for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
      print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")