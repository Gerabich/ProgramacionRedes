'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 3 noviembre 2023
Descripcion: api 2
'''
import requests

url = 'https://text-translator2.p.rapidapi.com/translate'
headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'X-RapidAPI-Key': '096cb21923mshdca5fb2e3286a06p12267ajsn27888e4f8ddc',
    'X-RapidAPI-Host': 'text-translator2.p.rapidapi.com'
}

while True:
    source_language = input("Ingresa el idioma fuente (por ejemplo, 'en' para inglés): ")
    target_language = input("Ingresa el idioma de destino (por ejemplo, 'id' para indonesio): ")

    if source_language.lower() == 'salir' or target_language.lower() == 'salir':
        break

    text_to_translate = input("Ingresa el texto a traducir: ")

    data = {
        'source_language': source_language,
        'target_language': target_language,
        'text': text_to_translate
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        
        # Verificar si la respuesta tiene la clave 'translated_text'
        if 'translated_text' in response.json():
            translated_data = response.json()['translated_text']
            print("Texto traducido:", translated_data)
        else:
            print("Error: No se pudo obtener el texto traducido.")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
