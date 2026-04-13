from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
contents = []
# contents = types.Content(
#     role='user',
#     parts=[types.Part.from_text(text='Why is the sky blue?')]
# )

while True:
    prompt = input("user: ")
    if prompt in ['bye','q','exit','end']:
        print("thanks for the chat!")
        break
    contents.append(types.Content(
        role='user',
        parts=[types.Part.from_text(text=str(prompt))]
    ))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            temperature=0.5
        )
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


