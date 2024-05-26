import streamlit as st 
import pandas as pd
import numpy as np

st.title("Dashboard")

df = pd.read_csv("extract_mail.csv")

st.dataframe(df, height=1500)