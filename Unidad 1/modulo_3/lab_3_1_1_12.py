'''
Descripción: Fundamentos de la sentencia if-else
Autor: Jessica Castillo
Fecha: 27 de Septiembre 2022
'''
year = int(input("Introduce un año:"))

if year < 1582:
    print("No esta dentro del período del calendario Gregoriano")
elif year % 4 !=0: #NO es divisible entre 4
    print("Año común")
elif year % 100 !=0:
    print("Año Bisiesto")
elif year % 400 !=0:
    print ("Año comun")
else:
    print('Año Bisiesto')
    

