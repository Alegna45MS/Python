# Imprime por pantalla el menaje: desea continuar (s/n)?. Si la respuesta válida, es decir, una “n”
# o una “s”, debe indicar el error y volver a solicitar la respuesta

# Iniciamos una variable booleana
respuesta_valida = False
# Mientras la respuesta no sea valida
while not respuesta_valida:
    # Pedir que introdudca la respuesta
    respuesta = input("Desea continuar (s/n)?: ")
    # Comprobamos que la respuesta es correcta si introducimos s o n
    respuesta_valida = respuesta == 's' or respuesta == 'n'
    #Si la respuesta no es valida,enviara un mensaje de error
    if not respuesta_valida:
        print("Error.Teclea una s o una n")
print("Fin del programa")
