from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ✅ List of models (priority order)
MODELS = [
    "gemini-2.0-flash",
    "gemini-1.5-pro",
    "gemini-1.5-flash"
]

def generate_text():
    prompt = "Write a short Krishna motivational quote in Hindi (1 line only)"

    for model_name in MODELS:
        try:
            print(f"Trying model: {model_name}")

            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            if response.text:
                print(f"✅ Success with: {model_name}")
                return response.text.strip()

        except Exception as e:
            print(f"❌ Failed: {model_name} -> {e}")

    # ❌ If all fail
    return "कर्म करो, फल की चिंता मत करो।"
