from agenda import *
import os
def main():
    # bloque principal
    agenda = Agenda()
    ruta = "/home/alumno/"
    nombre_fichero = ruta + "agenda.datos"
    if os.path.exists(nombre_fichero) :
        print("cargando el fichero")
        agenda.cargar()
    agenda.arrancar_aplicacion()

main()