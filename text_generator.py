import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_text():
    response = model.generate_content(
        "Short Krishna motivational quote in Hindi"
    )
    return response.text.strip()
