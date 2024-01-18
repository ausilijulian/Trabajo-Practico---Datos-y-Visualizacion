import pandas as pd
import matplotlib.pyplot as plt
ds=pd.read_csv('C:/Users/rjaus/Downloads/cuatri2/PA/company_sales_data.csv')
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

x = ds['month_number']
y = ds['total_profit']

max= ds['total_profit'].max()
month=ds.loc[ds['total_profit'] == max] #busco el maximo de ganancias
month=month['month_number']  #busco que mes tuvo esas ganancias

#me di cuenta que en el dataset los datos de total de unidades estaba erroneo,
#pero como aca pedia la cantidad de ganancia y no la cantidad de productos, lo grafique con esos datos

ax[0].set_title('Ganancias segun el Mes')
ax[0].fill_between(x, y,color='0.6')
ax[0].plot(month,max, marker ="o",color='r')
ax[0].set_xlabel('Mes')
ax[0].set_ylabel('Ganancias')
ax[0].grid(True)

ax[1].plot(ds['facecream'], color = 'red', label = 'Face Cream')
ax[1].plot(ds['facewash'], color = 'green', label = 'Face Wash')
ax[1].plot(ds['toothpaste'], color = 'y', label = 'Tooth Paste')
ax[1].plot(ds['bathingsoap'], color = 'black', label = 'Bathing Soap')
ax[1].plot(ds['shampoo'], color = 'c', label = 'Shampoo')
ax[1].plot(ds['moisturizer'], color = 'magenta', label = 'Moisturizer')
ax[1].set_title('Ventas durante el Año')
ax[1].set_xlabel('Mes')
ax[1].set_ylabel('Cantidad')
ax[1].legend(loc='upper right')
ax[1].grid(True)

plt.show()
