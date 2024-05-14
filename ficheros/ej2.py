archivo = open("ejercicio1","r+")
print(archivo.read())

nombre=archivo.name
modo = archivo.mode
encoding = archivo.encoding

archivo.close()