#Introduce por teclado dos e imprime cual es menor
#Introducimos num1 y num2 y los guardarmos en memoria
num1=int(input("Introduce el primer numero"))
num2=int(input("introduce el segundo numero"))
#Ponemos las condiciones
if num1 > num2:  # Si num1 es mayor que num2, num2 es el menor numero
    print(num2,"es menor que",num1)
else:  # Si num2 es mayor que num1, num1 es el menor numero
    print(num1, "es menor que", num2)
