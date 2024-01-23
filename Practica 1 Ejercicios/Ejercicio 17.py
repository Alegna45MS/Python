#Pide por teclado la altura o base de un triángulo como éste
#Introducimos la altura del triangulo
altura = int(input("Introduce la altura"))
#i es el contador de la altura y j el contador de asteriscos de 1 hasta el valor de la altura
for i in range(0,altura + 1):
    for j in range(0,i):
        print("*",end="")
    print(" ") #Cambio de linea
