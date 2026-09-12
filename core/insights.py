from core.ai import generate_ai_response


def build_summary_for_insights(df):
    """
    Builds a factual, Pandas-calculated summary of the dataset.
    No AI is involved in this step — only real statistics.
    """
    lines = []
    lines.append(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    lines.append(f"Column names and types: " +
                 ", ".join([f"{col} ({dtype})" for col, dtype in df.dtypes.items()]))

    numeric_df = df.select_dtypes(include="number")
    if not numeric_df.empty:
        lines.append("\nNumeric column statistics:")
        for col in numeric_df.columns:
            lines.append(
                f"- {col}: mean={numeric_df[col].mean():.2f}, "
                f"min={numeric_df[col].min()}, max={numeric_df[col].max()}"
            )

    categorical_df = df.select_dtypes(include="object")
    if not categorical_df.empty:
        lines.append("\nCategorical column information:")
        for col in categorical_df.columns:
            top_value = df[col].mode()[0] if not df[col].mode().empty else "N/A"
            lines.append(
                f"- {col}: {df[col].nunique()} unique values, "
                f"most common = '{top_value}'"
            )

    return "\n".join(lines)


def generate_insights(df):
    """
    Sends a factual Pandas-calculated summary to Gemini and asks it to
    explain the data in plain language. Gemini never calculates numbers
    itself — it only interprets numbers we already computed.
    """
    if df is None or df.empty:
        return "Error: The dataset is empty, so no insights can be generated."

    summary = build_summary_for_insights(df)

    prompt = f"""You are a data analyst. Based only on the dataset statistics
provided below, identify the most important insights. Do not invent
information that is not supported by these statistics. Give 4-6 concise
insights in simple language, as a bullet list.

Dataset statistics:
{summary}
"""

    response = generate_ai_response(prompt)
    return response