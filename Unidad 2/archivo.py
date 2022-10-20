#Castillo Aviles Jessica Quetzali

file = open("devices.txt", "r")
devices=[]
for line in file:
    line=line.strip()
    devices.append(line)
file.close()

print(devices)