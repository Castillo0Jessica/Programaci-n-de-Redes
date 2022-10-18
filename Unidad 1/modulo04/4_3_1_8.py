'''
Descripción: Día del año.  función que toma dos argumentos 
(un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo 
febrero es sensible al valor year, tu función debería ser universal).

Autor: Jessica Castillo
Fecha: 04 de octubre 2022
'''
'''La función define si son o no años bisiestos'''
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

'''toma dos argumentos (un año y un mes) con el if definimos si el mes tiene 
29 días que sería bisiesto, si no es normal'''
def days_in_month(year, month):
    diasMes = [31,28,31,30,31,30,31,31,30,31,30,31]

    if is_year_leap(year):
        if diasMes[month - 1] == 28:
            return 29
        else:
            return diasMes[month - 1]
    else:
        return diasMes[month - 1]
    return None

#Calcula los días del año dado, sea bisiesto o no
def day_of_year(year, month, day):
	days = 0
	for m in range(1, month):
		dpm = days_in_month(year, m)
		if dpm == None:
			return None
		days += dpm
	dpm = days_in_month(year, month)
	if day >= 1 and day <= dpm:
		return days + day
	else:
		return None

print(day_of_year(2000, 12, 31))
