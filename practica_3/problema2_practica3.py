'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 9 octubre 2023
Descripcion: Problema 2 de la practica impar
'''
lstnombres = []
for i in range(5):
    nombre = input("Ingresa el nombre de algun amigo: ")
    lstnombres.append(nombre)

lstedades = []
for i in range(5):
    edad = input("Ingresa las edades de tus amigos: ")
    lstedades.append(edad)

dicDatos = {}
for i in range(5):
    dicDatos[lstnombres[i]] = lstedades[i]

def datos(diccionario):
    for nombre, edad in diccionario.items():
        print(f"{nombre} -> {edad}")

datos(dicDatos)
print("Longitud de lstnombres:", len(lstnombres))
print("Longitud de lstedades:", len(lstedades))
print("Tamaño de dicDatos:", len(dicDatos))

claves = sorted(dicDatos.keys())
print("Claves ordenadas del diccionario:")
for clave in claves:
    print(clave)

def buscar_valor(diccionario, clave_buscar):
    if clave_buscar in diccionario:
        return diccionario[clave_buscar]
    else:
        return None

clave_buscar = input("Ingresa un nombre para buscar en el diccionario: ")
valor_encontrado = buscar_valor(dicDatos, clave_buscar)
if valor_encontrado is not None:
    print(f"Valor encontrado para {clave_buscar}: {valor_encontrado}")
else:
    print(f"{clave_buscar} no se encuentra en el diccionario.")
