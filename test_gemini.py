from gemini_api import generate_letter

# Sample input in Roman Telugu
test_input = "Naku income certificate kavali. Na peru Ramu. Address Hyderabad."

try:
    print("🔄 Testing Gemini API with sample input...\n")
    result = generate_letter(test_input)
    print("✅ Gemini API Response:\n")
    print(result)
except Exception as e:
    print("❌ Error while calling Gemini API:")
    print(e)
