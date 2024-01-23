# Imprime por pantalla el menaje: desea continuar (s/n)?. Si la respuesta válida, es decir, una “n”
# o una “s”, debe indicar el error y volver a solicitar la respuesta

# Introducimos la respuesta
respuesta = input("Desea continuar (s/n)? ")
# Mientras que respuesta sea diferente de n o s,entra en el bucle y se queda
while respuesta != 's' and respuesta != 'n':
    respuesta = input("Respuesta no valida.Introduce una s o n ")
print("Adios")
