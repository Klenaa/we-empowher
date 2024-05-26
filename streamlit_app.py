import streamlit as st 
import pandas as pde
import numpy as np

st.title("Dashboard")

st.set_page_config(page_title = "Mail Extracts", layout = "wide")
df = pd.read_csv("data/extract_mail.csv")

st.dataframe(df, height=1500)