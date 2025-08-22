import os
import pandas as pd
from datetime import datetime

# =========================
# UI Texts
# =========================
UI_TEXTS = {
    "en": {
        "title": "📜 SahayaSoochi",
        "description": "AI Letter Generator for Every Occasion.",
        "input_type": "Choose Input Type:",
        "input_text": "✍️ Enter your request",
        "language_label": "Select output language:",
        "generate_button": "Generate Letter",
        "output_title": "📄 Generated Letter",
        "output_box": "Letter Content",
        "download_button": "⬇️ Download Letter",
        "clear_history": "🗑️ Clear History",
        "no_history": "No history found.",
        "intent_detected": "📌 Detected Intent:",
        "timestamp": "⏰ Generated at:",
        "recording_info": "🎙️ Click start to record your request.",
        "recording_start": "🎤 Start Recording",
        "recording_status": "🔴 Recording... Please speak.",
        "recording_finished": "✅ Recording stopped.",
        "transcribed": "📝 Transcribed Text:",
        "speech_error": "❌ Could not understand audio",
        "connection_error": "⚠️ Could not connect to recognition service",
    },
    "te": {
        "title": "📜 సహాయసూచి - లేఖ జనరేటర్",
        "description": "ఇంగ్లీష్ లేదా తెలుగులో అధికారిక లేఖలను ఆటోమేటిక్‌గా రూపొందించండి.",
        "input_type": "ఇన్పుట్ రకం ఎంచుకోండి:",
        "input_text": "✍️ మీ అభ్యర్థనను నమోదు చేయండి",
        "language_label": "లేఖ భాషను ఎంచుకోండి:",
        "generate_button": "లేఖను తయారు చేయండి",
        "output_title": "📄 రూపొందించిన లేఖ",
        "output_box": "లేఖ విషయం",
        "download_button": "⬇️ లేఖను డౌన్లోడ్ చేసుకోండి",
        "clear_history": "🗑️ చరిత్రను తొలగించండి",
        "no_history": "చరిత్ర దొరకలేదు.",
        "intent_detected": "📌 గుర్తించిన ఉద్దేశ్యం:",
        "timestamp": "⏰ తయారు చేసిన సమయం:",
        "recording_info": "🎙️ రికార్డ్ చేయడానికి స్టార్ట్ నొక్కండి.",
        "recording_start": "🎤 రికార్డింగ్ ప్రారంభించండి",
        "recording_status": "🔴 రికార్డింగ్ జరుగుతోంది... దయచేసి మాట్లాడండి.",
        "recording_finished": "✅ రికార్డింగ్ ఆగింది.",
        "transcribed": "📝 ట్రాన్స్క్రిప్ట్ చేసిన వాక్యం:",
        "speech_error": "❌ ఆడియోను అర్థం చేసుకోలేకపోయాం",
        "connection_error": "⚠️ గుర్తింపు సేవకు కనెక్ట్ కాలేకపోయాం",
    },
}

# =========================
# Letter History
# =========================
HISTORY_FILE = "letter_history.csv"

def load_letter_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE).to_dict("records")
    return []

def save_letter_history(letter_data):
    df = pd.DataFrame([letter_data])
    if os.path.exists(HISTORY_FILE):
        df.to_csv(HISTORY_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(HISTORY_FILE, index=False)

def clear_letter_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

# =========================
# Intent Detection
# =========================
def detect_intent(user_input: str) -> str:
    text = user_input.lower()
    if "birth" in text:
        return "birth_certificate"
    elif "ration" in text:
        return "ration_card"
    elif "income" in text:
        return "income_certificate"
    elif "caste" in text:
        return "caste_certificate"
    elif "residence" in text:
        return "residence_certificate"
    elif "tax" in text:
        return "tax_exemption"
    else:
        return "general"

# =========================
# Corpus Saving
# =========================
def save_to_corpus(user_input, intent, input_source, letter, audio_file=None):
    """Save user input, intent, letter, and optional audio file into corpus.csv"""
    corpus_folder = "audio_corpus"
    os.makedirs(corpus_folder, exist_ok=True)

    file_path = "corpus.csv"

    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["timestamp", "intent", "input_source", "input", "letter", "audio_file"])
        df.to_csv(file_path, index=False)

    df = pd.read_csv(file_path)

    # Move audio file if present
    if audio_file:
        base_name = os.path.basename(audio_file)
        target_path = os.path.join(corpus_folder, base_name)
        if os.path.exists(audio_file) and not os.path.exists(target_path):
            os.rename(audio_file, target_path)
        audio_file = target_path

    new_row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "intent": intent,
        "input_source": input_source,
        "input": user_input,
        "letter": letter,
        "audio_file": audio_file if audio_file else ""
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(file_path, index=False)
