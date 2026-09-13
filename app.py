import streamlit as st
import google.generativeai as genai

# API Key secrets.toml থেকে পড়বে
genai.configure(api_key=st.secrets["general"]["GEMINI_API_KEY"])

# Model name ও secrets.toml থেকে পড়বে
model_name = st.secrets["general"]["MODEL_NAME"]

# Model initialize
model = genai.GenerativeModel(model_name)

st.title("ANOI Assistant 🚀")

user_input = st.text_input("তোমার প্রশ্ন লিখো:")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
