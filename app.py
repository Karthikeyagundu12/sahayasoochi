# ✅ app.py — SahayaSoochi with Gemini API Telugu & English letter support

import streamlit as st
import speech_recognition as sr
from datetime import datetime
import os

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

def main():
    st.set_page_config(
        page_title="SahayaSoochi",
        page_icon="✉️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Initialize session state
    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""

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

        if input_method == "Text":
            st.session_state["user_input"] = st.text_area(
                T["input_text"],
                height=150,
                placeholder="Example: Naku birth certificate kavali...",
                value=st.session_state.get("user_input", "")
            )
        else:
            st.info(T["recording_info"])
            if st.button(T["recording_start"]):
                recognizer = sr.Recognizer()
                with sr.Microphone() as source:
                    st.write(T["recording_status"])
                    audio_data = recognizer.listen(source, timeout=5)
                    st.write(T["recording_finished"])
                    try:
                        st.session_state["user_input"] = recognizer.recognize_google(audio_data, language="te-IN")
                        st.success(f"{T['transcribed']} {st.session_state['user_input']}")
                    except sr.UnknownValueError:
                        st.session_state["user_input"] = ""
                        st.error(T["speech_error"])
                    except sr.RequestError:
                        st.session_state["user_input"] = ""
                        st.error(T["connection_error"])

        # Output language choice
        language = st.radio(T["language_label"], ("Telugu", "English"), horizontal=True)

        # Generate letter
        if st.button(T["generate_button"], type="primary") and st.session_state["user_input"]:
            with st.spinner("Generating letter using Gemini..."):
                intent = detect_intent(st.session_state["user_input"])

                try:
                    letter = generate_letter(st.session_state["user_input"], language)
                except Exception as e:
                    st.error(f"❌ Error generating letter: {e}")
                    return

                # Save data
                input_source = "audio" if input_method == "Audio" else "text"
                save_to_corpus(st.session_state["user_input"], intent, input_source, letter)

                letter_data = {
                    "intent": intent,
                    "input": st.session_state["user_input"],
                    "letter": letter,
                    "language": language.lower(),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                save_letter_history(letter_data)

                # Display results
                st.subheader(T["output_title"])

                intent_display = {
                    "birth_certificate": "Birth Certificate",
                    "ration_card": "Ration Card",
                    "income_certificate": "Income Certificate",
                    "caste_certificate": "Caste Certificate",
                    "residence_certificate": "Residence Certificate",
                    "tax_exemption": "Tax Exemption",
                    "general": "General Application"
                }

                col_info1, col_info2 = st.columns(2)
                with col_info1:
                    st.info(f"{T['intent_detected']} {intent_display.get(intent, intent)}")
                with col_info2:
                    st.info(f"{T['timestamp']} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                st.text_area(T["output_box"], letter, height=300)

                # Download button
                letter_filename = f"{intent}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                st.download_button(
                    label=T["download_button"],
                    data=letter,
                    file_name=letter_filename,
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()
