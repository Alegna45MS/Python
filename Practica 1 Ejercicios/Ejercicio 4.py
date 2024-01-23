#Almacenamos la contraseña valido
password = "1234"
#Guardamos la contraseña introducida en memoria
password_introducida = input("Introduzca la contraseña")
#Comprobamos si la contraseña es correcta
if password_introducida == password:
    print("La contraseña es correcta")
else:
    print("No es correcta")
