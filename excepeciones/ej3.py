class MiError(Exception):
    "Excepcion propia"
    pass

def pidenumero(numero):
    try:
        numero=int(numero)
        if numero == 20:
            print("Adivinaste")
        else:
            raise MiError
    except MiError:
        print("Ese no era el numero")
    except:
        print("Hubo un error")

pidenumero(-1j)
pidenumero(12)
pidenumero(20)