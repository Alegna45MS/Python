import glob
import os.path


todos = glob.glob("/home/alumno/Escritorio/*")
ficheros=[]
directorios=[]

for file in todos:
    if(os.path.isdir(file)):
        directorios.append(file)
    if(os.path.isfile(file)):
        ficheros.append((file))


for i in directorios:
    print(i)
    print("DIRECTORIO")
for j in ficheros:
    print(j)
    print("FICHERO")




