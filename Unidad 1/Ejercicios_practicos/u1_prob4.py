'''
Descripción: Jugando con listas
Autor: Jessica Castillo
Fecha: 11 de octubre 2022
'''
'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo, Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las 
muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde 
<asignatura> es cada una de las asignaturas de la lista y <nota> cada una de 
las correspondientes notas introducidas por el usuario.'''


lista=["Matematicas","Fisica", "Quimica", "Historia", "Español"]
note=[]

nota=int(input("Qué nota sacaste en Matemáticas? "))
note.append(nota)
nota=int(input("Qué nota sacaste en Física? "))
note.append(nota)
nota=input("Qué nota sacaste en Química? ")
note.append(nota)
nota=input("Qué nota sacaste en Historia? ")
note.append(nota)
nota=input("Qué nota sacaste en Español? ")
note.append(nota)


print("En ",lista[0]," has sacado ",note[0])
print("En ",lista[1]," has sacado ",note[1])
print("En ",lista[2]," has sacado ",note[2])
print("En ",lista[3]," has sacado ",note[3])
print("En ",lista[4]," has sacado ",note[4])

