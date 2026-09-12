import streamlit as st
import pandas as pd

def render_upload():
    st.sidebar.header("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            st.sidebar.success(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")
        except Exception as e:
            st.sidebar.error(f"Could not read file: {e}")