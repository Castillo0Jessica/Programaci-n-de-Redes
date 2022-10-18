'''
Descripción: UN año bisiesto. Funciones
Escribir y probar una función que toma un argumento (un año) y 
devuelve True si el año es un año bisiesto, o False si no lo es.
Y si es ejecutado correctamente manda OK.
Autor: Jessica Castillo
Fecha: 04 de octubre 2022
'''
'''El año es bisiesto si es divisible entre 4,
   no lo es si es divisible entre 100,
   también es bisiesto si es divisible entre 400.
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

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
