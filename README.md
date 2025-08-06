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