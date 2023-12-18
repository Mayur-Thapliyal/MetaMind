import streamlit as st 
from dotenv import set_key,get_key
GOOGLE_API_KEY = get_key('.env','GOOGLE_API_KEY')

if GOOGLE_API_KEY:
    MASKED_GOOGLE_API_KEY = GOOGLE_API_KEY[-4:].rjust(len(GOOGLE_API_KEY), '*')
    GOOGLE_API_KEY = st.text_input( "GOOGLE API KEY",
                                    placeholder=MASKED_GOOGLE_API_KEY,)
else:
    GOOGLE_API_KEY = st.text_input( "GOOGLE API KEY")

if GOOGLE_API_KEY:
    set_key(".env",'GOOGLE_API_KEY',GOOGLE_API_KEY)
    "Changes Saved"