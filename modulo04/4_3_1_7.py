'''
Descripción: ¿Cuántos días?
Autor: Jessica Castillo
Fecha: 04 de octubre 2022
'''
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	res = test_results[i]
	print(yr, res, "-> ", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")