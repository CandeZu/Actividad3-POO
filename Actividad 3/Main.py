from ManejadorCamion import ManejadorCamion
from ManejadorCosecha import ManejadorCosecha
from Validador import ValidaEntero
from Menu import Menu
import os

if __name__ == '__main__':
    Camiones = ManejadorCamion()
    Camiones.cargar()

    Cosechas = ManejadorCosecha()
    Cosechas.cargar(Camiones)

    menu = Menu()
    cad = ' MENÚ '
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(58, '='))
        print('0 - Salir.')
        print('1 - Ingrese el identificador de un camión y le mostrará la cantidad total de kilos descargados.')
        print('2 - Ingrese un dia y le mostrará un listado de datos.')
        print('3 - Ingrese nueva carga.')
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( 0 <= op <= 3 ):
                band = True
            else:
                print('\nLa opción ingresada es incorrecta.\n')
        menu.opcion(op, Camiones, Cosechas)
        salir = op == 0