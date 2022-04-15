import sys

# argumentos requeridos:
#   fichero de entrada
#   marca de tiempo (tiempo absoluto (s)) que marca el momento 0 (OPCIONAL)

marcador = "*-+-*"
marca_query = "+-+-+"
marca_tiempo = 0

query_time = []
tiempos = []
persistencia = []
requester = []
endpoints = []

def print_list(a):
    for x in range(len(a)):
        print (a[x])

# Leer archivo
with open(sys.argv[1],'r',encoding="utf8") as file:
    archivo = file.readlines()

# Crear archivo de salida y cabecera
salida = open("salida.csv",'w')
salida.write("Tiempo (s),Persistencia,Tiempo query (ms),Requester,Endpoint\n")

# Calcular marca de tiempo
if len(sys.argv) > 2:
    marca_tiempo = int(sys.argv[2])
else:
    marca_tiempo = 0

# Extraccion de datos por linea
for line in archivo:
    if marcador in line:
        if (len(tiempos) < 1) and marca_tiempo == 0:
            marca_tiempo = int(line.split(marcador)[1])
            tiempos.append(0)
        else:
            time = int(line.split(marcador)[1])
            tiempos.append(time - marca_tiempo)

        
        if "DESACTIVAR" in line:
            persistencia.append("DESACTIVAR")
        elif "ACTIVAR" in line:
            persistencia.append("ACTIVAR")

        salida.write(str(tiempos[-1]) + "," + persistencia[-1] + ",,,\n")
        
    elif marca_query in line:
        tiempos.append(int(line.split(marca_query)[1]) - marca_tiempo)
        query_time.append(int(line.split(marca_query)[2]))
        persistencia.append(line.split(marca_query)[3])
        requester.append(line.split(marca_query)[4])
        endpoints.append(line.split(marca_query)[5])

        salida.write(str(tiempos[-1]) + "," + str(persistencia[-1]) + "," + str(query_time[-1]) + "," + str(requester[-1]) + "," + str(endpoints[-1]) + "\n")

salida.close()

