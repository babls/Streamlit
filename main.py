import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.title('Hello world')
st.markdown("---")
uploaded_files = st.file_uploader("Choose a excel file",type=["xlsx"], accept_multiple_files=True)
for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        st.markdown("---")
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        # To read file as string:
        #   string_data = stringio.read()
        #   st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        # dataframe = pd.read_csv(uploaded_file, sep=';')
        dataframe2 = pd.read_excel(uploaded_file, sheet_name=1)
        st.table(dataframe2)