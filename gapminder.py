# Gap minder dashboard
import  pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
# page title
st.markdown('#  Gapminder Dashboard')

df = pd.read_csv('gapminder_data_graphs.csv')

# Computation 
unique_years = df['year'].unique()

# add dropdwon
selected_year = st.selectbox(label= 'Year',
                             options=unique_years)
# This sets up the year as a filter in the selectbox that will affect the whole dashboard
df_plot = df[df['year']== selected_year]

# This displays dataframe table
#st.write(df_plot)

# add the averageds 
average_gdp = round(df_plot['gdp'].mean(),2)
average_life_exp = round(df_plot['life_exp'].mean(),2)
average_hdi = round(df_plot['hdi_index'].mean(), 2)

# create 3 column arrangment 

col1, col2, col3 = st.columns([1,1,1])
# add metric widget to different column
col1.metric(label=' Average GDP', value=average_gdp)
col2.metric(label='AVG Life Expentancy', value=average_life_exp)
col3.metric(label='AVG HDI Index',value=average_hdi)

# Add scatter plot
title = 'Plot of GDP vs Life Expectancy for year {}'. format(selected_year)
scatter_plot = px.scatter(data_frame=df_plot,
                          x = 'gdp',
                          y='life_exp',
                          color='continent',
                          title=title)
# call the chat 
st.plotly_chart(scatter_plot)

# add two plots (gdp by continent  and distributionof gdp by continent. Box plot and bar chart)
# step 1 create 2 columns 
colbox, colbar = st.columns([1,1])
# add box plot to colbox
title_box = 'Distribution of GDP accross different continents for the year {}'. format(selected_year)
colbox = px.box(data_frame=df_plot,
                x='continent',
                y='gdp',
                title=title_box)
st.plotly_chart(colbox)

# add bar chart
title_bar = 'Distribution of GDP accross different continents for the year {}'. format(selected_year)
colbar = px.bar(data_frame=df_plot,
                x='gdp',
                title=title_bar)
st.plotly_chart(colbar)