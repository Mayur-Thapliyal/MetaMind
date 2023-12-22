import streamlit as st 
from const import MODEL_OPTIONS
from streamlit_ws_localstorage import injectWebsocketCode, getOrCreateUID
from utils import get_local_storage_value,set_local_storage_value
# local_storage = injectWebsocketCode(hostPort='wsauthserver.supergroup.ai/', uid=getOrCreateUID())
def saveButtonHandler(key,value):
    set_local_storage_value(key,value)
def api_key_component(key_name):
    
    code_peace = (f"""
API_KEY = get_local_storage_value('{key_name}')
if API_KEY:
    MASKED_API_KEY = API_KEY[-4:].rjust(len(API_KEY), '*')
    API_KEY = st.text_input( "API KEY",
                                    placeholder=MASKED_API_KEY)
else:
    API_KEY = st.text_input( "API KEY")
    set_local_storage_value("{key_name}",API_KEY)
    """)
    exec(code_peace)
    
    

    
model_value = get_local_storage_value('SELECTED_MODEL')
if model_value:
    model_index=MODEL_OPTIONS.index(model_value)
    model = st.selectbox(
        label="Select the language model",
        options=MODEL_OPTIONS,
        placeholder="Choose your Model",
        index=model_index
    )
else:
    model = st.selectbox(
        label="Select the language model",
        options=["OpenAI", "Google Gemini", "Azure OpenAI", "GPT4All"],
        placeholder="Choose your Model",
    )
if model_value != model:
    set_local_storage_value('SELECTED_MODEL',model)
if model_value == 'OpenAI':
    api_key_component(key_name="OpenAI_API_KEY")
elif model_value  == "Google Gemini":
    api_key_component(key_name="Gemini_API_KEY")
elif model_value  == "":
    pass
elif model_value  == "":
    pass