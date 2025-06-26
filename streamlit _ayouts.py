# streamlit layouts
import streamlit as st
tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

# how to control tabl
with tab1:
    st.header(" this is tab 1")

with tab2:
    st.header(" this is tab 2")
with tab3:
    st.header(" this is tab 3")
