'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 2 Octubre 2023
Descripcion: Prob1
'''

def calculo(cantidad):
    if cantidad <= 0:
        return "La cantidad que introdujo es incorrecta, tiene que ser positiva."
    if cantidad <= 10000:
        impuesto = cantidad * 0.05
    elif cantidad <= 20000:
        impuesto = cantidad * 0.15
    elif cantidad <= 35000:
        impuesto = cantidad * 0.20
    elif cantidad <= 60000:
        impuesto = cantidad * 0.30
    else:
        impuesto = cantidad * 0.45
    return impuesto

cantidad = float(input("Ingrese la cantidad: "))
impuesto = calculo(cantidad)
print(f"El impuesto calculado es: {impuesto}")
