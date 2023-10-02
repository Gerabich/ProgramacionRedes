'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 2 Octubre 2023
Descripcion: Laboratorio 3.4.1.6
'''

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: Solicitar al usuario reemplazar el número de en medio.
numero_ingresado = int(input("Ingresa un número entero para reemplazar el número central: "))
hat_list[2] = numero_ingresado

# Paso 2: Eliminar el último elemento de la lista.
hat_list.pop()

# Paso 3: Imprimir la longitud de la lista existente.
print("La longitud de la lista es:", len(hat_list))

print(hat_list)
