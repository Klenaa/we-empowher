import streamlit as st 
import pandas as pd
import numpy as np

header = st.write()


st.set_page_config(page_title="We Empowher", page_icon=":sparkles:", layout="centered", initial_sidebar_state="auto", menu_items=None)

with header:
    st.title("We EmpowHer: Hackathon")
    st.text("Dans le cadre du Hackathon")


with dataset:
    st.header("Verbatim Dataset")

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

location_dist = pd.DataFrame(data['satisfaction cpam'].value_counts())
st.bar_chart(location_dist)

st.markdown('*First*: i know')


with model_training:
    st.header("here is a header")

    selection_column, disp_col = st.columns(2)
    max_depth = selection_column.slider("What should be the max", min_value = 10, max_value=100)
    variable = selection_column.selectbox('How Many tree should be used ?', option = [100,200,300, "No Limits"])
    input_feature = selection_column.text_input("question" )

