'''
Descripción: Operadores y expresiones
Autor: Jessica Castillo
Fecha: 22 de Septiembre 2022
'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

hour=(hour+((mins+dura)//60))%24
mins=((mins+dura)%60)
print(hour,mins,sep=":")