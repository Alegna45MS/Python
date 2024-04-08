class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        print()
        menu = [
            ['Agenda Personal'],
            ['1. Añadir Contacto', "anadir"],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Eliminar contacto'],
            ['6. Cerrar agenda']
        ]
        for option in menu:
            print(option[0])

    def anadir(self):
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        email = input("Introduce el email del contacto: ")
        contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
        self.contactos.append(contacto)

    def lista(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos:
                print("Nombre:", contacto['nombre'])
                print("Teléfono:", contacto['telefono'])
                print("Email:", contacto['email'])
                print()

    def agenda_vacia(self):
        return self.contactos == False

    def buscar(self, nombre):
        cont=0
        for contacto in self.contactos1:
            if contacto['nombre'] == nombre:
                return cont
            cont=cont+1
        return -1

    def editar(self):
        nombre = input("Introduce el nombre del contacto a editar: ")
        indice = self.buscar(nombre)
        if indice == -1:
            print("El contacto no se encuentra en la agenda.")
            return

        print("Selecciona qué quieres editar:")
        print("1. Nombre")
        print("2. Teléfono")
        print("3. E-mail")
        print("4. Volver")

        opcion = input("Elija una opción: ")
        if opcion == '1':
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            self.contactos[indice]['nombre'] = nuevo_nombre
        elif opcion == '2':
            nuevo_telefono = input("Introduce el nuevo teléfono: ")
            self.contactos[indice]['telefono'] = nuevo_telefono
        elif opcion == '3':
            nuevo_email = input("Introduce el nuevo email: ")
            self.contactos[indice]['email'] = nuevo_email
        elif opcion == '4':
            return
        else:
            print("Opción inválida.")

    def eliminar(self):
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        indice = self.buscar(nombre)
        if indice == -1:
            print("El contacto no se encuentra en la agenda.")
            return

        del self.contactos[indice]
        print("Contacto eliminado.")

    def cerrar_agenda(self):
        print("Saliendo de la agenda...")
        exit()


# Ejemplo de uso:
agenda = Agenda()
while True:
    agenda.menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        agenda.anadir()
    elif opcion == "2":
        agenda.lista()
    elif opcion == "3":
        nombre = input("Introduce el nombre del contacto a buscar: ")
        indice = agenda.buscar(nombre)
        if indice != -1:
            print("El contacto se encuentra en la posición:", indice)
        else:
            print("El contacto no se encuentra en la agenda.")
    elif opcion == "4":
        agenda.editar()
    elif opcion == "5":
        agenda.eliminar()
    elif opcion == "6":
        agenda.cerrar_agenda()
    else:
        print("Opción inválida. Inténtalo de nuevo.")