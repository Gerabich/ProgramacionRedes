'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 25 septiempre 2023
Descripcion: Laboratorio 2.6.1.11
'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

total_mins = hour * 60 + mins + dura
final_hour = total_mins // 60
final_min = total_mins % 60
final_hour %= 24
print(f"{final_hour:02d}:{final_min:02d}")
