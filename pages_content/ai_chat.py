import streamlit as st
from core.ai import generate_ai_response

def render_ai_chat():
    st.header("🤖 AI Assistant")
    st.write("Test the AI connection by entering a simple prompt below.")

    prompt = st.text_input("Enter a prompt:", placeholder="Explain data analysis in simple words.")

    if st.button("Ask AI"):
        if not prompt.strip():
            st.warning("Please enter a prompt first.")
        else:
            with st.spinner("Getting response from Gemini..."):
                response = generate_ai_response(prompt)

            if response.startswith("Error:"):
                st.error(response)
            else:
                st.success("AI Response:")
                st.write(response)