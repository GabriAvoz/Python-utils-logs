import sys

# argumentos requeridos:
#   fichero a modificar (con extension)
#   cadena a sustituir (si contine cadena de caracteres con espacio usar "")
#   cadena que sustituye ((si contine cadena de caracteres con espacio usar "")
#   nombre del fichero de salida (con extension) (opcional)

def escribir_archivo(texto, fichero = sys.argv[1]):
    with open(fichero,'w') as file:
        file.write(texto)

with open(sys.argv[1],'r') as file:
    archivo = file.read()

if sys.argv[3] == "\n":
    archivo = archivo.replace(sys.argv[2], '\n')

archivo = archivo.replace(sys.argv[2], sys.argv[3])

if len(sys.argv) > 4:
    escribir_archivo(archivo, sys.argv[4])
else:
    escribir_archivo(archivo)