from Camion import Camion
import csv

class ManejadorCamion:
    __camiones = []

    def __init__(self):
        self.__camiones = []

    def agregar(self, camion):
        self.__camiones.append(camion)

    def cargar(self):
        archivo = open('camion.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            identificador= int(fila[0])
            nomConductor = fila[1]
            patente = fila[2]
            marca = fila[3]
            tara = fila[4]
            unCamion = Camion(identificador, nomConductor, patente, marca, tara)
            self.agregar(unCamion)
        archivo.close()

    def buscarCamion(self, ID):
        camion = None
        i = 0
        while i < len(self.__camiones):
            if self.__camiones[i].getId() == ID:
                camion = self.__camiones[i]
                i = len(self.__camiones)
            else:
                i += 1
        return camion

    def __str__(self):
        s = ''
        for cam in self.__camiones:
            s += str(cam) + '\n'
        return s