
# ==============================================================================================
# ==================== 04-09-2026 ==========================================================================

import streamlit as st
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from weather_tools import get_weather
from tools_schema import tools
load_dotenv()


st.set_page_config(page_title="Weather Bot", page_icon="🌤️")
st.title("Basic Weather Bot")


try:
    with open("system_prompt.txt", 'r') as f:
        instructions = f.read()
except FileNotFoundError:
    st.warning("system_prompt.txt not found. Using default instructions.")
    instructions = "You are a helpful assistant"

client = genai.Client(api_key=os.getenv("GEMINI_API_PAID_KEY"))

functions = types.Tool(function_declarations=tools())

if "messages" not in st.session_state:
    st.session_state["messages"]=[]

for msg in st.session_state.messages:
    display_text = ""
    
    for part in msg.parts:
        if hasattr(part, "text") and part.text:
            display_text += part.text + "\n"
            
    if display_text.strip():
        role = "assistant" if msg.role == "model" else "user"
        with st.chat_message(role):
            st.markdown(display_text.strip())
               
prompt = st.chat_input("Ask your Question....")

if prompt:
    
    if prompt.lower() in {"bye","q","exit","end"}:
        st.success("Thanks for the Chatting")
        st.stop()
        
    with st.chat_message("user"):
        st.markdown(prompt)
    
    user_content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=str(prompt))]
    )
    st.session_state.messages.append(user_content)
    
    gen_config= types.GenerateContentConfig(
        tools=[functions],
        system_instruction=instructions,
        temperature=0.5
    )
    
    with st.spinner("thinking......."):
        try:
            
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite',
                contents=st.session_state.messages,
                config=gen_config
            )
            
            print(response,'response------')
            
            model_content = response.candidates[0].content
            st.session_state.messages.append(model_content)
            
            print(model_content,'model_content---------')
            function_calls = [
                part.function_call for part in model_content.parts
                if hasattr(part, "fucntion_call") and part.function_call
            ]
            
            if function_calls:
                function_response_parts = []
                
                for call in function_calls:
                    if call.name == "get_weather_data":
                        city = call.args.get("city")   
                        state = call.args.get("state")   
                        country = call.args.get("country")
                        print(f"Executing get_weather_data with city={city}, state={state}, country={country}")
                        
                        
                        weather_data = get_weather(city=city,state=state,country=country)
                        
                        print(weather_data,'weather_data----------')
                        
                        func_part = types.Part.from_function_response(
                            name = call.name,
                            response={"result": str(weather_data)}
                        )    
                        
                        function_response_parts.append(func_part)
                print(function_response_parts,'function_response_parts----------')          
                if function_response_parts:
                    function_response_content = types.Content(
                        role='user',
                        parts=function_response_parts
                    )  
                    
                    st.session_state.messages.append(function_response_content)     
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=st.session_state.messages,
                        config=gen_config
                    )   
                    
                    print(response,'response-----')
                    
                    st.session_state.messages.append(response.candidates[0].content)                     
                        
            
            final_text = ""
            last_msg = st.session_state.messages[-1]
            
            print(st.session_state.messages,'st.session_state.messages--')
            
            
            for part in last_msg.parts:
                if hasattr(part,'text') and part.text:
                    final_text += part.text + "\n"
                    
            if final_text.strip():
                with st.chat_message("assistant"):
                    st.markdown(final_text.strip())
            
            else:
                st.warning("Empty response from the Model...")
        except Exception as e:
            st.error(f"An error occured with the API: {str(e)}")


            
            
            
            
            
            
            
            
            
            
            
            
            
            
                




          
# ==============================================================================================
# ========= streamlit===== 09-06-2026 ====================

# import streamlit as st
# from google import genai
# from google.genai import types
# from dotenv import load_dotenv
# from tools_schema import tools
# from weather_tools import get_weather
# import os
# load_dotenv()


# st.set_page_config(page_title="Weather Bot", page_icon="🌤️")
# st.title("Basic Weather Bit")

