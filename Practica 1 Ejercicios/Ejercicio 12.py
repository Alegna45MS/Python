# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# Almacenamos la contraseña valida
contrasena = "1234"
# Introducimos la contraseña
contrasena_introducida = input("Introduce su contraseña ")
# Mientras la contraseña no sea correcta,seguira preguntando
while contrasena != contrasena_introducida:
    print("Contraseña incorrecta.Vuelve a introducirla")
    contrasena_introducida = input("Introduce su contraseña ")
print("Contraseña correcta")

