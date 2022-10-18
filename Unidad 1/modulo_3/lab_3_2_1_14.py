'''
Descripción: Fundamentos del ciclo while
Autor: Jessica Castillo
Fecha: 29 de Septiembre 2022
'''

blocks = int(input("Ingresa el número de bloques: "))
height = 0
utilizados = 0
fila = 1

while True:
    utilizados += fila
    
    if utilizados > blocks:
        break
    height += 1
    fila += 1	
print("La altura de la pirámide:", height)