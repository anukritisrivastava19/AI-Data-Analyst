import streamlit as st
import pandas as pd

def render_cleaning():
    st.header("Data Cleaning")
    if "df" in st.session_state:
        df = st.session_state.df

        st.subheader("Missing Values per Column")
        st.write(df.isnull().sum())

        st.subheader("Duplicate Rows")
        st.write("Number of duplicate rows:", df.duplicated().sum())

        col1, col2 = st.columns(2)
        remove_dup = col1.button("Remove Duplicate Rows")
        remove_missing = col2.button("Remove Rows with Missing Values")

        date_column = st.selectbox("Select a date column to convert (optional)", ["None"] + list(df.columns))
        convert_date = st.button("Convert to Date")

        if "cleaned_df" not in st.session_state:
            st.session_state.cleaned_df = df.copy()

        if remove_dup:
            st.session_state.cleaned_df = st.session_state.cleaned_df.drop_duplicates()

        if remove_missing:
            st.session_state.cleaned_df = st.session_state.cleaned_df.dropna()

        if convert_date and date_column != "None":
            st.session_state.cleaned_df[date_column] = pd.to_datetime(
                st.session_state.cleaned_df[date_column], errors="coerce"
            )

        cleaned = st.session_state.cleaned_df

        st.subheader("Cleaned Dataset")
        st.dataframe(cleaned)

        st.subheader("Summary")
        m1, m2, m3 = st.columns(3)
        m1.metric("Rows Before", df.shape[0])
        m2.metric("Rows After", cleaned.shape[0])
        m3.metric("Duplicates Removed", df.duplicated().sum())
    else:
        st.info("Please upload a CSV file to clean the dataset.")