import pandas as pd
import plotly.express as px
import streamlit as st 

st.set_page_config(layout='wide')
st.title('Auto MPG Dashboard')

df = pd.read_csv('clean_auto_mpg.csv')

# create a unique origin list 
unique_origin = list(df['origin'].unique())
# sort the origin list 
unique_origin.sort()

# create a comprehension list to add string to list 
unique_origin_str = ['Origin: ' + str(origin) for origin in unique_origin]
print( unique_origin)
print( unique_origin_str)

# create tabs 
tab1, tab2, tab3 = st.tabs([unique_origin_str[0],
                            unique_origin_str[1],
                            unique_origin_str[2]])

# define operation in different tabs 

with tab1:
    st.subheader(unique_origin_str[0])
    #create columns 
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    col5, col6 = st.columns([4,1])
    #get data with origin 1
    df_tab = df[df['origin'] == unique_origin[0]]
    #calculate the metrics 
    avg_mpg = round(df_tab['mpg'].mean(),1)
    avg_disp = round(df_tab['displacement'].mean(),1)
    avg_hp = round(df_tab['horsepower'].mean(),1)
    avg_wt = round(df_tab['weight'].mean(),1)

    # call the metric functionwidget for the widget to appear
    col1.metric(label='Avg MPG', value=avg_mpg)
    col2.metric(label='Avg Displacement', value=avg_disp)
    col3.metric(label='Avg Horsepower', value=avg_hp)
    col4.metric(label='Avg weight', value=avg_wt)

    # add 2 columns for scatter plot and histogram

col5.write( " This is for scatter plot")
col6.write( "This is for bar char")

# define scatter plot 
scatter = px.scatter(data_frame=df_tab,
           x= 'weight',
           y='horsepower',
           size='displacement',
           hover_name='car name',
           color='cylinders',
           title='Weight vs HP for cars from {}'.format(unique_origin[0]))
# call the scatter plot
col5.plotly_chart(scatter)

# add the histogram
histogram_plot = px.histogram(data_frame=df_tab,
                              x='mpg',
                              title='MPG Distribution')
# call the histogram chart
col6.plotly_chart(histogram_plot)

with tab2:
    st.subheader(unique_origin_str[1])
    #create columns 
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    col5, col6 = st.columns([4,1])
    #get data with origin 1
    df_tab = df[df['origin'] == unique_origin[1]]
    #calculate the metrics 
    avg_mpg = round(df_tab['mpg'].mean(),1)
    avg_disp = round(df_tab['displacement'].mean(),1)
    avg_hp = round(df_tab['horsepower'].mean(),1)
    avg_wt = round(df_tab['weight'].mean(),1)

    # call the metric functionwidget for the widget to appear
    col1.metric(label='Avg MPG', value=avg_mpg)
    col2.metric(label='Avg Displacement', value=avg_disp)
    col3.metric(label='Avg Horsepower', value=avg_hp)
    col4.metric(label='Avg weight', value=avg_wt)

    # add 2 columns for scatter plot and histogram

col5.write( " This is for scatter plot")
col6.write( "This is for bar char")

# define scatter plot 
scatter = px.scatter(data_frame=df_tab,
           x= 'weight',
           y='horsepower',
           size='displacement',
           hover_name='car name',
           color='cylinders',
           title='Weight vs HP for cars from {}'.format(unique_origin[1]))
# call the scatter plot
col5.plotly_chart(scatter)

# add the histogram
histogram_plot = px.histogram(data_frame=df_tab,
                              x='mpg',
                              title='MPG Distribution')
# call the histogram chart
col6.plotly_chart(histogram_plot)
with tab3:
    st.subheader(unique_origin_str[2])
    #create columns 
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    col5, col6 = st.columns([4,1])
    #get data with origin 1
    df_tab = df[df['origin'] == unique_origin[2]]
    #calculate the metrics 
    avg_mpg = round(df_tab['mpg'].mean(),1)
    avg_disp = round(df_tab['displacement'].mean(),1)
    avg_hp = round(df_tab['horsepower'].mean(),1)
    avg_wt = round(df_tab['weight'].mean(),1)

    # call the metric functionwidget for the widget to appear
    col1.metric(label='Avg MPG', value=avg_mpg)
    col2.metric(label='Avg Displacement', value=avg_disp)
    col3.metric(label='Avg Horsepower', value=avg_hp)
    col4.metric(label='Avg weight', value=avg_wt)

    # add 2 columns for scatter plot and histogram

col5.write( " This is for scatter plot")
col6.write( "This is for bar char")

# define scatter plot 
scatter = px.scatter(data_frame=df_tab,
           x= 'weight',
           y='horsepower',
           size='displacement',
           hover_name='car name',
           color='cylinders',
           title='Weight vs HP for cars from {}'.format(unique_origin[2]))
# call the scatter plot
col5.plotly_chart(scatter)

# add the histogram
histogram_plot = px.histogram(data_frame=df_tab,
                              x='mpg',
                              title='MPG Distribution')
# call the histogram chart
col6.plotly_chart(histogram_plot)


