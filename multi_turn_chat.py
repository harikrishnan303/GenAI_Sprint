#Used to demonstrate multi questions in a single chat and remebering the previous ones


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
    system_instruction="You are a concise Python tutor. Keep replies under 3 sentences.",
    temperature=0.4,
)

try:
    # 1. Create a stateful chat session
    chat = client.chats.create(
        model="gemini-3.5-flash-lite",
        config=config,
    )

    # 2. First turn
    r1 = chat.send_message("I'm learning lists and tuples in Python.")
    print("Turn 1:", r1.text, "\n")

    # 3. Second turn (remembers Turn 1 without repeating it!)
    r2 = chat.send_message("Which one should I use if my data shouldn't change?")
    print("Turn 2:", r2.text, "\n")

    # 4. Inspect stored conversation history
    print(f"Total messages stored in history: {len(chat.get_history())}")

except errors.APIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"Error: {e}")