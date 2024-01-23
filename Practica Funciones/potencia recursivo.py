def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)


def main():

    base = int(input("Introduce la base"))
    exp = int(input("Introduce el exponente"))
    print(base, "elevado a", exp, "es igual a:", potencia(base, exp))


main()
