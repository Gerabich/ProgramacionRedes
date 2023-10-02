'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 2 Octubre 2023
Descripcion: Prob2
'''

asignaturas = [
    "Probabilidad y Estadística",
    "Electrónica para IDC Física",
    "Conexión de redes WAN",
    "Administración de servidores I",
    "Programación de Redes",
    "Inglés IV",
    "Ajedrez"
]

calificaciones = {}
for asignatura in asignaturas:
    calificacion = float(input(f"Ingrese la calificacion de la unidad I de {asignatura}: "))
    calificaciones[asignatura] = calificacion 
    
for asignatura, calificacion in calificaciones.items():
    print(f"En {asignatura} has sacado {calificacion}")