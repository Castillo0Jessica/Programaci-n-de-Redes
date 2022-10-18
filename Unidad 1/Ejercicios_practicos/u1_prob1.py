'''
Descripción: Raíces de la ecuación cuadrática
Autor: Jessica Castillo
Fecha: 06 de octubre 2022
'''

A = int(input("Ingrese el coeficiente A: "))
B = int(input("Ingrese el coeficiente B: "))
C = int(input("Ingrese el coeficiente C: "))

'''Define función que calcule el resultado regrese su valor lógico que
indique True si tienen solución o False cuando no tiene solución'''

x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
    print()
      
else:
  x1 = (-B+((B**2-(4*A*C))**0.5))/(2*A)
  x2 = (-B-((B**2-(4*A*C))**0.5))/(2*A)
  print("Las soluciones son: ")
  print(x1)
  print(x2)


