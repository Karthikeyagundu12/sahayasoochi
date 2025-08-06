# SahayaSoochi Configuration File

# App Settings
APP_NAME = "SahayaSoochi"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI Letter Generator for Government Applications"

# Audio Recording Settings
RECORDING_DURATION = 5  # seconds
SAMPLE_RATE = 44100
CHANNELS = 1

# File Paths
CORPUS_FILE = "corpus.csv"
HISTORY_FILE = "letter_history.json"
AUDIO_FILE = "input.wav"

# Supported Languages
SUPPORTED_LANGUAGES = {
    "en": "English",
    "te": "తెలుగు"
}

# Default Districts and Mandals (for template filling)
DEFAULT_DISTRICTS = [
    "Adilabad", "Bhadradri Kothagudem", "Jagtial", "Jangaon", "Jayashankar Bhupalpally",
    "Jogulamba Gadwal", "Kamareddy", "Karimnagar", "Kumuram Bheem", "Mahabubabad",
    "Mahabubnagar", "Mancherial", "Medak", "Medchal–Malkajgiri", "Mulugu", "Nagarkurnool",
    "Nalgonda", "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli", "Rajanna Sircilla",
    "Rangareddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad", "Wanaparthy",
    "Warangal Rural", "Warangal Urban", "Yadadri Bhuvanagiri"
]

DEFAULT_MANDALS = [
    "Adilabad", "Bhadrachalam", "Jagtial", "Jangaon", "Bhupalpally", "Gadwal",
    "Kamareddy", "Karimnagar", "Asifabad", "Mahabubabad", "Mahabubnagar",
    "Mancherial", "Medak", "Medchal", "Mulugu", "Nagarkurnool", "Nalgonda",
    "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli", "Sircilla", "Rangareddy",
    "Sangareddy", "Siddipet", "Suryapet", "Vikarabad", "Wanaparthy",
    "Warangal", "Warangal", "Bhuvanagiri"
]

# Intent Detection Keywords
INTENT_KEYWORDS = {
    "birth_certificate": [
        "birth", "janmam", "janma", "puvvu", "puvvudu", "certificate", "pattanam",
        "పుట్టిన", "జన్మ", "పుట్టిన తేదీ", "ధృవీకరణ పత్రం"
    ],
    "ration_card": [
        "ration", "ration card", "rationcard", "rice", "sugar", "kerosene", "pds",
        "రేషన్", "రేషన్ కార్డు", "బియ్యం", "చక్కెర", "మట్టి నూనె"
    ],
    "income_certificate": [
        "income", "aadayam", "salary", "job", "employment", "earnings", "poverty",
        "ఆదాయం", "ఆదాయ ధృవీకరణ", "జీతం", "పని", "వృత్తి"
    ],
    "caste_certificate": [
        "caste", "kulam", "community", "jati", "category", "sc", "st", "obc",
        "కులం", "కుల ధృవీకరణ", "సమాజం", "వర్గం"
    ],
    "residence_certificate": [
        "residence", "vasam", "address", "domicile", "local", "permanent",
        "నివాస", "నివాస ధృవీకరణ", "చిరునామా", "స్థిర నివాసం"
    ],
    "tax_exemption": [
        "tax", "property tax", "house tax", "exemption", "rebate", "discount",
        "పన్ను", "ఆస్తి పన్ను", "మినహాయింపు", "రాయితీ"
    ]
}

# Letter Template Placeholders
TEMPLATE_PLACEHOLDERS = {
    "applicant_name": "[Applicant Name]",
    "phone_number": "[Phone Number]",
    "mandal": "[Mandal Name]",
    "district": "[District Name]",
    "address": "[Address]",
    "child_name": "[Child Name]",
    "dob": "[Date of Birth]",
    "place": "[Place of Birth]",
    "hospital": "[Hospital Name]",
    "gender": "[Gender]",
    "family_members": "[Number of Family Members]",
    "income": "[Annual Income]",
    "occupation": "[Occupation]",
    "purpose": "[Purpose]",
    "father_name": "[Father's Name]",
    "caste": "[Caste]",
    "sub_caste": "[Sub-caste]",
    "duration": "[Duration]",
    "property_address": "[Property Address]",
    "property_type": "[Property Type]",
    "assessment_no": "[Assessment Number]",
    "tax_amount": "[Tax Amount]",
    "reason": "[Reason for Exemption]",
    "Municipality": "[Municipality Name]"
}

# UI Configuration
UI_CONFIG = {
    "page_title": "SahayaSoochi",
    "page_icon": "✉️",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Mobile Responsive CSS
MOBILE_CSS = """
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
""" 