"""
Julián Guillermo Zapata Rugeles

Este módulo se encarga de la escritura de datos en un archivo de texto dada una ruta
a travez del paso de argumento.


"""
def guardarInformacion(string_cadena , string_ruta_archivo , string_file_name):
    try:
        print("[escritura] guardando.")
        archivo = open((string_ruta_archivo+string_file_name),"a")
        archivo.write(string_cadena)
        archivo.write('\n')
        archivo.close()
        print("[escritura] correcto.")
    except Exception as e:
        print("No se puede continuar ",e)
