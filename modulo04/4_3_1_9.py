'''
Descripción: Número de primos. Verificar de un rango de números cuál es 
primo y cual no, luego numerar los números primos.
Autor: Jessica Castillo
Fecha: 04 de octubre 2022
'''

#Identificar que numeros son divibles y cuales estan dentro del rango
#asignado para luego imprimirlos en consola.
def is_prime(num):
    x=2
    while x<num:
        if num % x == 0:
            return False
        x += 1
    return True

for i in range(1, 20):
	if is_prime(i + 1):
         print(i + 1, end=" ")

print()