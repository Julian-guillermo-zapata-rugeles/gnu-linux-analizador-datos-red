"""
Este módulo tiene como objetivo retornar rutas asociadas o necesarias
al modulo gestor

"""

import os

def obtenerRutaDatos():
    os.chdir(os.path.dirname(__file__))
    return os.getcwd().replace("modulos","datos/")
