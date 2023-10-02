'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 1 Octubre 2023
Descripcion: Laboratorio 3.2.1.10
'''

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()  # Esto convierte la palabra a mayúsculas

for palabra in user_word:
    if palabra in "AEIOU":
        continue  
    print(palabra)
