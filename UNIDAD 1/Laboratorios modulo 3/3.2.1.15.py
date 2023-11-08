'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha: 1 Octubre 2023
Descripcion: Laboratorio 3.2.1.15
'''
c0 = int(input("Ingresa un numero: "))
pasos = 0  # Contador :)

# c0 no tiene que ser igual a 1 
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)  
    pasos += 1

print("Pasos =", pasos)
