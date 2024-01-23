#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

#Introducimos el numero entero y lo guardamos en memoria
num = int(input("Introduce un numero: "))
#Comprobamos si el numero es par o impar
if num % 2==0:
    print("El numero es par")
else:
    print("El numero es impar")
