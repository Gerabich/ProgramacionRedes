'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 3 noviembre 2023
Descripcion: api 3
'''
import requests

url = 'https://the-mexican-food-db.p.rapidapi.com/4'
headers = {
    'X-RapidAPI-Key': '096cb21923mshdca5fb2e3286a06p12267ajsn27888e4f8ddc',
    'X-RapidAPI-Host': 'the-mexican-food-db.p.rapidapi.com'
}

while True:
    user_input = input("Presiona Enter para obtener datos o escribe 'Salir' (S) para terminar: ")
    
    if user_input.lower() == 'salir' or user_input.lower() == 's':
        print("Saliendo del programa.")
        break
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
