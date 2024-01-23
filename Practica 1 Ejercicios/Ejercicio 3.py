#Introduce por teclado un número e imprime en pantalla si es negativo, 0 o positivo.
#Introducimos num1 y lo guardarmos en memoria
num=int(input("Introduce un numero"))
#Ponemos las condiciones
if num>0: #Si num es mayor que 0,es positivo
    print(num, "es positivo")
elif num<0: #Si num es menor que 0,es negativo
    print(num, "es negativo")
else: #Si no se cumple ninguno,es que num es 0
    print(num ,"es 0")
