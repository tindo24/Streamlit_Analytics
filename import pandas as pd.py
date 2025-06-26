import pandas as pd
import plotly.express as px
df= pd.read_csv('iris.csv')
print(df.columns)
plot = px.scatter(data_frame=df,
                  size='sepal_width',
                  x = 'sepal_length', color='species',
                  facet_col='species',
                  y = 'petal_length',
                  title= ' Plot of Sepal length vs Petal length')

plot.show()