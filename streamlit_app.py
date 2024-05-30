import streamlit as st 
import pandas as pd
import numpy as np
import time as time

header = st.write()


st.set_page_config(page_title="We Empowher", page_icon=":sparkles:", layout="centered", initial_sidebar_state="auto", menu_items=None)


st.title("We EmpowHer: Hackathon")
st.text("Dans le cadre du Hackathon")



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



st.header("here is a header")

selection_column, disp_col = st.columns(2)

col1, col2 = st.columns([1,2])

col1.markdown(" #Welcome to my app!")

# function: file_uploader
# .success("")

# progress bar : .progress(0)



col2.success("ALRIGHT ! ")

col2.metric(label="# of Mails", value = "566k", delta = "3 °C")


with st.expender("click to read more"):
    st.write("Helllo, some details")