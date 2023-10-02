'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 25 septiempre 2023
Descripcion: Laboratorio 3.1.1.11
'''
income = float(input("Introduce el ingreso anual:"))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = max(0, tax)
tax = round(tax)

print("El impuesto es:", tax, "pesos")