import json
from core.ai import generate_ai_response


def build_dataset_context(df):
    """Builds a short text summary of the dataset for Gemini — not the full data."""
    columns_info = ", ".join([f"{col} ({str(dtype)})" for col, dtype in df.dtypes.items()])
    return f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns. Columns: {columns_info}."


def interpret_question(question, df):
    """
    Asks Gemini to convert the user's question into a simple JSON instruction.
    Gemini does NOT calculate anything here — it only labels what kind of
    analysis is needed. Returns a Python dict, or None if parsing fails.
    """
    context = build_dataset_context(df)

    prompt = f"""
You are helping convert a question about a dataset into a simple JSON instruction.

Dataset info: {context}

Question: "{question}"

Reply with ONLY a JSON object (no explanation, no markdown) in this exact format:
{{"operation": "<one of: count_rows, count_columns, average, maximum, minimum, sum, groupby_highest, groupby_lowest, unclear>", "column": "<column name or null>", "group_column": "<column name or null>"}}

Rules:
- operation must be exactly one of the listed options.
- column and group_column must be actual column names from the dataset, or null.
- If the question cannot be matched to these operations, use "operation": "unclear".
"""

    raw_response = generate_ai_response(prompt)

    if raw_response.startswith("Error:"):
        return None

    try:
        cleaned = raw_response.strip().strip("```json").strip("```").strip()
        intent = json.loads(cleaned)
        return intent
    except Exception:
        return None


def run_analysis(df, intent):
    """
    Performs the actual analysis using safe, predefined Pandas operations only.
    No AI-generated code is ever executed here.
    """
    operation = intent.get("operation")
    column = intent.get("column")
    group_column = intent.get("group_column")

    if operation == "count_rows":
        return f"The dataset has {df.shape[0]} rows."

    if operation == "count_columns":
        return f"The dataset has {df.shape[1]} columns."

    if column and column not in df.columns:
        return f"Sorry, I couldn't find a column named '{column}' in the dataset."

    if operation == "average":
        return f"The average {column} is {df[column].mean():.2f}."

    if operation == "maximum":
        return f"The maximum {column} is {df[column].max()}."

    if operation == "minimum":
        return f"The minimum {column} is {df[column].min()}."

    if operation == "sum":
        return f"The total {column} is {df[column].sum()}."

    if operation == "groupby_highest":
        if group_column not in df.columns:
            return f"Sorry, I couldn't find a column named '{group_column}' in the dataset."
        result = df.groupby(group_column)[column].sum().idxmax()
        value = df.groupby(group_column)[column].sum().max()
        return f"'{result}' has the highest total {column} ({value})."

    if operation == "groupby_lowest":
        if group_column not in df.columns:
            return f"Sorry, I couldn't find a column named '{group_column}' in the dataset."
        result = df.groupby(group_column)[column].sum().idxmin()
        value = df.groupby(group_column)[column].sum().min()
        return f"'{result}' has the lowest total {column} ({value})."

    return "Sorry, I couldn't determine the required analysis. Try asking about the average, maximum, minimum, total, or highest-performing category."


def answer_question(df, question):
    """
    Full flow: interpret the question, run safe Pandas analysis, return the answer.
    """
    intent = interpret_question(question, df)

    if intent is None or intent.get("operation") == "unclear":
        return "Sorry, I couldn't determine the required analysis. Try asking about the average, maximum, minimum, total, or highest-performing category."

    return run_analysis(df, intent)