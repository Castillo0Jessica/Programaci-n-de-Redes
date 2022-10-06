'''
Descripción: Realiza un programa en Python que indique si un número es divisible entre otro.
Autor: Jessica Castillo
Fecha: 06 de octubre 2022
'''

n1= int (input("Ingresa el primer número: "))
n2= int (input("Ingresa el segundo número: "))

if n1%n2 == 0:
        print("El ",n1, "es divisible entre",n2)
else:
    
        print("El ",n1, "no es divisible entre",n2)

