"""Diseña una función que calcule y retorne la potencia de una base entera positiva elevada a un
exponente entero positivo. Ejemplo: 2 ** 3 = 8 , 2 ** 0 = 1"""


def potencia(base, exp):
    # Inicializar el acumulador
    pot = 1
    for i in range(1, exp + 1):
        pot = pot * base
    return pot


def main():
    # Introducimos la base y exponente
    base = int(input("Introduce la base: "))
    exp = int(input("Introduce el exponente: "))
    # Imprimimos el resultado
    print(base,"elevado a",exp,"es igual a", potencia(base, exp))


main()
