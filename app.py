import streamlit as st
import openai

# ✅ API key বসাও (Secrets এ রাখা সবচেয়ে safe)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ✅ App Title
st.title("ANOI Assistant 🚀")
st.write("Hello ভাই! আমি ANOI, তোমার AI সহকারী।")

# ✅ User Input
user_input = st.text_input("✍ কিছু লিখো:")

# ✅ Response Section
if user_input:
    try:
        # OpenAI ChatCompletion ব্যবহার
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",   # চাইলে "gpt-4" ব্যবহার করতে পারো
            messages=[
                {"role": "system", "content": "You are ANOI, a bilingual Bengali-English assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(f"ANOI বলছে: {response.choices[0].message['content']}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
