cad1= input("Ingrese una palabra")
cont = 0


for i in range (len(cad1)):
    if (cad1[i] == ' '):
        cont= cont+1


if(cont==0):
    print("No hay espacios")
else:
    print("El numero de espacios es de: ", cont)

