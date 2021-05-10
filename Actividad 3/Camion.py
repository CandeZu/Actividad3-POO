class Camion:
    __identificador = 0
    __nomConductor = ''
    __patente = ''
    __marca = ''
    __tara = 0

def __init__(self, id, nomC, patente, marca, tara):
    self.__identificador = id
    self.__nomConductor = nomC
    self.__patente = patente
    self.__marca = marca
    self.__tara = tara

def getIdentidicador(self):
    return self.__identificador

def getPatente(self):
    return self.__patente

def getMarca(self):
    return self.__marca

def getNombreConductor(self):
    return self.__nomConductor

def getTara(self):
    return self.__tara

def __str__(self):
    return 'ID del camión: %s - Nombre del Conductor: %s - Patente del Camión: %s - Marca del Camión: %s - Peso del Camión: %s' % (self.__identificador, self.__nomConductor, self.__patente, self.__marca, self.__tara)
