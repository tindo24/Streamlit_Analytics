import pandas as pd
import plotly.express as px

df =  pd.read_csv('iris.csv')
print(df.head())

group1 = df.groupby(['species']).mean().reset_index()
print(group1)
plot = px.bar(data_frame=group1,
              x = 'species',
              y='petal_width',
              title= 'Petal Width Average')
plot.show()