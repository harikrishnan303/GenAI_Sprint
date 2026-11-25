import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors,types

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing GEMINI_API_KEY, Add it to your .env file before running.")

client=genai.Client(api_key=api_key)

#this bloack decides the output format
config=types.GenerateContentConfig(
    system_instruction=("You are a concise backend mentor."
                        "Reply in atmost 2 sentences."),
    temperature=0.1,#decides randomness of words
    
)

try: #this block handles the api call and what content to generate
    response=client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="why we need to live?",
        config=config,
    )
    print(response.text)
except errors.APIError as e:
    print(f"API ERROR:{e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")