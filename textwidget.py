# text widget in streamlit
import streamlit as st
import datetime
st.markdown('# Mark donw display')
st.markdown('## Mark donw display')
st.markdown('### Mark donw display')

st.header(' Header')
st.text( ' This is text ')
st.subheader('Sub header')
st.caption ( 'This is a caption ')

# display code 
code_snippet = """ 
def greet(name):
    return  f"hello, {name}!"
    """
st.code(code_snippet, language='python')
my_list = [1,3,3]
st.write(my_list)

st.header( " All about dropdown")
car_manufucture = ['Ford', 'Lexus', 'Toyota', 'VW', 'Audi']

selected_car = st.selectbox(label='Car Manufucturer',
                            options=car_manufucture, 
                            key='U1', index=3)

st.header ( "Multiselect")

my_fav = st.multiselect( label='Select Favourites', options=car_manufucture)

st.header(" Slider widget")
basic_slider = st.slider(label = 'basic label',
                         min_value= 1, max_value= 100, 
                         value=50)
st.write('selected number: {}'.format(basic_slider))

st.header('range slider')
range_slider = st.slider(label = 'basic label',
                         min_value= 1, max_value= 100, value=(50,75))
st.write('selected number: {}'.format(range_slider))

# number input parameter
number_input = st.number_input(
    label='Enter a number',
    min_value= 0 ,
    max_value=100,
    value= 50, # default value
    step= 1, # increment step
    help='Use this widget to input number.',
    label_visibility='visible'
)

side_bar_number = st.sidebar.number_input(label='Number in sidebar',
                                          min_value= 5,
                                          max_value=100,
                                          step= 5,
                                          value=30,
                                          label_visibility='visible')


st.header( "forms in streamlit")
#add form in area 
form = st.form(key='form1', clear_on_submit=False, enter_to_submit=True, border=True)

form.selectbox(label='Current State',options=['TX','NM','NV',])
form.form_submit_button(label='SUBMIT DETAILS')