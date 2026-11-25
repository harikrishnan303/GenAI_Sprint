import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors,types
from pydantic import BaseModel,Field #pydantic is python library used to validate and parse the output

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing GEMINI_API_KEY, Add it to your .env file before running.")

client=genai.Client(api_key=api_key)

class ConceptSummary(BaseModel):#used define the output format and validate the output
    topic:str=Field(description="short title of the concept")#Field() is a helper function used to validate rules
    one_line_summary:str=Field(description="Clear explanation in one sentenece")
    key_points:list[str]=Field(description="2 to 3 short bullent points")
    
config=types.GenerateContentConfig(#used to configure the output
    system_instruction="You are a clear technical tutor.Follow the requested schema",
    temperature=0.3,
    response_mime_type="application/json",#tells to return output in this formate
    response_schema=ConceptSummary,)#structure of output
try:
    response=client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Explain rotation of electric fan",
        config=config,
        
    )
    
    parsed=ConceptSummary.model_validate_json(response.text)#model _validate_json used to read
    
    print("Topic: ", parsed.topic)
    print("One-line Summary: ", parsed.one_line_summary)
    print("Key Points:")
    for point in parsed.key_points:
        print(f" - {point}")
        
except errors.APIError as e:
    print(f"API ERROR:{e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")