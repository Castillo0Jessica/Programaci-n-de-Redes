'''
Descripción: Operando con Listas
Autor: Jessica Castillo
Fecha: 29 de Septiembre 2022
'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

resultado = []
for i in my_list:
    if i not in resultado:
        resultado.append(i)
        
print("La lista con elementos únicos:")
print(resultado)