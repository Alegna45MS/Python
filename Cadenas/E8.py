def decimal_binario(num):
    cad=""
    while num!=0:
        if(num%2==0):
            cad="0"+cad
        else:
            cad="1"+cad
        num=num//2
    return cad



def main():
    num=int(input("Introduzca un numero para pasarlo a binario"))
    while num > 255 or num < 0:
        num = int(input("El numero sobrepasa el limite (255), introduzcalo de nuevo"))
    print(num," en binario es: ", decimal_binario(num))



main()