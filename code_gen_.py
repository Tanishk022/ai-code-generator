from google import genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

prompt = input("enter your design for frontend: ")
filename=input("Enter file name for html file: ")


# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"write a code index.html file for the given prompt {prompt} give only the codes"
)

retext = response.text

with open(f"{filename}.html" ,'w') as file:
    file.write(retext)


