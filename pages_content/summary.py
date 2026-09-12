import streamlit as st

def render_summary():
    st.header("📊 Data Summary & Statistical Analysis")

    if "cleaned_df" in st.session_state:
        df = st.session_state.cleaned_df

        numeric_df = df.select_dtypes(include="number")
        categorical_df = df.select_dtypes(include="object")

        st.subheader("Basic Dataset Information")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Rows", df.shape[0])
        m2.metric("Columns", df.shape[1])
        m3.metric("Numerical Columns", numeric_df.shape[1])
        m4.metric("Categorical Columns", categorical_df.shape[1])

        st.subheader("📊 Numerical Summary")
        if not numeric_df.empty:
            st.dataframe(numeric_df.describe(), use_container_width=True)
        else:
            st.write("No numerical columns found.")

        st.subheader("🏷️ Categorical Information")
        if not categorical_df.empty:
            for col in categorical_df.columns:
                st.write(f"**{col}** — Unique values:", df[col].nunique())
                st.write("Most common value:", df[col].mode()[0])
        else:
            st.write("No categorical columns found.")

        st.subheader("❓ Missing Values")
        missing_df = df.isnull().sum().reset_index()
        missing_df.columns = ["Column", "Missing Values"]
        st.dataframe(missing_df, use_container_width=True)

        st.subheader("🔗 Correlation Matrix")
        if not numeric_df.empty and numeric_df.shape[1] > 1:
            st.dataframe(numeric_df.corr(), use_container_width=True)
        else:
            st.write("Not enough numerical columns to calculate correlation.")
    else:
        st.info("Please clean the dataset first to view the summary.")