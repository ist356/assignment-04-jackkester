'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py

file = st.file_uploader("Upload a file", type = ['xlsx', 'csv', 'json'])
if file: 
    extent = pl.get_file_extension(file.name)
    loaded = pl.load_file(file, extent)
    df = pd.DataFrame(loaded)
    cols = pl.get_column_names(df)
    col_input = st.multiselect("Select columns to display", cols, default=cols) 

    if st.toggle("Filter Data"):
        optcols = st.columns(3)
        better_cols = pl.get_columns_of_type(df, 'object')
        col_option = optcols[0].selectbox("Pick your columns", better_cols)
        if col_option:
            unique_vals = pl.get_unique_values(df, col_option)
            value_option = optcols[1].selectbox("Select a value to filter on", unique_vals)
        st.dataframe(df[df[col_option] == value_option][col_input])
        st.dataframe(df[df[col_option] == value_option][col_input].describe())
    else:
        st.dataframe(df[col_input])
        st.dataframe(df[col_input].describe())
    
    

    
