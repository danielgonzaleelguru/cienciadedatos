import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
 

workbook="data.xlsx"
df=pd.read_excel(workbook)

newDatos= df[(df['Duracion']>=5) & (df['Duracion']<=6)]
print(newDatos)

newDatos['Fecha2'] = None
newDatos['Hora'] = None
print(newDatos)

def getDateColumn(x):
    return x.split(" ")[0]

def getTimeColumn(x):
    return x.split(" ")[1].split(":")[0]

newDatos['Fecha2']=newDatos['Fecha'].apply(getDateColumn)
newDatos['Hora']=newDatos['Fecha'].apply(getTimeColumn)

df3=newDatos.groupby(['Fecha2','Hora'])['Valor'].sum()

ax = df3.plot(kind='line', title='Curva de Vólumenes Acumulados o Masa Lluvia', figsize=(10, 6))
ax.set_ylabel("Valores acumulados de agua")
ax.set_xlabel("Hora del Día")
ax.legend(loc="upper left")
plt.show()
