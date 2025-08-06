import streamlit as st
import speech_recognition as sr
import soundfile as sf
import pandas as pd
import io
from datetime import datetime
import os
import json

from gemini_api import generate_letter  # ✅ Gemini API integrated
# UI text translations
UI_TEXTS = {
    "en": {
        "title": "✉️ SahayaSoochi – Letter Generator",
        "description": "Enter your request in Roman Telugu or record your voice in spoken Telugu",
        "input_type": "Select Input Type:",
        "input_text": "Enter in Roman Telugu:",
        "input_audio": "Record your voice in Telugu:",
        "language_label": "Output Letter Language:",
        "generate_button": "Generate Letter",
        "transcribed": "Transcribed Text:",
        "output_title": "📄 Generated Letter",
        "output_box": "Letter Output:",
        "ui_language": "UI Language:",
        "download_button": "Download Letter",
        "history_title": "📚 Letter History",
        "clear_history": "Clear History",
        "no_history": "No letters generated yet.",
        "recording_info": "🎙️ Click to record your voice (5 seconds)",
        "recording_start": "🎤 Start Recording",
        "recording_status": "Recording...",
        "recording_finished": "Recording finished.",
        "speech_error": "❌ Speech not recognized.",
        "connection_error": "❌ Could not connect to recognition service.",
        "intent_detected": "Detected Intent:",
        "letter_type": "Letter Type:",
        "timestamp": "Generated on:"
    },
    "te": {
        "title": "✉️ సహాయసూచి – లేఖ రూపొందింపు",
        "description": "మీ సమస్యను రోమన్ తెలుగు లో టైప్ చేయండి లేదా మైక్ ద్వారా చెప్పండి",
        "input_type": "ఇన్పుట్ పద్ధతిని ఎంచుకోండి:",
        "input_text": "రోమన్ తెలుగు లో నమోదు చేయండి:",
        "input_audio": "తెలుగు లో మాట్లాడండి:",
        "language_label": "లేఖ భాషను ఎంచుకోండి:",
        "generate_button": "లేఖ రూపొందించు",
        "transcribed": "వాయిస్ నుండి పొందిన వాక్యం:",
        "output_title": "📄 రూపొందించిన లేఖ",
        "output_box": "లేఖ ఫలితం:",
        "ui_language": "ఇంటర్‌ఫేస్ భాష:",
        "download_button": "లేఖ డౌన్‌లోడ్ చేయండి",
        "history_title": "📚 లేఖ చరిత్ర",
        "clear_history": "చరిత్రను తొలగించండి",
        "no_history": "ఇంకా లేఖలు రూపొందించబడలేదు.",
        "recording_info": "🎙️ మీ వాయిస్ రికార్డ్ చేయడానికి క్లిక్ చేయండి (5 సెకండ్లు)",
        "recording_start": "🎤 రికార్డింగ్ ప్రారంభించండి",
        "recording_status": "రికార్డింగ్ జరుగుతోంది...",
        "recording_finished": "రికార్డింగ్ పూర్తయింది.",
        "speech_error": "❌ వాక్కు గుర్తించబడలేదు.",
        "connection_error": "❌ గుర్తింపు సేవకు కనెక్ట్ చేయలేకపోయాము.",
        "intent_detected": "గుర్తించబడిన ఉద్దేశ్యం:",
        "letter_type": "లేఖ రకం:",
        "timestamp": "రూపొందించబడిన తేదీ:"
    }
}

