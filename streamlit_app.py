import streamlit as st 
import pandas as pd
import numpy as np



st.set_page_config(page_title="We Empowher", page_icon=":sparkles:", layout="centered", initial_sidebar_state="auto", menu_items=None)

DATA_URL = ("data/extract_satisfaction_verbatim.csv")

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)

data_load_state.text('Loading data...done!')

data