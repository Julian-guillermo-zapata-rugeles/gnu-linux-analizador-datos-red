"""
Julián Guillermo Zapata Rugeles

El objetivo de este comando es ejecutar las pruebas necesarias
devolver una cadena usando una estructura definida para ser guardada

se retornarán cadenas de texto hacia el modulo invocador para luego llamar al escritor
que se encargará de crear el archivo o escribir en el
"""

import os


def PruebaBasica():
    comando_basico = "speedtest --simple --timeout 5"
    comando_leido=os.popen(comando_basico).read().split("\n")
    salida_comando=""
    if len(comando_leido)==4:
        for datos in comando_leido:
            salida_comando+=datos+";"
        salida_comando=salida_comando[:-1]
    else:
        salida_comando="0;0;0;"
    return salida_comando
