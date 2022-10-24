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
    datos=pd.read_fwf('clusters_report.txt', widths=[9, 16, 16, 76], skiprows=4, names=nombrescol)
    reg1=[]
    for i in range(0,51):
        reg2=reg1.append(datos.iat[i,3])
    pega=' '
    Res1final1=pega.join(reg1[0:4])
    Res1final2=pega.join(reg1[4:9])
    Res1final3=pega.join(reg1[9:12])
    Res1final4=pega.join(reg1[12:16])
    Res1final5=pega.join(reg1[16:20])
    Res1final6=pega.join(reg1[20:24])
    Res1final7=pega.join(reg1[24:28])
    Res1final8=pega.join(reg1[28:32])
    Res1final9=pega.join(reg1[32:36])
    Res1final10=pega.join(reg1[36:40])
    Res1final11=pega.join(reg1[40:42])
    Res1final12=pega.join(reg1[42:47])
    Res1final13=pega.join(reg1[47:51])

    resttotal=[Res1final1, Res1final2,Res1final3, Res1final4, Res1final5, Res1final6, Res1final7, Res1final8, Res1final9, Res1final10, Res1final11, Res1final12, Res1final13]
    datosprueba=datos.copy()
    datosprueba=datosprueba.drop([1, 2, 3, 5 ,6, 7, 50, 8, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 43, 44, 45, 46, 48, 49],axis=0)
    claves=datosprueba.index.values
    valores= list(range(13))
    dict_from_list = dict(zip(claves, valores))
    datosprueba=datosprueba.rename(index= dict_from_list)
    for i in range(0,13):
        datosprueba.iat[i,3]= resttotal[i]
    datosprueba['porcentaje_de_palabras_clave']=datosprueba.porcentaje_de_palabras_clave.apply(lambda x: x.replace(',', '.')).apply(lambda x: x.replace(' %', ''))
    datosprueba['principales_palabras_clave']=datosprueba.principales_palabras_clave.apply(lambda x: x.replace('    ', ' ')).apply(lambda x: x.replace('  ', ' '))

    return datosprueba
