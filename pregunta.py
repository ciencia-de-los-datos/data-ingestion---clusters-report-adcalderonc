"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    nombrescol="cluster,cantidad_de_palabras_clave,porcentaje_de_palabras_clave,principales_palabras_clave".split(',')
    datos=pd.read_fwf('clusters_report.txt', widths=[9, 16, 16, 76], skiprows=4, names=nombrescol, na_filter=False)
    #

    return datos
