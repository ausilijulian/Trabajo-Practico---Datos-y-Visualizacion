import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
ds=pd.read_csv('C:/Users/rjaus/Downloads/cuatri2/PA/covid-vaccination-doses-per-capita.csv')

fig, ax = plt.subplots(figsize=(13,5))

ds['dia']=pd.DatetimeIndex(ds['Day']).day
arg=ds.loc[ds['Entity'] == "Argentina"].reset_index(drop = True) #selecciono solo los datos de argentina


x = arg.loc[arg['dia']==1] #selecciono solo un dia del mes para hacer el intervalo cada un mes
y = x['total_vaccinations_per_hundred']
x = x['Day'] #convierto la x en la columna con las fechas(que solo tiene los dia 1 de mes)

x=pd.DatetimeIndex(x).month.astype(str)+'-'+pd.DatetimeIndex(x).year.astype(str) #me quedo solo con el mes y el año para que el indice no se superponga


ax.set_title('Incremento en la vacunacion en Argentina')
ax.set_ylabel('Poblacion Percapita')
ax.set_xlabel('Mes')
ax.grid(True)

ax.plot(x, y,'c--')
plt.show()


