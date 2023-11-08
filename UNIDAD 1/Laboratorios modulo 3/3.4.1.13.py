'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 2 Octubre 2023
Descripcion: Laboratorio 3.4.1.13
'''
# Paso 1
beatles = []

# Paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3
nombres_a_agregar = ["Stu Sutcliffe", "Pete Best"]
for nombre in nombres_a_agregar:
    beatles.append(nombre)

# Paso 4
del beatles[3]
del beatles[3]

# Paso 5
beatles.insert(0, "Ringo Starr")
print("Lista de Beatles:", beatles)
print("Número de miembros de los Beatles:", len(beatles))
