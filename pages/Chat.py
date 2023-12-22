import streamlit as st
import numpy as np
import google.generativeai as genai
import os 
from utils import get_local_storage_value,set_local_storage_value
from streamlit_ws_localstorage import injectWebsocketCode, getOrCreateUID

# local_storage = injectWebsocketCode(hostPort='wsauthserver.supergroup.ai', uid=getOrCreateUID())
LLM_model = get_local_storage_value("SELECTED_MODEL")

if not LLM_model:
    assistant_message =  st.chat_message("GeminiBot",avatar="🤖")
    assistant_message.write("<p style='font-weight: bold; font-size:23px'>Hi.👋Please configure Model through settings </p>",unsafe_allow_html=True)
else:
    GOOGLE_API_KEY = get_local_storage_value("Gemini_API_KEY")
    if not GOOGLE_API_KEY:
        assistant_message =  st.chat_message("GeminiBot",avatar="🤖")
        
        assistant_message.write("<p style='font-weight: bold; font-size:23px'>Hi.👋Please configure API KEY through settings </p>",unsafe_allow_html=True)
    else:
        if "messages" not in st.session_state:
            st.session_state["messages"]= [{"role": "assistant", "content": "Hello 👋"}]
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
        
        # Create a slider for adjusting the temperature
        temperature = sidebar.slider(
            "Adjust the temperature",
            0.0, 1.0, 0.7, 0.01
        )
        def get_gpt_response(user_prompt=""):
            gpt_model_instance = genai.GenerativeModel(model)
            response = gpt_model_instance.generate_content(user_prompt)
            return response.text

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Display a chat input widget.
        if user_prompt := st.chat_input("Say something"):
        
            with st.chat_message("user"):
                st.markdown(user_prompt)
                st.session_state.messages.append({"role":"user", "content" :user_prompt})
                    
            response = get_gpt_response(user_prompt)
            # Display assistant response in chat message container
            if response:
                with st.chat_message("assistant"):
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
            
    