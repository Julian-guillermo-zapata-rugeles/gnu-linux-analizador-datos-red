"""
Gestor Principal

Utilizar mediante llamados simples a los modulos que gestionarán las pruebas de red
El objetivo será generar un archivo de texto para crear un análisis periodico de conectividad
estas incluyen el punto de acceso que se está empleando durante la prueba y velocidad de subida y bajada
Dichos datos se usarán para la futura predicción mediante IA y el reconocimiento de patrones asociados a los hábitos de red
de los dispositivos almacenados.

Pruebas disponibles actualmente:
    ----------------------------------------------------------------------
    Recolección del [ punto de Acceso , ms , bajada , subida ]
        (PruebaBasica) <function call on pruebas> pruebas.PruebaBasica()
    ----------------------------------------------------------------------

"""

from modulos import rutas
from modulos import pruebas

RUTA_DATOS = rutas.obtenerRutaDatos()
