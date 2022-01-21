import pandas as pd
import numpy as np
def hayNaN(datos,columna):
    if(datos[columna].isna().values.any()):
        print(f"Hay NaN en la columna {columna}")
    else:
        print(f"No hay NaN en la columna {columna}")
def ClasificarOutliers(df,columna):
    #Creamos una serie vacia y la unimos al dataframe.
    clasif = pd.Series(dtype="int64")
    datosmod = pd.concat([df,clasif],axis=1)
    #Cambiar el nombre de la nueva columna
    datosmod.columns = [*datosmod.columns[:-1], 'Clasificacion']
    for i in range(len(datosmod[columna])):
        if(datosmod[columna][i] == 30 or datosmod[columna][i] == 20 or datosmod[columna][i] == 35 ): #Los outliers de este data set.
            datosmod["Clasificacion"][i] = 1
        else: #Sino son estos 3, entonces son 0
            datosmod["Clasificacion"][i] = 0
    return datosmod
def test():
    print("Me importe bien")
def ClasificarOutliersVect(vect):
    #Creamos una lista
    clasif = []
    #Iterar dentro de la serie, buscando si alguno coincide con la busqueda
    for i in range(0, len(vect)):
        if (vect.iloc[i].item() == 30 or vect.iloc[i].item() == 20 or vect.iloc[i].item() == 35): #Los outliers son los que pesan 35, 20, 30
            clasif.append(-1) #A los outliers le ponemos un -1
        else:
            clasif.append(1) #De otra manera les ponemos un 1
    return pd.Series(clasif) #Transformamos la lista en una serie de pandas.
def reemplazarNAxModa(datos,columna):
    #Calculamos la moda
      moda = datos[columna].mode()
    #Rellenamos los Na con la moda.
      datos[columna] = datos[columna].fillna(moda)
      return datos