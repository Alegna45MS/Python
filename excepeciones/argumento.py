import sys
class MiError(Exception):
    "ERROR"
    pass
print("Los argumentos son",sys.argv)
def pedirArgumentos():
    try:
        if len(sys.argv) == 3:
            op1 = int(sys.argv[1])
            op2 = int(sys.argv[2])
            suma = op1 + op2
            print(op1, "+", op2, "=", suma)
        else:
            raise MiError
    except MiError:
        print("Los argumentos tienen que ser 3")
    except ValueError:
        print("Los argumentos tienen que ser numericos")

pedirArgumentos()


