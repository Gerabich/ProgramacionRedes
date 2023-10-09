'''
Autor: Gerardo Antonio Garcia Vazquez
Fecha 8 Octubre 2023
Descripcion: Laboratorio 4.3.1.8
'''
def is_year_leap(year):
   
    # Tu código del LABORATORIO 4.3.1.6.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
   
    # Tu código del LABORATORIO 4.3.1.7.
    days_por_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days_por_month[2] = 29

    if month < 1 or month > 12:
        return None
    return days_por_month[month]

def day_of_year(year, month, day):
  
    # Escribe tu código nuevo aquí.
    if year < 1 or month < 1 or month > 12 or day < 1:
        return None

    days_in_the_month = days_in_month(year, month)

    if day > days_in_the_month:
        return None

    total_days = day
    for i in range(1, month):
        total_days += days_in_month(year, i)

    return total_days

print(day_of_year(2000, 12, 31))

