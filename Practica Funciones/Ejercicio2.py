# Diseña una función que calcule y devuelva el factorial de un número entero. Sabemos que:
# !0 es 1, 5! = 5 * 4 * 3 * 2 * 1

"""Esta funcion calcula el factorial de un numero positivo de forma iterativa"""


def factorial(numero):
    # Inicializamos el acumulador
    fact = 1
    for i in range(1, (numero + 1)):
        fact = fact * i
    return fact


def main():
    # Introducimos el numero entero positivo
    numero = int(input("Intoduce un numero entero: "))
    # Imprimimos el resultado
    print("El factorial de", numero, "es:", factorial(numero))


# Aqui arranca la aplicacion
main()
