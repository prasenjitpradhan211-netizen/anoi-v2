import streamlit as st

# Title & description
st.title("ANOI Assistant 🤖")
st.write("Hello ভাই! আমি ANOI, তোমার AI সহকারী।")

# User input
user_input = st.text_input("তুমি কিছু লিখো:")

# Simple demo response
if user_input:
    st.success(f"ANOI বলছে: {user_input[::-1]}")  # demo হিসেবে উল্টে দেখাচ্ছে
