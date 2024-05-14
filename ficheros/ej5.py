import urllib.request

url="https://tools.ietf.org/html/rfc1180"
archivo_webpage=open("ejercicio1copia","wb")
webpage=urllib.request.urlopen(url)
for linea in webpage:
    archivo_webpage.write(linea)
archivo_webpage.close()