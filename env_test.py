import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")
app_name=os.getenv("MY_APP_NAME")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

print("App Name:",app_name)
print("key loaded succesfully",bool(api_key))