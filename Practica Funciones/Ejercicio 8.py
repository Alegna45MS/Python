#Diseña una función que reciba un número en base 10 e imprima en pantalla la conversión a binario

def decimal_binario(num,base):
    if (num<base):
        print(num,end="")

    else:
        decimal_binario(num//base,base)
        print(num%base,end="")

def main():
    num=int(input("Introduce un numero"))
    base=2
    decimal_binario(num,base)

main()
