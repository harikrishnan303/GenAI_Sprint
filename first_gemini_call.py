import os
from dotenv import load_dotenv
load_dotenv()
from google import genai
from google.genai import errors


api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing GEMINI_API_KEY. Add it to your .env file before running.")

client=genai.Client(api_key=api_key)

try:
    response=client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Explain photosynthesis"
    )
    print(response.text)
except errors.APIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")