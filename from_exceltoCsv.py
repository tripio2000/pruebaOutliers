import pandas as pd
import seaborn as sn
#Leemos el excel.
data  = pd.read_excel("/home/nicolas/interbrain/Datos frutas.xlsx")
#Lo transformamos a csv y lo escribimos como csv.
data.to_csv (r'/home/nicolas/interbrain/datos_frutas.csv', index = None, header=False)
datos = pd.read_csv("/home/nicolas/interbrain/datos_frutas.csv",header = 2)
#datos.head()
#Creamos una copia de los datos
datos1 = datos
#Cargamos las columnas que queremos eliminar
cols = [5,6]
#Eliminamos las columnas en el dataset copia
datos1.drop(datos1.columns[cols],axis = 1, inplace = True)
#Ahora borramos la fila 0 porque tiene datos sobre unidades que no necesitamos
datos1.drop(labels = [0],axis = 0,inplace = True)
datos1.to_csv("/home/nicolas/interbrain/duraznosfinal.csv")
print(datos1.head())