# Letter templates with more comprehensive content
LETTER_TEMPLATES = {
    "birth_certificate": {
        "en": {
            "title": "Application for Birth Certificate",
            "template": """To,
The Tahsildar,
{mandal} Mandal,
{district} District.

Subject: Application for Birth Certificate

Respected Sir/Madam,

I, {applicant_name}, resident of {address}, hereby submit this application requesting you to issue a birth certificate for my child.

Details of the child:
Name: {child_name}
Date of Birth: {dob}
Place of Birth: {place}
Hospital/Clinic: {hospital}
Gender: {gender}

I have attached all the required documents including:
1. Hospital discharge summary
2. Parent's ID proof
3. Address proof

I kindly request you to process my application and issue the birth certificate at the earliest.

Thanking you,
Yours faithfully,
{applicant_name}
{phone_number}"""
        },
        "te": {
            "title": "పుట్టిన తేదీ ధృవీకరణ పత్రం కోసం దరఖాస్తు",
            "template": """గౌరవ తహశీల్దార్ గారికి,
{mandal} మండలం,
{district} జిల్లా.

విషయం: పుట్టిన తేదీ ధృవీకరణ పత్రం కోసం దరఖాస్తు

గౌరవనీయులైన సర్/మేడం,

నేను, {applicant_name}, {address} నివాసి, మా బిడ్డకు పుట్టిన తేదీ ధృవీకరణ పత్రం జారీ చేయవలసినదిగా మీ ద్వారా ఈ దరఖాస్తును సమర్పిస్తున్నాను.

బిడ్డ వివరాలు:
పేరు: {child_name}
పుట్టిన తేదీ: {dob}
పుట్టిన ప్రదేశం: {place}
ఆసుపత్రి/క్లినిక్: {hospital}
లింగం: {gender}

అవసరమైన పత్రాలను జతచేసి ఉన్నాను:
1. ఆసుపత్రి డిస్చార్జ్ సమ్మరీ
2. తల్లిదండ్రుల గుర్తింపు పత్రం
3. చిరునామా ధృవీకరణ

మీ ద్వారా నా దరఖాస్తును పరిశీలించి త్వరలో పుట్టిన తేదీ ధృవీకరణ పత్రం జారీ చేయవలసినదిగా వినతిచేస్తున్నాను.

ధన్యవాదాలతో,
మీ విధేయుడు,
{applicant_name}
{phone_number}"""
        }
    },
    "ration_card": {
        "en": {
            "title": "Application for Ration Card",
            "template": """To,
The Tahsildar,
{mandal} Mandal,
{district} District.

Subject: Application for New Ration Card

Respected Sir/Madam,

I, {applicant_name}, resident of {address}, hereby submit this application requesting you to issue a new ration card for my family.

Family Details:
Head of Family: {applicant_name}
Address: {address}
Family Members: {family_members}
Total Family Income: Rs. {income} per annum

Documents attached:
1. Address proof
2. Income certificate
3. Family photo
4. Aadhaar cards of all family members

I kindly request you to process my application and issue the ration card at the earliest.

Thanking you,
Yours faithfully,
{applicant_name}
{phone_number}"""
        },
        "te": {
            "title": "రేషన్ కార్డు కోసం దరఖాస్తు",
            "template": """గౌరవ తహశీల్దార్ గారికి,
{mandal} మండలం,
{district} జిల్లా.

విషయం: కొత్త రేషన్ కార్డు కోసం దరఖాస్తు

గౌరవనీయులైన సర్/మేడం,

నేను, {applicant_name}, {address} నివాసి, మా కుటుంబానికి కొత్త రేషన్ కార్డు జారీ చేయవలసినదిగా మీ ద్వారా ఈ దరఖాస్తును సమర్పిస్తున్నాను.

కుటుంబ వివరాలు:
కుటుంబ ముఖ్యస్థుడు: {applicant_name}
చిరునామా: {address}
కుటుంబ సభ్యులు: {family_members}
మొత్తం కుటుంబ ఆదాయం: రూ. {income} సంవత్సరానికి

జతచేసిన పత్రాలు:
1. చిరునామా ధృవీకరణ
2. ఆదాయ ధృవీకరణ పత్రం
3. కుటుంబ ఫోటో
4. అన్ని కుటుంబ సభ్యుల ఆధార్ కార్డులు

మీ ద్వారా నా దరఖాస్తును పరిశీలించి త్వరలో రేషన్ కార్డు జారీ చేయవలసినదిగా వినతిచేస్తున్నాను.

ధన్యవాదాలతో,
మీ విధేయుడు,
{applicant_name}
{phone_number}"""
        }
    },
    "income_certificate": {
        "en": {
            "title": "Application for Income Certificate",
            "template": """To,
The Tahsildar,
{mandal} Mandal,
{district} District.

Subject: Application for Income Certificate

Respected Sir/Madam,

I, {applicant_name}, resident of {address}, hereby submit this application requesting you to issue an income certificate for my family.

Personal Details:
Name: {applicant_name}
Address: {address}
Occupation: {occupation}
Annual Income: Rs. {income}

Purpose of Certificate: {purpose}

Documents attached:
1. Salary certificate/Income proof
2. Address proof
3. Aadhaar card

I kindly request you to process my application and issue the income certificate at the earliest.

Thanking you,
Yours faithfully,
{applicant_name}
{phone_number}"""
        },
        "te": {
            "title": "ఆదాయ ధృవీకరణ పత్రం కోసం దరఖాస్తు",
            "template": """గౌరవ తహశీల్దార్ గారికి,
{mandal} మండలం,
{district} జిల్లా.

విషయం: ఆదాయ ధృవీకరణ పత్రం కోసం దరఖాస్తు

గౌరవనీయులైన సర్/మేడం,

నేను, {applicant_name}, {address} నివాసి, మా కుటుంబానికి ఆదాయ ధృవీకరణ పత్రం జారీ చేయవలసినదిగా మీ ద్వారా ఈ దరఖాస్తును సమర్పిస్తున్నాను.

వ్యక్తిగత వివరాలు:
పేరు: {applicant_name}
చిరునామా: {address}
వృత్తి: {occupation}
వార్షిక ఆదాయం: రూ. {income}

పత్రం ఉపయోగం: {purpose}

జతచేసిన పత్రాలు:
1. జీతం ధృవీకరణ/ఆదాయ ధృవీకరణ
2. చిరునామా ధృవీకరణ
3. ఆధార్ కార్డు

మీ ద్వారా నా దరఖాస్తును పరిశీలించి త్వరలో ఆదాయ ధృవీకరణ పత్రం జారీ చేయవలసినదిగా వినతిచేస్తున్నాను.

ధన్యవాదాలతో,
మీ విధేయుడు,
{applicant_name}
{phone_number}"""
        }
    },
    "caste_certificate": {
        "en": {
            "title": "Application for Caste Certificate",
            "template": """To,
The Tahsildar,
{mandal} Mandal,
{district} District.

Subject: Application for Caste Certificate

Respected Sir/Madam,

I, {applicant_name}, resident of {address}, hereby submit this application requesting you to issue a caste certificate.

Personal Details:
Name: {applicant_name}
Father's Name: {father_name}
Address: {address}
Caste: {caste}
Sub-caste: {sub_caste}

Documents attached:
1. Birth certificate
2. Parent's caste certificate
3. Address proof
4. Aadhaar card

I kindly request you to process my application and issue the caste certificate at the earliest.

Thanking you,
Yours faithfully,
{applicant_name}
{phone_number}"""
        },
        "te": {
            "title": "కుల ధృవీకరణ పత్రం కోసం దరఖాస్తు",
            "template": """గౌరవ తహశీల్దార్ గారికి,
{mandal} మండలం,
{district} జిల్లా.

విషయం: కుల ధృవీకరణ పత్రం కోసం దరఖాస్తు

గౌరవనీయులైన సర్/మేడం,

నేను, {applicant_name}, {address} నివాసి, నాకు కుల ధృవీకరణ పత్రం జారీ చేయవలసినదిగా మీ ద్వారా ఈ దరఖాస్తును సమర్పిస్తున్నాను.

వ్యక్తిగత వివరాలు:
పేరు: {applicant_name}
తండ్రి పేరు: {father_name}
చిరునామా: {address}
కులం: {caste}
ఉపకులం: {sub_caste}

జతచేసిన పత్రాలు:
1. పుట్టిన తేదీ ధృవీకరణ పత్రం
2. తల్లిదండ్రుల కుల ధృవీకరణ పత్రం
3. చిరునామా ధృవీకరణ
4. ఆధార్ కార్డు

మీ ద్వారా నా దరఖాస్తును పరిశీలించి త్వరలో కుల ధృవీకరణ పత్రం జారీ చేయవలసినదిగా వినతిచేస్తున్నాను.

ధన్యవాదాలతో,
మీ విధేయుడు,
{applicant_name}
{phone_number}"""
        }
    },
    "residence_certificate": {
        "en": {
            "title": "Application for Residence Certificate",
            "template": """To,
The Tahsildar,
{mandal} Mandal,
{district} District.

Subject: Application for Residence Certificate

Respected Sir/Madam,

I, {applicant_name}, resident of {address}, hereby submit this application requesting you to issue a residence certificate.

Personal Details:
Name: {applicant_name}
Father's Name: {father_name}
Address: {address}
Duration of Residence: {duration} years

Purpose of Certificate: {purpose}

Documents attached:
1. Address proof
2. Aadhaar card
3. Voter ID
4. Utility bills

I kindly request you to process my application and issue the residence certificate at the earliest.

Thanking you,
Yours faithfully,
{applicant_name}
{phone_number}"""
        },
        "te": {
            "title": "నివాస ధృవీకరణ పత్రం కోసం దరఖాస్తు",
            "template": """గౌరవ తహశీల్దార్ గారికి,
{mandal} మండలం,
{district} జిల్లా.

విషయం: నివాస ధృవీకరణ పత్రం కోసం దరఖాస్తు

గౌరవనీయులైన సర్/మేడం,

నేను, {applicant_name}, {address} నివాసి, నాకు నివాస ధృవీకరణ పత్రం జారీ చేయవలసినదిగా మీ ద్వారా ఈ దరఖాస్తును సమర్పిస్తున్నాను.

వ్యక్తిగత వివరాలు:
పేరు: {applicant_name}
తండ్రి పేరు: {father_name}
చిరునామా: {address}
నివాస కాలం: {duration} సంవత్సరాలు

పత్రం ఉపయోగం: {purpose}

జతచేసిన పత్రాలు:
1. చిరునామా ధృవీకరణ
2. ఆధార్ కార్డు
3. ఓటర్ ఐడి
4. యుటిలిటీ బిల్లులు

మీ ద్వారా నా దరఖాస్తును పరిశీలించి త్వరలో నివాస ధృవీకరణ పత్రం జారీ చేయవలసినదిగా వినతిచేస్తున్నాను.

ధన్యవాదాలతో,
మీ విధేయుడు,
{applicant_name}
{phone_number}"""
        }
    },
    "tax_exemption": {
        "en": {
            "title": "Application for Tax Exemption",
            "template": """To,
The Municipal Commissioner,
{Municipality} Municipality,
{district} District.

Subject: Application for Property Tax Exemption

Respected Sir/Madam,

I, {applicant_name}, resident of {address}, hereby submit this application requesting you to exempt the property tax levied on my property.

Property Details:
Property Address: {property_address}
Property Type: {property_type}
Assessment Number: {assessment_no}
Current Tax Amount: Rs. {tax_amount}

Reason for Exemption: {reason}

Documents attached:
1. Property documents
2. Income certificate
3. Disability certificate (if applicable)
4. Age certificate (if applicable)

I kindly request you to process my application and grant the tax exemption at the earliest.

Thanking you,
Yours faithfully,
{applicant_name}
{phone_number}"""
        },
        "te": {
            "title": "పన్ను మినహాయింపు కోసం దరఖాస్తు",
            "template": """గౌరవ మున్సిపల్ కమిషనర్ గారికి,
{Municipality} మున్సిపాలిటీ,
{district} జిల్లా.

విషయం: ఆస్తి పన్ను మినహాయింపు కోసం దరఖాస్తు

గౌరవనీయులైన సర్/మేడం,

నేను, {applicant_name}, {address} నివాసి, నా ఆస్తిపై విధించబడిన ఆస్తి పన్నును మినహాయించవలసినదిగా మీ ద్వారా ఈ దరఖాస్తును సమర్పిస్తున్నాను.

ఆస్తి వివరాలు:
ఆస్తి చిరునామా: {property_address}
ఆస్తి రకం: {property_type}
అంచనా సంఖ్య: {assessment_no}
ప్రస్తుత పన్ను మొత్తం: రూ. {tax_amount}

మినహాయింపు కారణం: {reason}

జతచేసిన పత్రాలు:
1. ఆస్తి పత్రాలు
2. ఆదాయ ధృవీకరణ పత్రం
3. వికలాంగ ధృవీకరణ పత్రం (ఉంటే)
4. వయస్సు ధృవీకరణ పత్రం (ఉంటే)

మీ ద్వారా నా దరఖాస్తును పరిశీలించి త్వరలో పన్ను మినహాయింపును మంజూరు చేయవలసినదిగా వినతిచేస్తున్నాను.

ధన్యవాదాలతో,
మీ విధేయుడు,
{applicant_name}
{phone_number}"""
        }
    }
}

