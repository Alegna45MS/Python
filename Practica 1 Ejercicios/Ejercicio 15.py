# Programa una calculadora sencilla que haga las operaciones de suma, resta, multiplicación y
# división de dos floats

# Inicializamos una variable booleana
salir = False
# Mientras que no quiera salir
while not salir:
    # Imprimimos en pantalla un menu
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")
    # Introducimos la opcion elegida y comprobamos si es valida
    opcion_valida = False
    while not opcion_valida:
        #Introducimos una opcion
        opcion = int(input("Escoge una opcion entre 1-5"))
        opcion_valida=opcion >=1 and opcion <=5
        #Si la opcion no es valida,envia un mensaje de error
        if not opcion_valida:
            print("Error:La opcion tiene que estar comprendido entre 1 y 5")

    #Comprobamos si desea abandonar la aplicacion
    salir = opcion == 5
    if not salir:
        num1=float(input("Introduce el primer operando"))
        #Mientras que haya elegido dividir y el divisor sea 0,volvemos a pedir el segundo numero
        num2=float(input("Introducimos el segundo operando"))
        while num2 == 0 and opcion == 4:
            num2 = float(input("Error:No se puede dividir por cero.Vuelva a introducirlo"))
        #Hacemos la operacion dependiendo de la operacion elegida
        match opcion:
            case 1:
                resultado = num1 + num2
            case 2:
                resultado = num1 - num2
            case 3:
                resultado = num1 * num2
            case 4:
                resultado = num1 / num2
        print(resultado)
print("Hasta luego")
