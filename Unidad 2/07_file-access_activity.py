#Castillo Aviles Jessica Quetzali

file = open("devices.txt", "a")


while True:
    newitem=input("Nuevo dispositivo: ")
    
    if newitem == "exit":
        print("All done!")
        break
    file.write(newitem+ "\n")

file.close()


