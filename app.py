# ✅ app.py — SahayaSoochi with Gemini API Telugu & English letter support (with Audio Save)

import streamlit as st
import speech_recognition as sr
import os
from datetime import datetime
import wave

# ✅ Gemini API integration
from gemini_api import generate_letter

# ✅ App logic imports
from config import (
    UI_TEXTS,
    load_letter_history,
    clear_letter_history,
    detect_intent,
    save_to_corpus,
    save_letter_history
)


# ===============================
# Utility: Save recorded audio
# ===============================
def record_audio_to_file():
    """Record audio using Microphone and save to corpus_audio folder"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Recording... Please speak now (max 5 sec)...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        st.success("✅ Recording finished")

    # Save as WAV file
    os.makedirs("corpus_audio", exist_ok=True)
    filename = f"corpus_audio/audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())

    return audio, filename


# ===============================
# Main App
# ===============================
def main():
    st.set_page_config(
        page_title="SahayaSoochi",
        page_icon="✉️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Init state
    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""
    if "audio_file" not in st.session_state:
        st.session_state["audio_file"] = None

    # ===== Sidebar =====
    with st.sidebar:
        ui_lang = st.radio(
            "🌐 UI Language:",
            options=["en", "te"],
            format_func=lambda x: "English" if x == "en" else "తెలుగు"
        )
        T = UI_TEXTS[ui_lang]

        st.markdown("---")
        st.markdown("### 📚 Letter History")

        history = load_letter_history()
        if history:
            for i, letter_data in enumerate(reversed(history[-5:])):
                with st.expander(f"{letter_data.get('intent', 'Letter')} - {letter_data.get('timestamp', '')}"):
                    st.text_area("Generated Letter", letter_data.get('letter', ''), height=100, key=f"hist_{i}")
            if st.button(T["clear_history"]):
                clear_letter_history()
                st.rerun()
        else:
            st.info(T["no_history"])

    # ===== Main Content =====
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(f'<h1 class="main-header">{T["title"]}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center; font-size: 1.2rem;">{T["description"]}</p>', unsafe_allow_html=True)

        # Input Method
        input_method = st.radio(T["input_type"], ("Text", "Audio"), horizontal=True)

        user_input = ""
        audio_path = None

        if input_method == "Text":
            user_input = st.text_area(
                T["input_text"],
                height=150,
                placeholder="Example: Naku birth certificate kavali...",
                value=st.session_state.get("user_input", "")
            )
            st.session_state["user_input"] = user_input

        else:
            st.info(T["recording_info"])
            if st.button(T["recording_start"]):
                try:
                    audio_data, audio_path = record_audio_to_file()
                    st.session_state["audio_file"] = audio_path
                    st.success(f"🎤 Audio saved: {audio_path}")

                    # Try transcription
                    recognizer = sr.Recognizer()
                    try:
                        user_input = recognizer.recognize_google(audio_data, language="te-IN")
                        st.session_state["user_input"] = user_input
                        st.success(f"{T['transcribed']} {user_input}")
                    except sr.UnknownValueError:
                        user_input = ""
                        st.error(T["speech_error"])
                    except sr.RequestError:
                        user_input = ""
                        st.error(T["connection_error"])

                except Exception as e:
                    st.error(f"❌ Error recording audio: {e}")

        # Output language choice
        language = st.radio(T["language_label"], ("Telugu", "English"), horizontal=True)

        # ===== Generate Letter =====
        if st.button(T["generate_button"], type="primary") and (user_input or st.session_state.get("audio_file")):
            with st.spinner("Generating letter using Gemini..."):
                intent = detect_intent(user_input if user_input else "audio_request")

                try:
                    letter = generate_letter(user_input if user_input else "Audio request (no transcription)", language)
                except Exception as e:
                    st.error(f"❌ Error generating letter: {e}")
                    return

                # Save corpus (text + audio link)
                save_to_corpus(
                    user_input if user_input else "Audio only (not transcribed)",
                    intent,
                    input_method.lower(),
                    letter,
                    audio_file=st.session_state.get("audio_file")
                )

                letter_data = {
                    "intent": intent,
                    "input": user_input if user_input else "Audio only",
                    "letter": letter,
                    "language": language.lower(),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "audio_file": st.session_state.get("audio_file") or ""
                }
                save_letter_history(letter_data)

                # Display results
                st.subheader(T["output_title"])
                st.text_area(T["output_box"], letter, height=300)

                fname = f"{intent}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                st.download_button(T["download_button"], letter, file_name=fname, mime="text/plain")


if __name__ == "__main__":
    main()
