import pandas as pd
import matplotlib.pyplot as plt
ds=pd.read_csv('C:/Users/rjaus/Downloads/cuatri2/PA/company_sales_data.csv')
fig, ax = plt.subplots(figsize=(5, 5))

ds=ds.drop(columns=['month_number','total_units','total_profit'])

sum=pd.DataFrame({'facecream': [ds['facecream'].sum()],'facewash': [ds['facewash'].sum()],
                  'toothpaste': [ds['toothpaste'].sum()],'bathingsoap': [ds['bathingsoap'].sum()],
                  'shampoo': [ds['shampoo'].sum()],'moisturizer': [ds['moisturizer'].sum()]})

ds = pd.concat([ds,sum])

plt.pie(ds.iloc[12], labels=ds.columns, autopct="%0.1f %%")

ax.set_title('Porcentaje de productos vendidos durante el año')

print(sum)
plt.show()

