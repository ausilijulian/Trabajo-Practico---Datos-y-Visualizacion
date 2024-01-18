import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
cupM=pd.read_csv('C:/Users/rjaus/Downloads/cuatri2/PA/WorldCupMatches.csv')
cupP=pd.read_csv('C:/Users/rjaus/Downloads/cuatri2/PA/WorldCupPlayers.csv')
cup=pd.read_csv('C:/Users/rjaus/Downloads/cuatri2/PA/WorldCups.csv')


fig,ax=plt.subplots(2,1,figsize=(12,10))

#aca hago un ciclo para quedarme con los datos del campeon de cada mundial
i=0
golescampeon=[]
while i<len(cup['Winner']):
    a=cupM.loc[(cupM['Home Team Name'] == cup['Winner'][i]) & (cup['Year'][i] == cupM['Year'])]
    b=cupM.loc[(cupM['Away Team Name'] == cup['Winner'][i]) & (cup['Year'][i] == cupM['Year'])]
    a=a['Home Team Goals'].sum()
    b=b['Away Team Goals'].sum()
    golescampeon.append(a+b)
    i=i+1


#aca me di cuenta que el dato del ultimo mundial era erroneo, y a raiz de eso
#me di cuenta que la tabla tenia valores duplicados
golescampeon[19]=18 #dato real


sns.barplot(x="Year", y=golescampeon,data=cup, palette='bright',saturation=3,hue='Winner',width=0.8,ax=ax[0],dodge=False)
#use el dodge que no se bien que hace, pero me ayudo porque a poner el hue las barras se me corrian de eje y se achicaban

ax[0].set_title('Goles anotados en el mundial y su campeon')
ax[0].set_xlabel('Año')
ax[0].set_ylabel('Goles anotados')
ax[0].grid(True)
ax[0].legend(loc=0)




rio=cupM.loc[cupM['City'] == 'Rio De Janeiro '].reset_index(drop = True)
rio['Goles']=rio['Home Team Goals']+rio['Away Team Goals']
rio['Partido']=rio['Home Team Initials']+'-'+rio['Away Team Initials']
sns.scatterplot(x="Partido", y="Goles", hue="Datetime", data=rio,palette='husl',ax=ax[1])
ax[1].set(ylim=(0,10))
ax[1].set_title('Goles en partidos en Rio de Janeiro')
ax[1].grid(True)
ax[1].legend(loc=1,fontsize='x-small')
ax[1].set_yticks(np.arange(0,10))



#filtrado de capitanes con camiseta numero 10
capitanes=cupP.loc[cupP['Shirt Number'] == 10].loc[cupP['Position'] == 'C'].reset_index(drop = True)

plt.show()