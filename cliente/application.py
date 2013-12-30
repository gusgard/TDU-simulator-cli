__author__ = 'yoda'
import socket
import sys
from time import sleep
from vehiculo import Vehiculo
import threading
import random

class miThread(threading.Thread):
    def __init__(self, ip, port, vehiculo, tiempo_muerto):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.vehiculo = vehiculo
        self.tiempo_muerto = tiempo_muerto

    def run(self):
        #print "Arranca" + str(self.vehiculo.id_vehiculo)
        while 1:
            sleep(self.tiempo_muerto)
            generar_vehiculo(self.vehiculo)
            client(self.ip, self.port, self.vehiculo.serializar())
        #print "Finalizando... " + str(self.vehiculo.id_vehiculo)



def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "respuesta ", len(response)
        print "Received: {}".format(response)

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
    IP, PORT = "awseb-e-q-AWSEBLoa-U0TZFW27RVH5-1541299131.us-west-2.elb.amazonaws.com", 9997
    #data = " ".join(sys.argv[1:])
    cantidad_vehiculos = int(sys.argv[1])
    #mensaje = sys.argv[2]
    #print "por parametro ", segundos, mensaje

    #vehiculo = Vehiculo(id_vehiculo,0,0,0)

    for cant in xrange(0, cantidad_vehiculos):
        vehiculo = Vehiculo(cant, 0, 0, 0)
        tiempo_muerto = float(random.randint(1, 100))/10
        print tiempo_muerto
        thread = miThread(IP, PORT, vehiculo, tiempo_muerto)
        thread.start()

    #while 1:
    #    sleep(0.1)
        #client(IP, PORT, data+str(cont))
        #generar_vehiculo(vehiculo)
        #client(IP, PORT, vehiculo.serializar())

