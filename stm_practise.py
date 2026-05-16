
# ----------- ---------- Example-1 -------------- --------------#


from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

contents=[]

while True:
    prompt = input("user: ")
    if prompt in {'bye','q','end'}:
        print("thank for chat!")
        break
    contents.append(
        types.Content(
            role='user',
            parts=[types.Part.from_text(text=str(prompt))]
        )
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=contents,
        
    )
    
    if not response or response.text is None:
        print("Empty response from model")
        break
    
    if response.text:
        contents.append(
            types.Content(
                role='model',
                parts=[types.Part.from_text(text=str(response.text))]
            )
        )
        print(f"Bot: {response.text}")
    
    
    
#   =================================================================

# ----------- ---------- Example-2 -------------- --------------#

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

contents=[]

with open("system_prompt.txt", "r") as f:
    instructions = f.read()

while True:
    prompt = input("user: ")
    if prompt in {'bye','q','end'}:
        print("thank for chat!")
        break
    
    # system_prompt = f"system instructions: {instructions} \n\n user query: {prompt}"
    contents.append(
        types.Content(
            role='user',
            parts=[types.Part.from_text(text=str(prompt))]
        )
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=contents,
        config=types.GenerateContentConfig(
        system_instruction=instructions),
        
    )
    
    if not response or response.text is None:
        print("Empty response from model")
        break
    
    if response.text:
        contents.append(
            types.Content(
                role='model',
                parts=[types.Part.from_text(text=str(response.text))]
            )
        )
        print(f"Bot: {response.text}")
    
    
    
    
    
    
    
    
    













  
    
    
    
    
    













