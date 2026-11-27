#Combine multi-turn chat + streaming into a tiny terminal chatbot:

#Create a chat = client.chats.create(...).

#Start a while True: loop that reads user_input = input("You: ").

#Break out of the loop if user_input.lower() in {"exit", "quit"}.

#Otherwise, stream the reply with chat.send_message_stream(user_input) and print each chunk live!

import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors,types

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing Gemini_api_key")

client=genai.Client(api_key=api_key)

config=types.GenerateContentConfig(
    system_instruction="You are a clear technical tutor,Give replies properly",
    temperature=0.3,)
try:
    
    chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=config,)
    
    print("Welcome to the Hari's chatbot! Type your questions below. Type 'exit' or 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in{"exit","quit"}:
            print("Exiting chat. Goodbye!")
            break
        if not user_input:
            continue
        response_stream = chat.send_message_stream(user_input)
        for chunk in response_stream:
          print(chunk.text, end="", flush=True)
        print()  # Final newline after stream finishes

except errors.APIError as e:
    print(f"\nAPI Error: {e}")
except Exception as e:
    print(f"\nError: {e}")
        