def main():
    salir=False
    while salir == False:
        opcion=introducir_opcion()
        salir=opcion==5
        if not salir:
            op1=float(input("Introduce el primer operando"))
            op2=float(input("Introduce el segundo operando"))
            match opcion:
                    case 1:
                        resultado=suma(op1,op2)
                    case 2:
                        resultado=resta(op1,op2)
                    case 3:
                        resultado=multiplicar(op1,op2)
                    case 4:
                        resultado=dividir(op1,op2)
            print(resultado)
        print("Hasta luego")


main()


def introducir_opcion():
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Salir")
        opcionvalida=False
        while not opcionvalida:
            opcion=(int(input("Escoge una opcion entre 1-5")))
            opcionvalida=opcion>=1 and opcion <=5
            if not opcionvalida():
                print("Error:La opcion tiene que estar comprendido entre 1 y 5")
        return opcion


def suma(op1,op2):
    return op1+op2

def resta(op1,op2):
    return op1-op2

def multiplicar(op1,op2):
    return op1*op2

def dividir(op1,op2):
    return op1/op2
