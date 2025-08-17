# ✅ gemini_api.py — Gemini integration with safe corpus saving
import os
import json
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

CORPUS_FILE = "corpus_data.json"

def save_to_corpus(user_input: str, generated_letter: str, language: str):
    """
    Saves user input and generated letter to JSON corpus safely.
    """
    entry = {
        "timestamp": datetime.now().isoformat(),
        "language": language,
        "user_input": user_input,
        "generated_letter": generated_letter
    }

    # Load existing data safely
    if os.path.exists(CORPUS_FILE) and os.path.getsize(CORPUS_FILE) > 0:
        with open(CORPUS_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    # Save back
    with open(CORPUS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_letter(user_input: str, language: str = "English") -> str:
    """
    Generates a formal letter using Gemini API and saves corpus.
    Args:
        user_input: Problem statement (Roman Telugu or English)
        language: "Telugu" or "English"
    Returns:
        str: Generated letter in specified language only
    """
    try:
        # Normalize language input
        language_text = "Telugu" if language.lower() == "telugu" else "English"

        # Merge instructions into user input
        prompt = (
            f"You are SahayaSoochi, an assistant that generates formal government application letters. "
            f"Take this short user input: '{user_input}' and expand it into a grammatically correct "
            f"{language_text} letter. Use only {language_text} and do not include any other language. "
            "Ensure politeness and official format."
        )

        # Create Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Send as single user message (no system role)
        response = model.generate_content(
            [
                {"role": "user", "parts": [prompt]}
            ]
        )

        letter = response.text.strip()

        # Save input & output to corpus
        save_to_corpus(user_input, letter, language_text)

        return letter

    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"
