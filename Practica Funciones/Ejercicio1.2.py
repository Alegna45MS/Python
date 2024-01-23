# Definimos la funcion
def es_par(numero):
    return numero % 2 == 0


def main():
    # Introducimos un numero entero
    numero = int(input("Introduce un numero entero: "))
    # Comprobamos que el numero es par
    if es_par(numero):
        print(numero, "es par")
    else:
        print(numero, "es impar")


main()

#Paso de parametros:existen dos formas de pasar parametros:por valor y por referencia.
#en el paso de parametros por valor,lo que le paso a la funcion invocada es una copia del contenido que tiene la variable declarada en el ambito en el cual llamo a la funcion
#En java los objetos se pasan por referencia
