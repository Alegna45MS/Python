
def hacer_backup(archivo_origen,archivo_destino):
    origen=open(archivo_origen,"r+")
    destino=open(archivo_destino,"r+")
    linea=origen.readline()
    while linea != " ":
        destino.write(linea)
        linea=origen.readline()
    origen.close()
    destino.close()

def main():
    hacer_backup("ejercicio1","ejercicio1copia")


