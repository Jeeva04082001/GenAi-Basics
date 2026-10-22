
# ==============================================================================================
# ==================== 03-09-2026 ==========================================================================

# ----- Example-1 ---------------------------------------

# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# contents=[]

# while True:
#     prompt = input("user: ")
    
#     if prompt in ['q','exit','end','bye']:
#         print("thanks for the chat!")
#         break
#     contents.append(types.Content(
#         role='user',
#         parts=[types.Part.from_text(text=str(prompt))]
#     ))
    
#     response = client.models.generate_content(
#         model="gemini-2.5-flash-lite",
#         contents=contents,
#         config=types.GenerateContentConfig(
#             temperature=0.5
#         )
#     )
    
#     if not response or response.text is None:
#         print("Empty response from model")
#         break
    
#     if response.text:
#         contents.append(types.Content(
#             role='model',
#             parts=[types.Part.from_text(text=str(response.text))]
#         ))
        
#         print(f"Bot: {response.text}")
#         print(contents,'cc-----------------')


# ----- Example-2 ---------------------------------------

# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# contents = []

# while True:
#     prompt = input("User: ")
#     if prompt in {'q','bye','exit','end'}:
#         print("Thanks for the chat!")
#         break
    
#     contents.append(types.Content(
#         role='user',
#         parts=[types.Part.from_text(text=str(prompt))]
#     ))
    
#     response = client.models.generate_content(
#         model="gemini-2.5-flash-lite",
#         contents=contents,
#         config=types.GenerateContentConfig(
#             temperature=0.5
#         )
#     )
    
#     if not response or response.text is None:
#         print("Empty response from the model")
#         break
    
#     if response.text:
#         contents.append(
#             types.Content(
#                 role="model",
#                 parts=[types.Part.from_text(text=str(response.text))]
#             )
#         )
        
#         print(f"Bot: {response.text}")
#         print(contents,'coo---------------')


# ----- Example-3 ---------------------------------------


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
    prompt= input("User: ")
    if prompt in {'bye','end','exit','q'}:
        print("thanks for the chat!")
        break
    
    contents.append(types.Content(
        role='user',
        parts=[types.Part.from_text(text=str(prompt))]
    ))

    response = client.models.generate_content(
        model='gemini-2.5-flash-lite',
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=instructions
        )
    )
    
    if not response or response.text is None:
        print("Empty response from model")
        break
    
    if response.text:
        contents.append(types.Content(
            role="model",
            parts=[types.Part.from_text(text=str(response.text))]
        ))
        
        print(f"Bot: {response.text}")
        print(contents,'gg-----------------------')


# ==============================================================================================
# ==============================================================================================

#------------- 08-06-2026--- Example-1 ------------

# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# contents=[]

# while True:
#     prompt = input("user: ")
#     if prompt in ['bye','q','exit','end']:
#         print("Thanks for the Chat!")
#         break
#     contents.append(types.Content(
#         role='user',
#         parts=[types.Part.from_text(text=str(prompt))]
#     ))
    
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=contents,
#         config=types.GenerateContentConfig(
#             temperature=0.5
#         )
#     )
    
#     if not response or response.text is None:
#         print("Empty response from model")
#         break
    
#     if response.text:
#         contents.append(
#             types.Content(
#                 role='model',
#                 parts=[types.Part.from_text(text=str(response.text))]
#             )
#         )
        
#         print(f"Bot: {response.text}")
#         print(contents,'contents----------')



#------------- 08-06-2026--- Example-2 ------------

# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()


# # client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# client = genai.Client(api_key="AIzaSyBO-keD9IaehJetsP1TxWJjSEGFyTfCO2M")
# contents=[]

# while True:
#     prompt = input("user: ")
#     if prompt in {'bye','q','exit','end'}:
#         print("Thanks for the chat!")
#         break
#     contents.append(types.Content(
#         role='user',
#         parts=[types.Part.from_text(text=str(prompt))]
#     ))
    
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=contents
        
#     )
    
#     # print(contents,'contents-----')
#     # print(response,'response-----')
    
#     if not response or response.text is None:
#         print("Empty response from model")
#         break
    
#     if response.text:
#         contents.append(
#             types.Content(
#                 role='model',
#                 parts=[types.Part.from_text(text=str(response.text))]
#             )
#         )
        
#         print(f"BOT: {response.text}")

#------------- 09-06-2026--- Example-3 ------------

# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()


# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# contents = []

# with open("system_prompt.txt","r") as f:
#     instructions = f.read()
    
# while True:
#     prompt = input("user: ")
#     if prompt in {'bye','q','exit','end'}:
#         print("thanks for the chat!")
#         break
#     contents.append(
#         types.Content(
#             role='user',
#             parts=[types.Part.from_text(text=str(prompt))]
#         )
#     )
    
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=contents,
#         config=types.GenerateContentConfig(
#             system_instruction=instructions
#         )
#     )
    
#     print(response,'response----')
#     print("------------------------------------------------------")
#     print(contents,'contents-----------------')
#     print("------------------------------------------------------")
    
    
#     if not response or not response.text:
#         print("Empty response form model!")
#         break
    
#     if response.text:
#         contents.append(
#             types.Content(
#                 role='model',
#                 parts=[types.Part.from_text(text=str(response.text))]
#             )
#         )
        
#         print(f"Bot: {response.text}")
        

# ==============================================================================================
# ==============================================================================================


#------------- 30-05-2026---------------


# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()


# client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# contents=[]

# while True:
#     prompt=input("user: ")
#     if prompt in ['bye','q','exit','end']:
#         print("thanks for the chat!")
#         break
    
#     contents.append(types.Content(
#         role='user',
#         parts=[types.Part.from_text(text=str(prompt))]
#     ))
    
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=contents,
#         config=types.GenerateContentConfig(
#             temperature=0.5
#         )
#     )
    
#     if not response or response.text is None:
#         print("Empty response from model")
#         break
    
#     if response.text:
#         contents.append(
#             types.Content(
#                 role='model',
#                 parts=[types.Part.from_text(text=str(response.text))]
#             )
#         )
        
#         print(f"Bot : {response.text}")
#         print(f"Response : {response}")
#         print('contents: ',contents)

# ==================================================================================


# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()


# client= genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# contents=[]

# with open("system_prompt.txt","r") as f:
#     instructions=f.read()

# while True:
#     prompt=input("user: ")
#     if prompt in {'bye','exit','q','end'}:
#         print("thanks for the chat!")
#         break
    
#     contents.append(
#         types.Content(
#             role='user',
#             parts=[types.Part.from_text(text=str(prompt))]
#         )
#     )
    
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=contents,
#         config=types.GenerateContentConfig(
#             system_instruction=instructions
#         ),
#     )
    
#     if not response or response.text is None:
#         print("Empty response from model")
#         break
    
#     if response.text:
#         contents.append(
#             types.Content(
#                 role='model',
#                 parts=[types.Part.from_text(text=str(response.text))]
#             )
#         )
#         print(f"Bot: {response.text}")
    
    
    
    
    
    
    
    
    
    

