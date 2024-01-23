# Diseñar un programa que obtenga el salario neto de n trabajadores de acuerdo a las siguientes premisas
# -Las 38 primeras horas semanales se cobran a la tarifa ordinaria.
# -Cualquier hora extra realizada se cobra 1.5 veces la tarifa ordinaria.
# -Los primeros 600 euros están libres de impuestos. Los siguientes 600 están sometidos a retenciones del 25% y los restantes al 45%.
# -Pedir por teclado el número de trabajadores y la tarifa ordinaria.

def main():
    emp = pedir_empleado()
    tarifa = pedir_tarifa()
    calcular_salario(emp, tarifa)


main()


def pedir_empleado():
    while emp <= 0:
        print("El numero de trabajdores no puede ser inferior a 0.Vuelve a introducirlo")
        trabajadores = int(input("Dime el numero de trabjadores: "))
    return emp


def pedir_tarifa():
    tarifa = int(input("DIme la tarifa ordinaria"))
    while tarifa <= 0:
        print("La tarifa no puede ser inferior a 0.Vuelve a introducirlo")
        tarifa = int(input("Dime la tarifa ordinaria"))
    return tarifa

def pedir_horas():
    horas = int(input("Dime la cantidad de horas semanales de trabajo"))

def calc_bruto(tarifa,horastrabajadas):
    salariofijo=38*tarifa
    horasextra = horastrabajadas-38
    bruto = salariofijo*(horasextra*1.5)

def calcular_impuesto(salariobruto):
    tramo1=(salariobruto-600)
    tramo2=(salariobruto-1200)
    if salariobruto<=600:
        impuestos=0
    elif salariobruto<=1200:
        impuestos=tramo1*0.25
    else:
        impuestos=600*0.25 + tramo2*0.45

def ver_resultado(salariobruto,impuestos,neto):
    print(salariobruto+impuestos+neto)



def calcular_salario(emp, tarifa):
    for i in range(1,emp+1):
        print("Empleado",i)
        horastrabajadas = pedir_horas()
        salariobruto=calcular_salario(tarifa,horastrabajadas)
        impuestos=calcular_impuesto(salariobruto)
        neto=salariobruto-impuestos
        ver_resultado(salariobruto,impuestos,neto)

