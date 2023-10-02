'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 25 septiempre 2023
Descripcion: Laboratorio 3.1.1.11
'''

income = float(input("Introduce el ingreso anual:"))

#
# Escribe tu código aquí.
#

if income <= 85_528:
    tax= income * 0.18 -556.02
    
    

tax = round(tax, 0)
print("El impuesto es:", str(tax) , "pesos")
