def cargar_diccionario():
    dic1 = {}
    for i in range(0, 3):
        en = input("Introduce la palabra en ingles")
        es = input("Introduce la traduccion en español")
        dic1[en] = es
    return dic1


def listar_dic(dic1):
    for i in dic1:
        print(i)


def buscar_dic(dic1):
    palabraBuscar = input("Introduce la palabra a buscar en ingles")
    if palabraBuscar in dic1:
        print(dic1[palabraBuscar])
    else:
        print("No se ha encontrado")


def main():
    diccionario = cargar_diccionario()
    listar_dic(diccionario)
    buscar_dic(diccionario)


main()
