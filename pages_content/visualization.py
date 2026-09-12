import streamlit as st
import plotly.express as px

def render_visualization():
    st.header("Data Visualization")
    if "cleaned_df" in st.session_state:
        df = st.session_state.cleaned_df

        chart_type = st.selectbox(
            "Select chart type",
            ["Bar Chart", "Line Chart", "Pie Chart", "Histogram", "Scatter Plot"]
        )

        numeric_cols = list(df.select_dtypes(include="number").columns)
        categorical_cols = list(df.select_dtypes(include="object").columns)

        if chart_type in ["Bar Chart", "Pie Chart"]:
            if categorical_cols:
                column = st.selectbox("Select a categorical column", categorical_cols)
                counts = df[column].value_counts().reset_index()
                counts.columns = [column, "count"]

                if chart_type == "Bar Chart":
                    fig = px.bar(counts, x=column, y="count")
                else:
                    fig = px.pie(counts, names=column, values="count")

                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No categorical columns available for this chart type.")

        elif chart_type == "Histogram":
            if numeric_cols:
                column = st.selectbox("Select a numeric column", numeric_cols)
                fig = px.histogram(df, x=column)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No numeric columns available for a histogram.")

        elif chart_type == "Line Chart":
            if numeric_cols:
                column = st.selectbox("Select a numeric column", numeric_cols)
                fig = px.line(df, y=column)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No numeric columns available for a line chart.")

        elif chart_type == "Scatter Plot":
            if len(numeric_cols) >= 2:
                x_col = st.selectbox("Select X-axis column", numeric_cols, key="scatter_x")
                y_col = st.selectbox("Select Y-axis column", numeric_cols, key="scatter_y")
                fig = px.scatter(df, x=x_col, y=y_col)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("Need at least two numeric columns for a scatter plot.")
    else:
        st.info("Please upload and clean a dataset first to see visualizations.")