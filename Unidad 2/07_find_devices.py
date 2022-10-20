#Castillo Aviles Jessica Quetzali

file = open("devices.txt", "r")

dispo=input("Ingresa un dispositivo:  ")
for line in file:
    line=line.strip()
    if (dispo in line):
        print(line)
    else:
        print("Dispositivo no encontrado")
        break
file.close()






























