__author__ = 'yoda'
import socket
import sys
from time import sleep
from vehiculo import Vehiculo

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received1: {}".format(response)

        #time.sleep(20)
        #sock.sendall(message)
        #response = sock.recv(1024)
        #print "Received2: {}".format(response)

    finally:
        sock.close()

def generar_vehiculo(vehiculo):
    vehiculo.var1 += 1
    vehiculo.var2 += 2
    vehiculo.var3 += 3
    return vehiculo

if __name__ == "__main__":
    IP, PORT = "localhost", 9997
    #data = " ".join(sys.argv[1:])
    id_vehiculo = sys.argv[1]
    #mensaje = sys.argv[2]
    #print "por parametro ", segundos, mensaje

    cont = 0
    vehiculo = Vehiculo(id_vehiculo,0,0,0)

    while 1:
        sleep(0.1)
        cont += 1
        #client(IP, PORT, data+str(cont))
        generar_vehiculo(vehiculo)
        client(IP, PORT, vehiculo.serializar())

    #time.sleep(int(segundos))
    #
    #
    #client(IP, PORT, "termino , mandnado segundo mensaje")

