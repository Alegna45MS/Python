import sys

class MiError(Exception):
    "ERROR"
    pass

print("Los argumentos son",sys.argv)

def pedirArgumentos():
    with open("contador","w+") as contador:
        contador.write("0")
    try:
        if len(sys.argv)==2:
            opcion=sys.argv[1]
            if(opcion=="inc"):
                abrirFichero("inc")
            else:
                abrirFichero("dec")
        else:
            raise MiError
    except MiError:
        print("Los argumentos tienen que ser 2")

