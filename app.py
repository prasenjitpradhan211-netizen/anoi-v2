
import streamlit as st
import google.generativeai as genai

# 👉 এখানে তোমার Gemini API key বসাও
genai.configure(api_key="AQ.Ab8RN6KKZ4vbAU2JaDNS5tCF9Qkj2SCgCE8knswvIfbKnmu_dQ")

# Page config
st.set_page_config(
    page_title="ANOI Assistant",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("ANOI Settings ⚙️")
st.sidebar.info("🎯 লক্ষ্য: Madhyamik প্রস্তুতি\n\nএই অ্যাপ তোমাকে পড়াশোনা + প্রজেক্ট balance করতে সাহায্য করবে।")

# Main Title
st.title("ANOI Assistant 🚀")
st.markdown(
    "<h3 style='color:#2E86C1;'>Hello ভাই! আমি ANOI, তোমার AI সহকারী।</h3>",
    unsafe_allow_html=True
)

# Input
user_input = st.text_input("✍️ কিছু লিখো:")

# History memory
if "history" not in st.session_state:
    st.session_state["history"] = []

# Response
if user_input:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    st.success(f"ANOI বলছে: {response.text}")
    st.session_state["history"].append((user_input, response.text))

# Show history
if st.session_state["history"]:
    st.subheader("📜 History")
    for i, (q, a) in enumerate(st.session_state["history"], 1):
        st.markdown(f"<b>{i}. তুমি:</b> {q}", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#117A65;'>👉 ANOI:</span> {a}", unsafe_allow_html=True)
