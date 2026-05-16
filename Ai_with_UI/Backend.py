
    
# ========= streamlit============================================

import streamlit as st
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

st.title("Basic Bot")

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

if "messages" not in st.session_state:
    st.session_state.messages = []

for idx, msg in enumerate(st.session_state.messages):
    if idx % 2 == 1:
        with st.chat_message("assistant"):
            st.markdown(msg.parts[0].text)
    else:
        with st.chat_message(msg.role):
            st.markdown(msg.parts[0].text)
            
    # print(msg.role)
    # print(msg.parts[0].text)

prompt = st.chat_input("Ask your question...")

# Content(
#   parts=[
#     Part(
#       text='hi'
#     ),
#   ],
#   role='user'
# )
if prompt:
    
    if prompt in {"bye", "exit"}:
        st.success("Thanks for chat")
        st.stop()
    
    st.session_state.messages.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=str(prompt))]
        )
    )
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.spinner("In Progress..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=st.session_state.messages
        )
        # print(response,'response--')
        
    if response.text:
        st.session_state.messages.append(
            types.Content(
                role="model",
                parts=[types.Part.from_text(text=str(response.text))]
            )
        )
            
        # print(st.session_state.messages,'jjjjjjjjjj')  
        
        with st.chat_message("assistant"):
            st.markdown(response.text)

    else:
        st.warning("Empty response from the Model...")





