#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos"
#los números impares desde 1 hasta ese número separados por comas

num = int(input("Introduce un numero "))
if num<0:
    print("Tiene que ser entero positivo")
else:
    for i in range(1,num+1,2):
        print(i ,end=" ")
