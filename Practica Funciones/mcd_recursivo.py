def mcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = mcd(num1-num2, num2)
            return num1
        else:
            num2 = mcd(num1, num2-num1)
            return num2
    return num1


def main():
    # Introduce num1 y num2
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    # Enviamos a pantalla el resultado
    print("El maximo comun divisor de", num1, "y", num2, "es:", mcd(num1, num2))


main()
