import sys

# argumentos requeridos:
#   fichero a modificar (con extension)
#   palabra a añadir (si contine cadena de caracteres con espacio usar "". NO SE INCLUYE ESPACIO POR DEFECTO)
#   nombre del fichero de salida (con extension)

archivo = open(sys.argv[3],'w')

if sys.argv[3].find(".sh") >= 0:
    archivo.write("#!/bin/sh\n\n")

with open(sys.argv[1],'r') as fichero:
    for linea in fichero:
        archivo.write(sys.argv[2] + str(linea))
        
archivo.close()
