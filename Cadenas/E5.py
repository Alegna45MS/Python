def palindromo(cad):
    pos=0
    for i in range(len(cad)-1,0+1,-1):
        if(cad[i]!=cad[pos]):
            return False
        pos = pos+1
    return True



def main():
    cad = input("Ingrese una palabra")
    if(palindromo(cad)):
        print("Es un palindromo")
    else:
        print("No es un palindromo")


main()