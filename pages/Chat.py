import streamlit as st
import numpy as np
import google.generativeai as genai
import dotenv
dotenv.load_dotenv(".env")
GOOGLE_API_KEY="AIzaSyBJ51o9pit7RqRYCc2OiUb1k2tebHY8ktM"

genai.configure(api_key=GOOGLE_API_KEY)
model_list = []
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        model_list.append(m.name.split("/")[-1])
        
# Create title and logo
st.title("Experiance the new Gemini Chat bot")
# Create sidebar for settings
sidebar = st.sidebar
# Create a dropdown menu for selecting the model
model = sidebar.selectbox(
    "Select the language model",
    model_list
)
model
# Create a slider for adjusting the temperature
temperature = sidebar.slider(
    "Adjust the temperature",
    0.0, 1.0, 0.7, 0.01
)

assistant_message =  st.chat_message("GeminiBot",avatar="🤖")
assistant_message.write("Hello 👋")

# Display a chat input widget.
prompt = st.chat_input("Say something")
if prompt:
    human_prompt = {}