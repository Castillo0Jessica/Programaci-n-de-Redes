'''
Descripción: LA sentencia continue.
Autor: Jessica Castillo
Fecha: 29 de Septiembre 2022
'''
user_word=input("INgresa una palabra: ")
user_word = user_word.upper() 
for letter in user_word:
   if letter == "A":
       continue
   elif letter =="E":
       continue
   elif letter=="I":
       continue
   elif letter =="O":
       continue
   elif letter=="U":
       continue
   else:
       print(letter)