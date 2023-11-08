'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 2 Octubre 2023
Descripcion: Laboratorio 3.1.1.12
'''
year = int(input("Introduce un año:"))

if year >= 1582:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Año Bisiesto")
    else:
        print("Año Común")
else:
    print("No dentro del período del calendario Gregoriano")
