# Changelog
All notable changes to **SahayaSoochi** will be documented in this file.  
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to **Semantic Versioning**.

---

## [Unreleased]

🚀 Features in Development
- Voice-to-text transcription for Telugu using Whisper / Gemini Speech API  
- Offline letter generation (local templates without API dependency)  
- Integration with Supabase/PostgreSQL for corpus storage  
- Admin dashboard for reviewing submitted problem statements  
- API for third-party integration (e.g., mobile apps)

---

## [1.0.0] - 2025-08-15

🎉 **Initial Release**  
This is the first public release of **SahayaSoochi**, a beginner-friendly app to generate government application letters in **Telugu & English**.  

✨ **Added**

### Core Features
- User input via **text** (Roman Telugu)  
- Automatic detection of user intent (e.g., ration card, pension, income certificate)  
- Template-based letter generation in **Telugu and English**  
- Support for multiple letter categories (complaints, requests, certificates, leave applications, etc.)  

### AI Capabilities
- Integration with **Gemini API** for natural Telugu text generation  
- Roman Telugu input → Native Telugu script conversion  
- Corpus collection of user problem statements for future improvements  

### User Interface
- **Streamlit-based** web application  
- Simple, clean UI with input box and results display  
- Option to view generated letters in Telugu & English  
- Button to clear/reset generated letters  

### Backend Services
- Local JSON storage for letter history  
- Corpus saving functionality for research & improvement  
- Config-driven environment variable handling (`.env` for API keys)  

---

## 🔧 Technical Stack
- **Frontend**: Streamlit 1.33.0  
- **AI/ML**: Gemini API (for Telugu letter generation)  
- **Database**: JSON / CSV corpus storage (future: Supabase/PostgreSQL)  
- **Deployment**: Hugging Face Spaces (Streamlit runtime)  

---

## 📚 Documentation
- README with setup instructions  
- Example letter templates (Telugu & English)  
- Corpus guidelines for contributors  

---

## 🔒 Security
- `.env` file for API key management  
- Local-only file uploads (no third-party leaks)  

---

## 🌍 Supported Languages
- **Telugu** (native script & Roman Telugu input)  
- **English**  

---

## 👥 Contributors
Special thanks to all contributors who supported this beginner-friendly project!  

---

## Version History Summary

| Version  | Release Date | Major Features |
|----------|--------------|----------------|
| 1.0.0    | 2025-08-15   | First stable release with core Telugu-English letter generation |

---

## Upgrade Notes
### From Development → 1.0.0
- Add `.env` with `GEMINI_API_KEY`  
- Install dependencies from `requirements.txt`  
- Run Streamlit app: `streamlit run app.py`  

---

## Deprecation Notices
- None yet (all features are fresh in 1.0.0 release)  

---

## Future Roadmap
### Version 1.1.0 (Q4 2025)
- Voice input for Telugu → text transcription  
- Export letters as **PDF** and **Word**  

### Version 1.2.0 (Q1 2026)
- Corpus collection dashboard  
- Multi-user support with login  

### Version 2.0.0 (Q3 2026)
- Mobile application (Android + iOS)  
- AI-powered smart intent detection  
- Multi-language expansion (Hindi, Tamil, Kannada, Marathi, etc.)  

