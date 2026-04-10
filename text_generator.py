from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def generate_text():
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="Write a short Krishna motivational quote in Hindi"
    )
    return response.text.strip()
