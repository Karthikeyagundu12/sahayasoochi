<<<<<<< HEAD
# SahayaSoochi - AI Letter Generator

A Streamlit-based AI letter generation app that helps users create formal government application letters in Telugu or English. The app supports both text input (Roman Telugu) and voice recording (spoken Telugu).

## Features

- **Multi-language Support**: UI available in English and Telugu
- **Voice Input**: Record Telugu speech and convert to text
- **Text Input**: Type in Roman Telugu script
- **Intent Detection**: Automatically detects the type of certificate/letter needed
- **Letter Generation**: Creates formal government application letters
- **Offline Operation**: Works without cloud APIs (except speech recognition)
- **Data Collection**: Saves user inputs to CSV for future NLP training
- **Mobile Compatible**: Responsive design for mobile devices

## Supported Letter Types

- Birth Certificate (పుట్టిన తేదీ ధృవీకరణ పత్రం)
- Ration Card (రేషన్ కార్డు)
- Income Certificate (ఆదాయ ధృవీకరణ పత్రం)
- Caste Certificate (కుల ధృవీకరణ పత్రం)
- Residence Certificate (నివాస ధృవీకరణ పత్రం)
- Tax Exemption (పన్ను మినహాయింపు)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sahayasoochi_voice_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. **Select UI Language**: Choose between English and Telugu interface
2. **Choose Input Method**: 
   - Text: Type your request in Roman Telugu
   - Audio: Record your voice in Telugu
3. **Select Output Language**: Choose Telugu or English for the generated letter
4. **Generate Letter**: Click the generate button to create your formal letter

## Example Inputs

### Roman Telugu Text:
- "Naku birth certificate kavali"
- "Maa family ki ration card apply cheyali"
- "Income certificate avasaram"

### Voice Recording:
Speak clearly in Telugu about your requirement.

## File Structure

```
sahayasoochi_voice_app/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── corpus.csv         # Generated data corpus (created after first use)
```

## Technical Details

- **Framework**: Streamlit
- **Speech Recognition**: Google Speech Recognition API
- **Audio Processing**: sounddevice, soundfile, pydub
- **Data Storage**: Pandas CSV
- **Language Support**: Telugu and English

## Data Collection

The app automatically saves all user inputs to `corpus.csv` with the following information:
- User input (text or transcribed speech)
- Detected intent
- Input source (text/audio)
- Timestamp

This data can be used for future NLP model training and improvement.

## Contributing

Feel free to contribute by:
- Adding new letter templates
- Improving intent detection
- Enhancing the UI/UX
- Adding more language support

## License

This project is open source and available under the MIT License. 
=======
     ** SahayaSoochi(సహాయసూచి)**

**Telugu Government Application Generator"**

"**ప్రతి గళం ప్రభుత్వంతో మాట్లాడాలి. ప్రతి గ్రామానికి ఒక అధికార అభ్యర్థన!"
Every voice should reach the government. Every village deserves official access.**


~Speak, Type, or Upload – Get Your Official Letters in Seconds
 Corpus Collection meets Public Empowerment

# 1.Project Theme 
SahayaSoochi is a people-first, AI-powered tool designed to help rural citizens of Andhra Pradesh and Telangana easily generate formal government application letters in Telugu.

From income certificates to caste validations, this app converts:

-Text

-Voice

-Video

into ready-to-use application drafts in proper Telugu format.

At the same time, it collects valuable spoken and written Telugu corpus for open-source AI — supporting multilingual model training.

# What Users Can Do

# 1.1 Feature Description

-Text Input	Enter name, village, request type to get a letter

-Audio Input	Speak in Telugu – auto-transcribed via Whisper

- Video Upload	Upload a video – extract audio, transcribe, generate

-Telugu Letter	Get structured, downloadable formal letter

- Offline Support	Built for rural & low-bandwidth users

# 2. Tech Stack
-Frontend: Streamlit

-AI Models: Whisper (ASR), Template-based  Generation

-Audio/Video: ffmpeg-python

-Storage: SQLite / Firebase

-Deployment: Hugging Face Spaces

-Focus: Offline-first, Telugu-first

# 3.Testing Summary
- Telangana dialects tested
- Works on slow 3G connections
- Font scaling helps elderly users
- Mobile Telugu input verified
- Audio size limits conserve bandwidth

# 4.Expected Outcomes

Metric	Target

Villages Reached	    20+ 

Users Onboarded	        200+

Letters Generated	    300+

Student Volunteers  	30+

WhatsApp Groups Used	25+

# 5.User Acquisition Strategy
- Poster Campaigns: Local Telugu posters in temples, schools, village centers
-Field Demos: Volunteers guide locals to record and submit requests
-WhatsApp Sharing: App link and video demo shared in regional groups
- Guided Drives: In panchayats, hands-on collection sessions
- Community Champions: Early users help spread the app village-to-village

# 6.Team Members

Karthikeya – Team Lead, AI Integration & Frontend

Muktha – Voice & Video Processing Engineer

Spandana – Corpus Structuring & Language Design

Anjali – Outreach Strategy & Field Testing

Sowmya – Deployment, Hosting & Documentation

# 7. Contact
* Email: karthikeyagundu2005@gmail.com

**Team meambers Gitlab accounts: 

     1.Karthikeya_gundu

     2.Muktha2005

     3.spandana_gunda

     4.Anjaligoud
     
     5.meegada_sowmya

*Region: Andhra Pradesh, Telangana

*Language Focus: తెలుగు (Telugu)with plan to expand
     
     
      **Built for the viswam.ai Open AI Data Movement**

>>>>>>> d243847b6ec1dbad345b1a85ed528d17a3dcc2ea
