# Definimos la funcion
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Introducimos un numero entero
numero = int(input("Introduce un numero entero: "))
# Comprobamos que el numero es par
if es_par(numero):
    print(numero,"es par")
else:
    print(numero,"es impar")

#Ambito de la variable:...fuera de ese ambito,esa variable no existe
