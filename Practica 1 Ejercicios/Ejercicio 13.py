#Imprime un bucle while los múltiplos de 2 comprendidos entre 1 y 10

#Inicializamos contador
cont = 0
#Mientras que el contador sea menor que 10
while cont<=10:
    #Comprobamos que el contador es multiplo de 2
    if cont % 2 == 0:
        print(cont," es multiplo de 2 y 2 es multiplo de ",cont)
    cont = cont + 1
