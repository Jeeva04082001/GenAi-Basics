

# ==============================================================================================
# ==================== 04-09-2026 ==========================================================================










# ==============================================================================================

# from datetime import datetime
# from google import genai
# from google.genai import types
# import os
# from dotenv import load_dotenv
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from contextlib import asynccontextmanager
# import asyncpg

# load_dotenv()



# @asynccontextmanager
# async def lifespan(app: FastAPI):
    
#     app.state.db = await asyncpg.create_pool(
#         user="postgres",
#         password="Itispossible@2001",
#         database="AgentPractise",
#         host="localhost",
#         port=5432,
#         min_size=1,
#         max_size=10
#     )

#     print("Database Connected")
    
#     yield
    
#     await app.state.db.close()
    
#     print("Databse Closed")

# app = FastAPI(lifespan=lifespan)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credientials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# async def insert_chat(
#     app,
#     userid:str,
#     chatid:int,
#     user_chat:str,
#     model_chat:str,
#     chat_summary:str=None,
#     input_token:int=0,
#     output_token:int=0
# ):
    
#     current_time = datetime.now()
    
#     async with app.state.db.acquire() as conn:
        
#         await conn.execute(
#             """
#             INSERT INTO chats (
#                 chatid,
#                 userid,
#                 user_chat,
#                 model_chat,
#                 chat_summary,
#                 input_token,
#                 output_token,
#                 firstchat_time,
#                 lastchat_time,
#                 created_at,
#                 updated_at
#             )
#             VALUES (
#                 $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11
#             )
#             """,
#             chatid,
#             userid,
#             user_chat,
#             model_chat,
#             chat_summary,
#             input_token,
#             output_token,
#             current_time,
#             current_time,
#             current_time,
#             current_time
            
#         )
        
#         return {
#             "status":"success",
#             "message":"Chat inserted successfully"
#         }


# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")) 

# with open("system_prompt.txt","r") as f:
#     instructions = f.read() 

# def text_form(text:str):
#     return types.Content(
#         role='user',
#         parts=[types.Part.from_text(text=str(text))]
#     )

# def function_response_form(name:str,response:str):
#     return types.Content(
#         role='user',
#         parts=[
#             types.Part.from_function_response(
#                 name=name,
#                 response={"result":response}
#             )
#         ]
#     )

# def model_text_form(text:str):
#     return types.Content(
#         role='model',
#         parts=[types.Part.from_text(text=text)]
#     )

# USER_SESSIONS={}

# class ChatInput(BaseModel):
#     query:str
#     user_id:str
#     chat_id:str

# @app.post("/start_chat")
# async def start_chat(data:ChatInput):
#     response_payload={
#         "text":""
#     }
    
#     print(data,'data-------------------')
    
#     user_query=data.query
#     user_id=data.user_id
#     chat_id=data.chat_id
    
#     print(user_query,user_id,chat_id,'uuuuuuuuuuuuuuuu')
    
#     if user_id not in USER_SESSIONS:
#         USER_SESSIONS[user_id]={}
#         if chat_id not in USER_SESSIONS[user_id]:
#             USER_SESSIONS[user_id][chat_id]=[]
#             response_payload["text"]="Hi, how can i help you today?"
#             USER_SESSIONS[user_id][chat_id].append(text_form(str(user_query)))
#             USER_SESSIONS[user_id[chat_id]].append(model_text_form(str(response_payload["text"])))
#     elif user_id in USER_SESSIONS and chat_id not in USER_SESSIONS[user_id]:
#         USER_SESSIONS[user_id][chat_id]=[]
#         response_payload["text"]="Hi, how can i help you today?"
#         USER_SESSIONS[user_id][chat_id].append(text_form(str(user_query)))  
#         USER_SESSIONS[user_id][chat_id].append(model_text_form(str(response_payload["text"])))  

#     elif user_query in {"Hi","hi","Hello","hello"}:
#         response_payload["text"]="Hi, how can i help you today?"
#         USER_SESSIONS[user_id][chat_id].append(text_form(str(user_query)))  
#         USER_SESSIONS[user_id][chat_id].append(model_text_form(str(response_payload["text"])))  
#     else:
        
#         USER_SESSIONS[user_id][chat_id].append(text_form(str(user_query)))
        
#         response = await client.aio.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=USER_SESSIONS[user_id][chat_id],
#             config=types.GenerateContentConfig(
#                 system_instruction=instructions
#             )
#         )
        
#         parts = response.candidates[0].content.parts
        
#         function_calls=[]
        
#         text_output=""
        
#         USER_SESSIONS[user_id][chat_id].append(parts)
        
#         for part in parts:
#             if hasattr(part,"function_call") and part.function_call:
#                 function_calls.append(part.function_call)
                
#             if hasattr(part,"text") and part.text:
#                 text_output += part.text
        
#         if function_calls:
#             for call in function_calls:
#                 print("Function Call Detected:")
#                 print("Name:", call.name)
#                 print("Args:", call.args)
                
#         if text_output:
#             print("Bot: ",text_output)
#             response_payload["text"] += "\n" + text_output               
#     text = response_payload["text"].strip()
#     await insert_chat(
#         app=app,userid=user_id,chatid=chat_id,
#         user_chat=user_query,model_chat=text,
#         chat_summary=""
#     )
    
#     print(USER_SESSIONS,'USER_SESSIONS--------')
#     return {'generated_text':text}


# if __name__ == "main":
#     import uvicorn
#     uvicorn.run(app,host='0.0.0.0',port=8000)












