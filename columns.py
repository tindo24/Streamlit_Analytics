# elements within columns

import streamlit as st

# learn about columns
col1, col2, col3 = st.columns(3, gap='small',vertical_alignment='top')

with col1:
    st.header('Column 1')

with col2:
    st.header('Column 2')
with col3:
    st.header('Column 3')