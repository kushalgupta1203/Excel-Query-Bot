import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(dotenv_path=os.path.abspath(os.path.join(os.getcwd(), ".env")))

print(os.getenv("GEMINI_API_KEY"))  # Should print your API key, NOT None

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Hello, how are you?")
    print(response.text)
except Exception as e:
    print("Error:", e)
