import os
with open('texto', 'r') as file:
    # Obtiene el tamaño total del archivo
    file_size = size = os.path.getsize('texto')

    # Itera desde el final del archivo hasta el principio
    for i in range(file_size - 1, -1, -1):
        # Mueve el puntero de lectura a la posición actual
        file.seek(i)
        # Lee un carácter
        char = file.read(1)
        # Imprime el carácter
        print(char, end='')