# creamos nuestra clase agenda
import pickle


class Agenda:
    # iniciamos nuestra clase
    def __init__(self):
        # crearemos una lista donde guardaremos los datos de nuestra agenda
        self.contactos = []

    def agenda_vacia(self):
        return len(self.contactos) == 0

    # menu del programa

    # función para añadir un contacto
    def anadir(self):
        print("---------------------")
        print("Añadir nuevo contacto")
        print("---------------------")
        nom = input("Introduzca el nombre del contacto: ")
        data = self.buscar(nom)
        existe = data != -1
        if existe:
            print("contacto ya existe")
        else:
            telf = input("Introduzca el teléfono: ")
            email = input("Introduzca el email: ")
            self.contactos.append({'nombre': nom, 'telf': telf, 'email': email})

    # función para hacer consultas
    def consultas(self):
        if self.agenda_vacia():
            print("No hay ningún contacto en la agenda")
        else:
            nom = input("Introduzca el nombre del contacto: ")
            data = self.buscar(nom)
            existe = data != -1
            if not existe:
                print("el contacto no existe en la agenda")

    # función para imprimir la lista de contactos
    # En este caso imprimiremos solo los nombres de los contactos
    # con ellos podremos buscar luego un contacto
    def lista(self):
        print("------------------")
        print("Lista de contactos")
        print("------------------")
        if self.agenda_vacia():
            print("No hay ningún contacto en la agenda")
        else:
            for x in range(len(self.contactos)):
                print(self.contactos[x]['nombre'] + " " + self.contactos[x]['telf'] + " " + self.contactos[x]['email'])

    # función para buscar un contacto a través del nombre
    def buscar(self, nom):
        for x in range(len(self.contactos)):
            if nom == self.contactos[x]['nombre']:
                print("Datos del contacto")
                print("Nombre: ", self.contactos[x]['nombre'])
                print("Teléfono: ", self.contactos[x]['telf'])
                print("E-mail: ", self.contactos[x]['email'])
                return x
        return -1

    # función para editar los datos de un contacto
    def editar(self):
        if self.agenda_vacia():
            print("No hay ningún contacto en la agenda")
        else:
            print("---------------")
            print("Editar contacto")
            print("---------------")
            nom = input("Introduzca el nombre del contacto: ")
            data = self.buscar(nom)
            existe = data != -1
            if existe:
                condition = False
                while condition == False:
                    print("Selecciona que quieres editar: ")
                    print("1. Nombre")
                    print("2. Teléfono")
                    print("3. E-mail")
                    print("4. Volver")
                    option = int(input("Introduzca la opción deseada: "))
                    if option == 1:
                        nom = input("Introduzca el nuevo nombre: ")
                        self.contactos[data]['nombre'] = nom
                    elif option == 2:
                        telf = input("Introduzca el nuevo teléfono: ")
                        self.contactos[data]['telf'] = telf
                    elif option == 3:
                        email = input("Introduzca el nuevo email: ")
                        self.contactos[data]['email'] = email
                    elif option == 4:
                        condition = True
            else:
                print("el contacto no existe en la agenda")

    def eliminar(self):
        if self.agenda_vacia():
            print("No hay ningún contacto en la agenda")
        else:
            print("---------------")
            print("Eliminar contacto")
            print("---------------")
            nom = input("Introduzca el nombre del contacto: ")
            data = self.buscar(nom)
            existe = data != -1
            if existe:
                self.contactos.remove(self.contactos[data])
                print("contacto eliminado")
            else:
                print("el contacto no existe en la agenda")

    def guardar(self):
        f = open("/home/alumno/agenda.datos", "wb")
        pickle.dump(self.contactos, f)
        f.close()

    def cargar(self):
        f = open("/home/alumno/agenda.datos", "rb")
        personas = pickle.load(f)
        f.close()
        self.contactos = personas

    def arrancar_aplicacion(self):
        print()
        lista_menu = [
            ['Agenda Personal'],
            ['1. Añadir Contacto'],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Eliminar contacto'],
            ['6. Cerrar agenda']
        ]

        for x in range(7):
            print(lista_menu[x][0])

        opcion = int(input("Introduzca la opción deseada: "))
        match opcion:
            case 1:
                self.anadir()
            case 2:
                self.lista()
            case 3:
                self.consultas()
            case 4:
                self.editar()
            case 5:
                self.eliminar()
            case 6:
                print("Saliendo de la agenda ...")
                self.guardar()
                exit()
            case opcion_novalida_:
                print("opcion no válida")

        self.arrancar_aplicacion()
