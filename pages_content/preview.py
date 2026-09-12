import streamlit as st

def render_preview():
    st.header("👀 Dataset Preview")

    if "df" in st.session_state:
        df = st.session_state.df

        col1, col2 = st.columns(2)
        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])

        st.subheader("First 10 Rows")
        st.dataframe(df.head(10), use_container_width=True)

        st.subheader("Column Data Types")
        dtype_df = df.dtypes.astype(str).reset_index()
        dtype_df.columns = ["Column", "Data Type"]
        st.dataframe(dtype_df, use_container_width=True)

    else:
        st.info("Please upload a CSV file from the sidebar to see the preview.")