'''
Descripción: Lo básico de las listas- los Beatles
Autor: Jessica Castillo
Fecha: 29 de Septiembre 2022
'''

# paso 1


Beatles=[]
print("Paso 1:", Beatles)

# paso 2
Beatles.append("Jonh Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3
for i in range (2):
    Beatles.append(input("Agrega uno más"))
print("Paso 3:", Beatles)

# paso 4
del Beatles[3]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0,"Ringo Start")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))