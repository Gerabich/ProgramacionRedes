'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 2 Octubre 2023
Descripcion: Laboratorio 3.6.1.9
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Escribe tu código aquí.
unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("La lista con elementos únicos:")
print(unique_list)
