import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

FALLBACK_MODELS = ["gemini-3.6-flash", "gemini-3.1-flash-lite", "gemini-2.5-flash"]

def generate_ai_response(prompt: str) -> str:
    """
    Sends a text prompt to Gemini and returns the response as plain text.
    Keeps error handling simple and beginner-friendly.
    """
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Error: GEMINI_API_KEY not found. Please check your .env file."

    if not prompt or not prompt.strip():
        return "Error: Prompt cannot be empty."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-3.6-flash")
        response = model.generate_content(prompt)

        if not response or not response.text:
            return "Error: The AI did not return a response. Please try again."

        return response.text

    except Exception as e:
        return f"Error: Could not get a response from the AI. ({e})"
    