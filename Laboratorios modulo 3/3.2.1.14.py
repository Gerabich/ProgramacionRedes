'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 1 Octubre 2023
Descripcion: Laboratorio 3.2.1.14
'''
blocks = int(input("Ingresa el número de bloques: "))

altura = 0
bloquesu = 0  
bloques_por_capa = 1  

while bloquesu + bloques_por_capa <= blocks:
    altura += 1 
    bloquesu += bloques_por_capa  
    bloques_por_capa += 1  

print("La altura de la pirámide es:", altura)