# try:
#     with open("system_prompt.txt","r") as f:
#         instruction = f.read()
# except FileNotFoundError:
#     st.warning("system_prompt.txt no found. Using default instruction")    

#     instruction = "You are a helpful assistant."

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY1"))

# functions = types.Tool(function_declarations=tools())


# if "messages" not in st.session_state:
#     st.session_state.messages=[]

# for msg in st.session_state.messages:
    
#     print(msg,'msg---------')
#     print("--------------------------")
#     display_text=""
    
#     for part in msg.parts:
#         if hasattr(part, "text") and part.text:
#             display_text += part.text + "\n"
    
#     if display_text.strip():
#         role = "assistant" if msg.role == "model" else "user"  
#         with st.chat_message(role):
#             st.markdown(display_text.strip())
            
#     print(display_text,'display_text')
           
# prompt = st.chat_input("Ask your question...")

# if prompt:
#     if prompt.lower() in {"bye","exit","q","end"}:
#         st.success("Thanks for the Chat!")
#         st.stop()
    
#     with st.chat_message("user"):
#         st.markdown(prompt)
        
#     user_content = types.Content(
#         role="user",
#         parts=[types.Part.from_text(text=str(prompt))]
#     )
    
#     st.session_state.messages.append(user_content)
    
#     gen_config = types.GenerateContentConfig(
#         tools=[functions],
#         system_instruction=instruction,
#         temperature=0.5
#     )
    
#     with st.spinner("Thinking..."):
#         try:
#             print("prompt-----------",prompt)
#             print("-------------------------------------")
            
#             response = client.models.generate_content(
#                 model="gemini-2.5-flash",
#                 contents=st.session_state.messages,
#                 config=gen_config
#             )
            
#             print(response,'response--------------')
#             print("---------------------------------------------")
            
#             model_content = response.candidates[0].content
#             st.session_state.messages.append(model_content)

#             print(model_content,'model_content-----')
#             function_calls=[
#                 part.function_call for part in model_content.parts
#                 if hasattr(part,"function_call") and part.function_call
#             ]
            
#             print(function_calls,'function_calls----1')
#             if function_calls:
#                 function_response_parts = []
                
#                 for call in function_calls:
                    
#                     print(call,'call----------')
#                     if call.name == "get_weather_data":
#                         city = call.args.get("city")
#                         state = call.args.get("state")
#                         country = call.args.get("country")
                        
#                         print(f"Executing get_weather_data with city={city}, state={state}, country={country}")
                        
#                         weather_data = get_weather(city=city,state=state,country=country)

#                         print(weather_data,'weather_data---------')
                        
#                         func_part = types.Part.from_function_response(
#                             name=call.name,
#                             response = {"result": str(weather_data)}
#                         )
                        
#                         print(func_part,'func_part-----------')
                        
#                         function_response_parts.append(func_part)
#                 print(function_response_parts,"function_response_parts-------------")
                
#                 if function_response_parts:
#                     func_response_content = types.Content(
#                         role='user',
#                         parts=function_response_parts
#                     )
#                     st.session_state.messages.append(func_response_content)

#                     response = client.models.generate_content(
#                         model="gemini-2.5-flash",
#                         contents=st.session_state.messages,
#                         config=gen_config
#                     )
                    
#                     print(response,'response-------222')
#                     print("-------------------------------------")
                    
#                     st.session_state.messages.append(response.candidates[0].content)
#             print(function_calls,'function_calls----22222')

#             final_text = ""
#             last_msg = st.session_state.messages[-1]
#             print(st.session_state.messages,'st.session_state.messages----------')
#             print("--------------------------------------------------------")
            
#             for part in last_msg.parts:
#                 if hasattr(part,"text") and part.text:
#                     final_text += part.text + "\n"
            
#             if final_text.strip():
#                 with st.chat_message("assistant"):
#                     st.markdown(final_text.strip())

#             else:
#                 st.warning("Empty response from the Model....")
#         except Exception as e:
#             st.error(f"An error occured with the API: {str(e)}")







