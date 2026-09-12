import streamlit as st
from core.insights import generate_insights

def render_insights():
    st.header("🤖 AI-Powered Insights")
    st.write("Let AI identify important patterns and observations from your dataset.")

    if "cleaned_df" not in st.session_state:
        ...

    if "cleaned_df" not in st.session_state:
        st.info("Please upload and clean a dataset first.")
        return

    df = st.session_state.cleaned_df

    if df.empty:
        st.warning("The cleaned dataset is empty. Nothing to analyze.")
        return

    st.write("Click the button below to generate AI insights based on your cleaned dataset.")

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing your data and generating insights..."):
            insights = generate_insights(df)

        if insights.startswith("Error:"):
            st.error(insights)
        else:
            st.success("Here are your insights:")
            st.write(insights)