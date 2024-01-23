#Escribir un programa que pida al usuario dos números float y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error

#Introducimos num1 y num2 y los guardarmos en memoria
num1=float(input("Introduce el dividendo "))
num2=float(input("Introduce el divisor "))
#Comprobamos si el divisor no es cero y luego dividirlos
if num2==0:
    #Error cuando el divisor es cero
    print("Error: el divisor no puede ser 0")
else:
    resultado = num1/num2
    print("El cociente es", resultado) #Imprimimos el resultado

