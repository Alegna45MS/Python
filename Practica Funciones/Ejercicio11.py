#Diseñar un programa que lea desde teclado: el día , el código del mes y el año

def main():
    mes = pedirMes()
    anno = pediranno()


def validar_datos():


def esBisiesto():


def pediranno():
    annoValido= False
    while not annoValido:
        anno=int(input("Introduce el año"))
        annoValido == anno >=


def pedirMes():
    mesValido = False
    while not mesValido:
        mes = int(input("Introduce el mes"))
        mesValido = mes>=1 and mes <= 12
        if not mesValido:
            print("error")
    return mes

def validarDia():
    diaValido = False
    while not diaValido:
        dia = int(input("Introduce el dia"))
        match mes:
            case 1|3|5|7|8|10|12:
                diaValido = dia>=1 and dia<=30
            case 4|6|9|11:
                diaValido = dia>=1 and dia<=28
            case 2:
                if esBisiesto():



