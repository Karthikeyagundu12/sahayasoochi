import os
import pandas as pd

# =========================
# UI TEXTS
# =========================
# SahayaSoochi Configuration File

# ================= UI TEXTS =================
UI_TEXTS = {
    "en": {
        "title": "SahayaSoochi",
        "description": "AI Letter Generator for Every Occasion",
        "input_type": "Select Input Method:",
        "input_text": "Enter your request:",
        "recording_info": "Click below to record your voice.",
        "recording_start": "🎤 Start Recording",
        "recording_status": "Listening...",
        "recording_finished": "Recording complete.",
        "transcribed": "Transcribed Text:",
        "speech_error": "Sorry, could not understand the audio.",
        "connection_error": "Connection error while processing audio.",
        "language_label": "Choose output letter language:",
        "generate_button": "Generate Letter",
        "output_title": "Generated Letter",
        "intent_detected": "Intent detected:",
        "timestamp": "Generated at:",
        "output_box": "Letter Output",
        "download_button": "Download Letter",
        "clear_history": "🗑 Clear History",
        "no_history": "No letter history found."
    },
    "te": {
        "title": "సహాయసూచి",
        "description": "ప్రతి సందర్భానికి లేఖలు రూపొందించండి",
        "input_type": "ఇన్‌పుట్ విధానం ఎంచుకోండి:",
        "input_text": "మీ అభ్యర్థన నమోదు చేయండి:",
        "recording_info": "మీ వాయిస్ రికార్డ్ చేయడానికి కింది బటన్ క్లిక్ చేయండి.",
        "recording_start": "🎤 రికార్డింగ్ ప్రారంభించండి",
        "recording_status": "వింటోంది...",
        "recording_finished": "రికార్డింగ్ పూర్తయింది.",
        "transcribed": "లిఖిత రూపం:",
        "speech_error": "క్షమించండి, ఆడియోను అర్థం చేసుకోలేకపోయాను.",
        "connection_error": "ఆడియో ప్రాసెస్ చేస్తుండగా కనెక్షన్ లోపం.",
        "language_label": "లేఖ భాషను ఎంచుకోండి:",
        "generate_button": "లేఖ సృష్టించండి",
        "output_title": "సృష్టించిన లేఖ",
        "intent_detected": "గుర్తించిన ఉద్దేశ్యం:",
        "timestamp": "సృష్టించిన సమయం:",
        "output_box": "లేఖ అవుట్‌పుట్",
        "download_button": "లేఖ డౌన్‌లోడ్ చేయండి",
        "clear_history": "🗑 చరిత్రను క్లియర్ చేయండి",
        "no_history": "లేఖ చరిత్ర లభించలేదు."
    }
}

# ================= App Settings =================
APP_NAME = "SahayaSoochi"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI Letter Generator for Government Applications"

# ================= Audio Recording Settings =================
RECORDING_DURATION = 5  # seconds
SAMPLE_RATE = 44100
CHANNELS = 1

# ================= File Paths =================
CORPUS_FILE = "corpus.csv"
HISTORY_FILE = "letter_history.json"
AUDIO_FILE = "input.wav"

# ================= Supported Languages =================
SUPPORTED_LANGUAGES = {
    "en": "English",
    "te": "తెలుగు"
}

# ================= Helper Functions =================
import json
import os

def load_letter_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_letter_history(letter_data):
    history = load_letter_history()
    history.append(letter_data)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def clear_letter_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

def save_to_corpus(user_input, intent, source, letter):
    import csv
    exists = os.path.exists(CORPUS_FILE)
    with open(CORPUS_FILE, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if not exists:
            writer.writerow(["input", "intent", "source", "letter"])
        writer.writerow([user_input, intent, source, letter])

def detect_intent(user_input):
    user_input_lower = user_input.lower()
    if "birth" in user_input_lower:
        return "birth_certificate"
    elif "ration" in user_input_lower:
        return "ration_card"
    elif "income" in user_input_lower:
        return "income_certificate"
    elif "caste" in user_input_lower:
        return "caste_certificate"
    elif "residence" in user_input_lower:
        return "residence_certificate"
    elif "tax" in user_input_lower:
        return "tax_exemption"
    else:
        return "general"
