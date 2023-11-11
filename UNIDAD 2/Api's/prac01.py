'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 3 noviembre 2023
Descripcion: api 1
'''

import requests
import requests

url = 'https://macrotrends-finance.p.rapidapi.com/quotes/history-price'

headers = {
    'X-RapidAPI-Key': '096cb21923mshdca5fb2e3286a06p12267ajsn27888e4f8ddc',
    'X-RapidAPI-Host': 'macrotrends-finance.p.rapidapi.com'
}

while True:
    symbol = input("Ingresa el símbolo (o escribe 'Salir' para terminar): ")

    if symbol.lower() == 'salir' or symbol.lower() == 's':
        break

    range_value = input("Ingresa el rango (por ejemplo, '1m' para 1 mes): ")

    params = {
        'symbol': symbol,
        'range': range_value
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

