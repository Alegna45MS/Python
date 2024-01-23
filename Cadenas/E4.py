cad1= input("Ingrese una palabra")
cad2=""


for i in range(len(cad1)):
    if(cad1[i]!=' '):
        cad2+=cad1[i]+' '


print("Cadena inicial: ", cad1)
print("Cadena modificada: ", cad2)
