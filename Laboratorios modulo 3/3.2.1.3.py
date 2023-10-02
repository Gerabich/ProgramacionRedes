'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 1 octubre 2023
Descripcion: Laboratorio 3.2.1.3
'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numbers = int(input("Ingresa el numero secreto: "))

while numbers != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numbers = int(input("Vuelve a intentarlo: "))

print(f"¡Bien hecho, muggle! El número secreto era {numbers}. Eres libre ahora.")
