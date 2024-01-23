#Introduce por teclado las notas de un conjunto de alumnos hasta que teclees un 0 para salir.
#Imprime la nota media siempre y cuando haya introducido alguna nota.

#Inicializamos un booleano para salir de la aplicacion
salir = False
#Inicializamos un contador de notas
cont = 0
#Inicializamos un acumulador para sumar las notas
suma = 0
while not salir: #not salir = salir==False
    nota = float(input("Introduce las notas.0 para terminar"))
    salir = nota==0 #Si nota es 0,salir=True y sale del bucle
    if not salir:
        suma = suma + nota
        cont = cont + 1
if cont>0:
    media = suma/cont
    print("La media es:",media)
else:
    print("No has introducido ningun valor")
