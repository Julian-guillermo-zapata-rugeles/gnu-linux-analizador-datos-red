import os

def obtenerRutaDatos():
    os.chdir(os.path.dirname(__file__))
    return os.getcwd().replace("modulos","datos/")
