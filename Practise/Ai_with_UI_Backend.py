# ==============================================================================================
# ==================== 03-09-2026 ==========================================================================

# streamlit run .\Ai_with_UI_Backend.py == running file command

import streamlit as st
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()


st.title("Simple Bot") 
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

if "messages" not in st.session_state:
    st.session_state["messages"]=[]
    
for idx,msg in enumerate(st.session_state.messages):
    print(msg,'msg------------------')
    
    if idx % 2 == 1:
        with st.chat_message("assistant"):
            st.markdown(msg.parts[0].text)
    else:
        with st.chat_message(msg.role):
            st.markdown(msg.parts[0].text)
            
prompt = st.chat_input("Ask your question.......")

if prompt:
    
    if prompt in {'bye','end','exit','q'}:
        st.success("Thanks for the chat!")
        st.stop()
    
    st.session_state.messages.append(types.Content(
        role='user',
        parts=[types.Part.from_text(text=str(prompt))]
    ))
    
    with st.chat_message('user'):
        st.markdown(prompt)
        
    with st.spinner("In progress......."):
        
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite',
            contents=st.session_state.messages
        )
        
        if response.text:
            st.session_state.messages.append(types.Content(
                role='model',
                parts=[types.Part.from_text(text=str(response.text))]
            ))
            
            with st.chat_message("assistant"):
                st.markdown(response.text)

        else:
            st.warning("Empty response from the model...")






        
# ==============================================================================================
#------------- 09-06-2026---------------

# from google import genai
# import streamlit as st
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()


# st.title("Basic Bot")

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# if "messages" not in st.session_state:
#     st.session_state.messages=[]

# for idx,msg in enumerate(st.session_state.messages):
#     print(msg,'msg----------------')
#     print("-----------------------------------------------")
#     if idx % 2 == 1:
#         with st.chat_message("assistant"):
#             st.markdown(msg.parts[0].text)
    
#     else:
#         with st.chat_message(msg.role):
#             st.markdown(msg.parts[0].text)

# prompt = st.chat_input("Ask your question")

# if prompt:
#     if prompt in {"exit","bye","q","end"}:
#         st.success("Thanks for the chat!")
#         st.stop()
        
#     st.session_state.messages.append(
#         types.Content(
#             role='user',
#             parts=[types.Part.from_text(text=str(prompt))]
#         )
#     )  
    
#     with st.chat_message("user"):
#         st.markdown(prompt)     
    
#     with st.spinner("In Progress........."):
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=st.session_state.messages
#         )
        
#         print(response,'response--')
#         print('------------------------------------')
    
    
#     if response.text:
#         st.session_state.messages.append(
#             types.Content(
#                 role="model",
#                 parts=[types.Part.from_text(text=str(response.text))]
#             )
#         )
        
#         with st.chat_message("assistant"):
#             st.markdown(response.text)
#     else:
#         st.warning("Empty response from the Model.....")
    
    
    
    
# ============================================================================================== 
#------------- 30-05-2026---------------


# import streamlit as st
# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# load_dotenv()


# st.title("Basic Bot")
# client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

# if "messages" not in st.session_state:
#     st.session_state.messages=[]
    

# for idx, msg in enumerate(st.session_state.messages):
#     if idx % 2 == 1:
#         with st.chat_message("assistant"):
#             st.markdown(msg.parts[0].text)
#     else:
#         with st.chat_message(msg.role):
#             st.markdown(msg.parts[0].text)
    
#     print(msg,'msg-----------')
#     print(msg.role)       
#     print(msg.parts[0].text)       


# prompt = st.chat_input("Ask your questions...")

# if prompt:
#     if prompt in {"bye","exit"}:
#         st.success("Thanks for tha chat!")
#         st.stop()
        
#     st.session_state.messages.append(
#         types.Content(
#             role='user',
#             parts=[types.Part.from_text(text=str(prompt))]
#         )
#     )
    
#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     with st.spinner("In Progress..."):
#         response=client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=st.session_state.messages
#         )
        
#     if response.text:
#         st.session_state.messages.append(
#             types.Content(
#                 role="model",
#                 parts=[types.Part.from_text(text=str(response.text))]
#             )
#         )  
        
#         with st.chat_message("assistant"):
#             st.markdown(response.text)
#     else:
#         st.warning("Empty response from the Model...")        
         
    
    
    































































