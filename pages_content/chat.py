import streamlit as st
from core.qa import answer_question

def render_chat():
    st.header("💬 Ask Questions About Your Data")
    st.write("Ask questions about your uploaded dataset in plain English.")

    with st.expander("💡 Example questions"):
        st.write("- Which month had the highest sales?")
        st.write("- What is the average age?")
        st.write("- Which category has the highest value?")
        st.write("- How many records are present?")

    if "cleaned_df" not in st.session_state:
        st.info("Please upload and clean a dataset first to ask questions about it.")
        return
    ...

    if "cleaned_df" not in st.session_state:
        st.info("Please upload and clean a dataset first to ask questions about it.")
        return

    df = st.session_state.cleaned_df

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_input("Ask a question about your dataset:",
                              placeholder="Which category has the highest sales?")

    if st.button("🔍 Analyze"):
        if not question.strip():
            st.warning("Please enter a question first.")
        else:
            with st.spinner("Analyzing your data..."):
                answer = answer_question(df, question)

            st.session_state.chat_history.append((question, answer))

    if st.session_state.chat_history:
        st.subheader("💡 Answer")
        last_question, last_answer = st.session_state.chat_history[-1]
        st.write(last_answer)

        with st.expander("Previous questions"):
            for q, a in reversed(st.session_state.chat_history[:-1]):
                st.write(f"**Q:** {q}")
                st.write(f"**A:** {a}")
                st.divider()