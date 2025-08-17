# ✅ test_gemini.py — quick test for Gemini letter generation
from gemini_api import generate_letter

test_inputs = [
    "naku death certificate kavali",
    "office ki leave kavali 2 days fever valla",
    "road repair complaint pettali",
    "naku caste certificate kavali"
]

for text in test_inputs:
    print("\n📝 Input:", text)
    print("📄 Output:", generate_letter(text, "English"))
