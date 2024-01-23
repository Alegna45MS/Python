#Pide por teclado la altura y base de un rectángulo de asteriscos e imprímelo
#Introducimos la altura y base del rectangulo
altura =int(input("Introduce la altura")) #Numero de filas
base = int(input("Introduce la base"))#Numero de asteriscos como base
#i es el contador de altura y j es el contador de base
for i in range(1,altura + 1):
    for j in range(1,base + 1):
        print("*",end="")
    print(" ") #Cambio de linea