def save_to_corpus(user_input, intent, source, generated_letter=""):
    """Save user input and generated letter to corpus"""
    data = {
        "input": user_input,
        "intent": intent,
        "source": source,
        "generated_letter": generated_letter,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.DataFrame([data])
    if not os.path.exists("corpus.csv"):
        df.to_csv("corpus.csv", index=False)
    else:
        df.to_csv("corpus.csv", mode='a', header=False, index=False)

def save_letter_history(letter_data):
    """Save letter to history"""
    history_file = "letter_history.json"
    history = []
    
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            history = json.load(f)
    
    history.append(letter_data)
    
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def load_letter_history():
    """Load letter history"""
    history_file = "letter_history.json"
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def clear_letter_history():
    """Clear letter history"""
    history_file = "letter_history.json"
    if os.path.exists(history_file):
        os.remove(history_file)

def detect_intent(user_input):
    """Enhanced intent detection with more keywords"""
    input_lower = user_input.lower()
    
    # Birth certificate keywords
    birth_keywords = ['birth', 'janmam', 'janma', 'puvvu', 'puvvudu', 'pattanam']
    if any(keyword in input_lower for keyword in birth_keywords):
        return "birth_certificate"
    
    # Ration card keywords
    ration_keywords = ['ration', 'ration card', 'rationcard', 'rice', 'sugar', 'kerosene', 'pds']
    if any(keyword in input_lower for keyword in ration_keywords):
        return "ration_card"
    
    # Income certificate keywords
    income_keywords = ['income', 'aadayam', 'salary', 'job', 'employment', 'earnings', 'poverty']
    if any(keyword in input_lower for keyword in income_keywords):
        return "income_certificate"
    
    # Caste certificate keywords
    caste_keywords = ['caste', 'kulam', 'community', 'jati', 'category', 'sc', 'st', 'obc']
    if any(keyword in input_lower for keyword in caste_keywords):
        return "caste_certificate"
    
    # Residence certificate keywords
    residence_keywords = ['residence', 'vasam', 'address', 'domicile', 'local', 'permanent']
    if any(keyword in input_lower for keyword in residence_keywords):
        return "residence_certificate"
    
    # Tax exemption keywords
    tax_keywords = ['tax', 'property tax', 'house tax', 'exemption', 'rebate', 'discount']
    if any(keyword in input_lower for keyword in tax_keywords):
        return "tax_exemption"
    
    return "general"

def generate_letter(intent, input_text, language='telugu'):
    """Generate letter using templates"""
    if intent not in LETTER_TEMPLATES:
        # Fallback for general intent
        if language == 'telugu':
            return f"గౌరవ తహశీల్దార్ గారికి,\n\n{input_text}\n\nధన్యవాదాలతో,\nమీ విధేయుడు"
        else:
            return f"Dear Sir/Madam,\n\n{input_text}\n\nSincerely,\nApplicant"
    
    # Convert language parameter to template key
    lang_key = 'te' if language.lower() == 'telugu' else 'en'
    template = LETTER_TEMPLATES[intent][lang_key]
    
    # Extract basic information from input text
    # This is a simplified extraction - in a real app, you might use NLP
    lines = input_text.split('\n')
    applicant_name = "Applicant"  # Default
    phone_number = "Phone: Not provided"
    
    # Try to extract name and phone from input
    for line in lines:
        if 'name' in line.lower() or 'peru' in line.lower():
            applicant_name = line.split(':')[-1].strip() if ':' in line else line
        if 'phone' in line.lower() or 'mobile' in line.lower():
            phone_number = line.split(':')[-1].strip() if ':' in line else line
    
    # Fill template with extracted or default values
    letter_content = template["template"].format(
        applicant_name=applicant_name,
        phone_number=phone_number,
        mandal="[Mandal Name]",
        district="[District Name]",
        address="[Address]",
        child_name="[Child Name]",
        dob="[Date of Birth]",
        place="[Place of Birth]",
        hospital="[Hospital Name]",
        gender="[Gender]",
        family_members="[Number of Family Members]",
        income="[Annual Income]",
        occupation="[Occupation]",
        purpose="[Purpose]",
        father_name="[Father's Name]",
        caste="[Caste]",
        sub_caste="[Sub-caste]",
        duration="[Duration]",
        property_address="[Property Address]",
        property_type="[Property Type]",
        assessment_no="[Assessment Number]",
        tax_amount="[Tax Amount]",
        reason="[Reason for Exemption]",
        Municipality="[Municipality Name]"
    )
    
    return letter_content

def main():
    st.set_page_config(
        page_title="SahayaSoochi",
        page_icon="✉️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better mobile compatibility
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton > button {
        width: 100%;
        margin: 0.5rem 0;
    }
    .stTextArea > div > div > textarea {
        font-size: 16px;
    }
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar for UI language selection
    with st.sidebar:
        ui_lang = st.radio("🌐 UI Language:", options=["en", "te"], 
                          format_func=lambda x: "English" if x == "en" else "తెలుగు")
        T = UI_TEXTS[ui_lang]
        
        st.markdown("---")
        st.markdown("### 📚 Letter History")
        
        # Load and display history
        history = load_letter_history()
        if history:
            for i, letter_data in enumerate(reversed(history[-5:])):  # Show last 5
                with st.expander(f"{letter_data.get('intent', 'Letter')} - {letter_data.get('timestamp', '')}"):
                    st.text_area("Generated Letter", letter_data.get('letter', ''), height=100, key=f"hist_{i}")
            
            if st.button(T["clear_history"]):
                clear_letter_history()
                st.rerun()
        else:
            st.info(T["no_history"])
    
    # Main content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(f'<h1 class="main-header">{T["title"]}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center; font-size: 1.2rem;">{T["description"]}</p>', unsafe_allow_html=True)
        
        # Input method selection
        input_method = st.radio(T["input_type"], ("Text", "Audio"), horizontal=True)
        user_input = ""
        
        if input_method == "Text":
            user_input = st.text_area(T["input_text"], height=150, 
                                     placeholder="Example: Naku birth certificate kavali...")
        else:
            st.info(T["recording_info"])
            if st.button(T["recording_start"]):
                duration = 5
                fs = 44100
                st.write(T["recording_status"])
                audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
                sd.wait()
                st.write(T["recording_finished"])
                sf.write("input.wav", audio, fs)
                st.audio("input.wav")

                recognizer = sr.Recognizer()
                with sr.AudioFile("input.wav") as source:
                    audio_data = recognizer.record(source)
                    try:
                        user_input = recognizer.recognize_google(audio_data, language="te-IN")
                        st.success(f"{T['transcribed']} {user_input}")
                    except sr.UnknownValueError:
                        st.error(T["speech_error"])
                    except sr.RequestError:
                        st.error(T["connection_error"])
        
        # Language selection
        language = st.radio(T["language_label"], ("Telugu", "English"), horizontal=True)
        
        # Generate button
        if st.button(T["generate_button"], type="primary") and user_input:
            with st.spinner("Generating letter..."):
                intent = detect_intent(user_input)
                letter = generate_letter(intent, user_input, language.lower())
                
                # Save to corpus and history
                input_source = "audio" if input_method == "Audio" else "text"
                save_to_corpus(user_input, intent, input_source, letter)
                
                # Save to history
                letter_data = {
                    "intent": intent,
                    "input": user_input,
                    "letter": letter,
                    "language": language.lower(),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                save_letter_history(letter_data)
                
                # Display results
                st.subheader(T["output_title"])
                
                # Show intent detection
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
                
                # Display letter
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