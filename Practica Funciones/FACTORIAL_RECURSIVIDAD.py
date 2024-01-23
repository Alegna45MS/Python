def factorial(num):
    if (num == 0):
        return 1
    return num * factorial(num - 1)


def main():
    num = int(input("Introduce un numero entero pequeño"))
    print("El factorial de", num, "=", factorial(num))


main()
