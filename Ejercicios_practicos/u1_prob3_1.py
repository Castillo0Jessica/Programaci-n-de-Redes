'''
Descripción: PArtiendo fecha
Autor: Jessica Castillo
Fecha: 11 de octubre 2022
'''

'''
Crea una función que acepta la cantidad y regrese el impuesto calculado.
Solo se permiten valores positivos mayores a cero.

'''
money=int(input("Ingresa el la cantidad de dinero: "))

if (money > 0):
    if money < 10000:
        interes= money*0.05
        print("El impuesto es de $",interes)
    elif money >10000 and money<=20000:
        interes= money*0.15
        print("El impuesto es de $",interes)
    elif money >20000 and money<=35000:
        interes= money*0.20
        print("El impuesto es de $",interes)
    elif money >35000 and money<=60000:
        interes= money*0.30
        print("El impuesto es de $",interes)
    elif money >60000:
        interes= money*0.45
        print("El impuesto es de $",interes)
else:
    print("Cantidad inválida")





