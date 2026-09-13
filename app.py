import streamlit as st
import openai

# ✅ Secrets থেকে API key নেবে
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("ANOI Assistant 🚀")
user_input = st.text_input("✍ কিছু লিখো:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":user_input}]
    )
    st.success(f"ANOI বলছে: {response.choices[0].message['content']}")
