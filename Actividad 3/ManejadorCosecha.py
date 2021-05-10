from Cosecha import Cosecha
import csv


class ManejadorCosecha:
    __cosecha = None

    def __init__(self):
        self.__cosecha = Cosecha()

    def Cargar(self, camiones):
        archivo = open('ingreso.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            Id = int(fila[0])
            dia = int(fila[1])
            kg = int(fila[2])
            camion = camion.buscarCamion(ID)
            tara = int(camion.getTara())
            self.__cosecha.AgregarKG(id - 1, dia - 1, kg - tara)
        archivo.close()

    def Kilos(self, id, tara):
        kilos = 0
        for i in range(45):
            kilos += self.__cosecha.getValor(id - 1, i)
        print('\nEl camión de Identificador: %s, tiene un total de %s Kg descargados.' % (id, kilos))

    def getLista(self):
        return self.__cosecha