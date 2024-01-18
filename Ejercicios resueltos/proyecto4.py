import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ds=pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')
ds=ds.drop(columns=['zn','indus','chas','nox','rm','age','dis','rad','b',])


fig, ax = plt.subplots(2, 2, figsize=(11, 11))

x=ds['medv']
y_crim=ds['crim']
y_lstat=ds['lstat']
y_tax=ds['tax']
y_ptratio=ds['ptratio']

ax[0,0].set_title('Precio vs Crimen')
ax[0,1].set_title('Precio vs Bajos ingresos')
ax[1,0].set_title('Precio vs Impuestos')
ax[1,1].set_title('Precio vs Cantidad de maestros por alumno')

ax[0,0].set_xlabel('valor promedio vivienda ($1000)')
ax[0,1].set_xlabel('valor promedio vivienda ($1000)')
ax[1,0].set_xlabel('valor promedio vivienda ($1000)')
ax[1,1].set_xlabel('valor promedio vivienda ($1000)')

ax[0,0].set_ylabel('Crimen Per capita')
ax[0,1].set_ylabel('% de población con bajos ingresos')
ax[1,0].set_ylabel('impuesto a la propiedad valor total $10,000')
ax[1,1].set_ylabel('Cantidad de maestros por alumno')


ax[0,0].grid(True)
ax[0,1].grid(True)
ax[1,0].grid(True)
ax[1,1].grid(True)

#elegi este tipo de grafico para mostrar la distribucion, ya que hay datos en algunas columnas que son un poco
#desproporcionados,por eso elegi este tipo de histograma para que muestre bien donde hay mas datos distribuidos

sns.kdeplot(x=x, y=y_crim, data=ds,fill=True,ax=ax[0,0])
sns.kdeplot(x=x, y=y_lstat, data=ds,fill=True,ax=ax[0,1], color="g")
sns.kdeplot(x=x, y=y_tax, data=ds,fill=True,ax=ax[1,0], color="c")
sns.kdeplot(x=x, y=y_ptratio, data=ds,fill=True,ax=ax[1,1], color="m")



plt.show()

