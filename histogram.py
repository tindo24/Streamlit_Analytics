import pandas as pd
import plotly.express as px
df= pd.read_csv('iris.csv')
print(df.columns)

plot = px.histogram(data_frame=df,
                    x ='sepal_length', nbins=8, color='species',
                    title=' Histogram of sepal length')
plot.show()