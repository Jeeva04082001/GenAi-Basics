
    
# ========= streamlit============================================
import streamlit as st
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Import your custom tools
from tools_schema import tools
from weather_tools import get_weather
load_dotenv()

# --- 1. App Configuration & Setup ---
st.set_page_config(page_title="Weather Bot", page_icon="🌤️")
st.title("Basic Weather Bot")

# Safely load the system prompt
try:
    with open("system_prompt.txt", 'r') as f:
        instruction = f.read()
except FileNotFoundError:
    st.warning("system_prompt.txt not found. Using default instructions.")
    instruction = "You are a helpful assistant."

# Securely initialize the client (Set GEMINI_API_KEY in environment or .streamlit/secrets.toml)
# api_key = "AIzaSyBglCHHhs-MDp5vuPhDUPeTLitJx_ACZrQ"
client = genai.Client(api_key=os.getenv("GEMINI_API_PAID_KEY"))

functions = types.Tool(function_declarations=tools())

# --- 2. Initialize Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. Render Chat History ---
for msg in st.session_state.messages:
    display_text = ""
    
    print(display_text,'display_text--------------------')
    
    
    # Extract text from the parts. We ignore function calls/responses in the UI loop.
    for part in msg.parts:
        if hasattr(part, "text") and part.text:
            display_text += part.text + "\n"
    
    # Only render UI chat bubbles for actual text messages
    if display_text.strip():
        # Map Gemini roles to Streamlit roles
        role = "assistant" if msg.role == "model" else "user"
        with st.chat_message(role):
            st.markdown(display_text.strip())

    
# --- 4. Handle User Input ---
prompt = st.chat_input("Ask your question...")

if prompt:
    
    if prompt.lower() in {"bye", "exit"}:
        st.success("Thanks for chatting!")
        st.stop()
    
    # Render user prompt immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Append the user's content to the session state
    user_content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=prompt)]
    )
    st.session_state.messages.append(user_content)
    
    # Helper configuration to keep code DRY
    gen_config = types.GenerateContentConfig(
        tools=[functions],
        system_instruction=instruction,
        temperature=0.5
    )

    with st.spinner("Thinking..."):
        try:
            # First API Call
            print(prompt,'prompt---------')
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=st.session_state.messages,
                config=gen_config
            )
            
            print(response,'response---')
            
            # Append the model's exact response (text OR function call) to history
            model_content = response.candidates[0].content
            st.session_state.messages.append(model_content)
            
            print(model_content,'model_content---------')
            
            
            # Check for function calls in the model's response
            function_calls = [
                part.function_call for part in model_content.parts 
                if hasattr(part, "function_call") and part.function_call
            ]
            
            if function_calls:
                function_response_parts = []
                
                # Execute tools
                for call in function_calls:
                    if call.name == "get_weather_data":
                        city = call.args.get("city")   
                        state = call.args.get("state")   
                        country = call.args.get("country")
                        
                        print(f"Executing get_weather_data with city={city}, state={state}, country={country}")
                        weather_data = get_weather(city=city, state=state, country=country)
                        
                        print(weather_data,'weather_data---------')
                        # Build the response part
                        func_part = types.Part.from_function_response(
                            name=call.name,
                            response={"result": str(weather_data)}
                        )
                        function_response_parts.append(func_part)
                
                # Append the tool execution results back to history
                print(function_response_parts,'function_response_parts-------')
                if function_response_parts:
                    func_response_content = types.Content(
                        role='user', # Gemini requires function responses to be passed by the user
                        parts=function_response_parts
                    )
                    st.session_state.messages.append(func_response_content)
                    
                    # Second API Call: Let the model read the tool results and answer
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=st.session_state.messages,
                        config=gen_config
                    )
                    
                    print(response,'response-------222')
                    
                    
                    # Append the final text response to history
                    st.session_state.messages.append(response.candidates[0].content)

            # --- 5. Display Final Output ---
            # Retrieve text from the absolute final message in the chain
            final_text = ""
            last_msg = st.session_state.messages[-1]
            
            print(st.session_state.messages,'st.session_state.messages----------')
            for part in last_msg.parts:
                if hasattr(part, "text") and part.text:
                    final_text += part.text + "\n"

            if final_text.strip():
                with st.chat_message("assistant"):
                    st.markdown(final_text.strip())
            else:
                st.warning("Empty response from the Model...")
                
        except Exception as e:
            st.error(f"An error occurred with the API: {str(e)}")