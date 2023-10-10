'''
 Nombre: Gerardo Antonio Garcia Vazquez
 Fecha: 08 de Octubre de 2023 
 Description: Laboratorio: 4.3.1.10
'''
def liters_100km_to_miles_gallon(liters):
    return 100 / (liters / 3.785411784 * 0.621371)

def miles_gallon_to_liters_100km(miles):
    return 100 / (miles * 1.609344 / 3.785411784)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))