

from langchain_text_splitters import RecursiveCharacterTextSplitter
import pdfplumber
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


#---- Retrival Arugmented generation =RAG
pdf_path = r"Ai_with_Rag\6th_Social_Science_Term_I_EM - www.tntextbooks.in.pdf"

all_text = []

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages[:20], start=1):
        text = page.extract_text() or ""
        
        # all_text.append(f"\n--- Page {page_num} ---\n")
        all_text.append(text)

full_text = "\n".join(all_text)

# print(full_text[:500])




text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n\n","\n"," "]
)
text=text_splitter.split_text(full_text)
# print(text[:10])

# for i,char in enumerate(text):
#     if i ==5:
#         break
#     print(char)
#     print("-"*50)
# print(len(text))



def convert_embed(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    # print(result.embeddings[0].values[:10])
    return result.embeddings[0].values
    
chunk_embedding=[]

for txt in text:
    chunk_embedding.append(convert_embed(text=txt))
    






