'''
Descripción: Hipotesis de Collatz
Autor: Jessica Castillo
Fecha: 29 de Septiembre 2022
'''
c0=int(input("Ingresa un número: "))

paso= 0
while c0 !=1:
    
    if c0%2==0:
        c0=int (c0/2)
        print(c0)
    else:
        c0=int(3*c0+1)
        print(c0)
        

    paso+=1  
print("pasos= ", paso)
    