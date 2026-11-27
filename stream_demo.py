#this chat used to print patch by patch in the screen instead of waiting for the whole content to be displayed

import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing GEMINI_API_KEY. Add it to your .env file before running.")

client = genai.Client(api_key=api_key)

config = types.GenerateContentConfig(
    system_instruction="You are a clear backend mentor. Explain step by step.",
    temperature=0.4,
)

try:
    response = client.models.generate_content_stream(
        model="gemini-3.8-flash",
        contents="Explain how HTTP request and response work in 4 short steps.",
        config=config,
    )

    for chunk in response:
        print(chunk.text, end="", flush=True)
    print()  # Final newline after stream finishes

except errors.APIError as e:
    print(f"\nAPI Error: {e}")
except Exception as e:
    print(f"\nError: {e}")