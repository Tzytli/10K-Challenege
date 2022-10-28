#!/usr/bin/env python
# coding: utf-8

# In[115]:


#tratamiento de datos
import pandas as pd
import numpy as np
import math as mat
import matplotlib.pyplot as plt
import numpy 
import seaborn as sb
from datetime import datetime


# In[116]:


#cargar datos
Awa=pd.read_csv("Municipios_con_sequias.csv")

Awa.head(25)


# In[114]:


una_fecha = '20/04/2019'
fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
print(fecha_dt)


# In[147]:


awita = Awa[Awa.Entidad.isin(['Nuevo León'])]
display(awita)


# In[183]:


piedata3=awita.groupby('31-01-03')['Nombre del Municipio'].count()
display(piedata3)


# In[184]:


piedata3=awita.groupby('31-12-07')['Nombre del Municipio'].count()
display(piedata3)


# In[185]:


grafi = piedata3.plot.bar(rot=0,figsize=(10, 7))
mt.plot()


# In[188]:


piedata6=awita.groupby('31-12-18')['Nombre del Municipio'].count()
display(piedata6)


# In[189]:


grafic = piedata6.plot.bar(rot=0,figsize=(10, 7))
mt.plot()


# In[186]:


grafic = piedata5.plot.bar(rot=0,figsize=(10, 7))
mt.plot()


# In[178]:


piedata4=awita.groupby('31-12-20')['Nombre del Municipio'].count()
display(piedata4)


# In[179]:


graf = piedata4.plot.bar(rot=0,figsize=(10, 7))
mt.plot()


# In[180]:


piedata5=awita.groupby('31-12-07')['Anormalmente Seco (D0)'].mean()
display(piedata5)


# In[132]:


graf=awita.groupby('Nombre del Municipio')['Anormalmente Seco (D0)' ].mean()


grafi = graf.plot.pie(rot=0,figsize=(15, 15))
mt.plot()


# In[131]:


graf=awita.groupby('Nombre del Municipio')['Sequía Severa (D2)' ].mean()


grafi = graf.plot.pie(rot=0,figsize=(15, 15))
mt.plot()


# In[130]:




graf=awita.groupby('Nombre del Municipio')['Sequía Extrema (D3)' ].mean()


grafi = graf.plot.pie(rot=0,figsize=(15, 15))
mt.plot()


# In[128]:



graf=awita.groupby('Nombre del Municipio')['Sequía Excepcional (D4)' ].mean()


grafi = graf.plot.pie(rot=0,figsize=(10, 10))
mt.plot()


# In[134]:


graf=awita.groupby('Nombre del Municipio')['Total (D0 a D4)' ].mean()


grafi = graf.plot.pie(rot=0,figsize=(15, 15))
mt.plot()


# In[110]:


awita.describe()


# In[39]:


#cargar datos
h2o=pd.read_csv("Temperatura_Promedio_NL.csv")

h2o.head(25)


# In[40]:


h2o.describe()


# In[41]:


h2o.dropna(inplace=True)


# In[42]:


h2o


# In[54]:


h2o.set_index('Año')


# In[82]:


h2o.plot(x='Año', y='ENE', kind='bar', use_index=True)


# In[83]:


h2o.plot(x='Año', y='FEB', kind='bar', use_index=True)


# In[84]:


h2o.plot(x='Año', y='MAR', kind='bar', use_index=True)


# In[85]:


h2o.plot(x='Año', y='ABR', kind='bar', use_index=True)


# In[96]:


h2o.plot(x='Año', y='MAY', kind='bar', use_index=True)


# In[87]:


h2o.plot(x='Año', y='JUN', kind='bar', use_index=True)


# In[88]:


h2o.plot(x='Año', y='JUL', kind='bar', use_index=True)


# In[89]:


h2o.plot(x='Año', y='AGO', kind='bar', use_index=True)


# In[90]:


h2o.plot(x='Año', y='SEP', kind='bar', use_index=True)


# In[91]:


h2o.plot(x='Año', y='OCT', kind='bar', use_index=True)


# In[92]:


h2o.plot(x='Año', y='NOV', kind='bar', use_index=True)


# In[93]:


h2o.plot(x='Año', y='DIC', kind='bar', use_index=True)


# In[143]:


h2o.plot(x='Año', y='ANUAL', kind='bar', use_index=True)

