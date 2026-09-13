import streamlit as st
from openai import OpenAI

# ✅ Client configure করো (Secrets থেকে API key নেবে)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ✅ Title
st.title("ANOI Assistant 🚀")
st.write("হ্যালো ভাই, আমি ANOI, তোমার AI সহকারী।")

# ✅ Input box
user_input = st.text_input("✍ কিছু লিখো:")

# ✅ Response section
if user_input:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",   # চাইলে "gpt-4" ব্যবহার করতে পারো
            messages=[
                {"role": "system", "content": "You are ANOI, a bilingual Bengali-English assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(f"ANOI বলছে: {response.choices[0].message.content}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
