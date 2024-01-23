# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

# Introducimos la renta y lo guardamos en memoria
renta = int(input("Introduce su renta: "))

# Comprobamos la cantidad de impositivo que corresponde segun la renta
if renta < 10000:
    imp=5
elif 10000 <= renta <= 20000:
    imp=10
elif 20000 <= renta <= 35000:
    imp=20
elif 35000 <= renta <= 60000:
    imp=30
else:
    imp=45
print("Su impositivo es del",imp,"%")
