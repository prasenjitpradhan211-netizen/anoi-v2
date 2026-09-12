import streamlit as st
import google.generativeai as genai

# ✅ Gemini API key নিরাপদে Streamlit Secrets থেকে নাও
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ✅ Page setup
st.set_page_config(
    page_title="ANOI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ Sidebar
st.sidebar.title("⚙️ ANOI Settings")
st.sidebar.info("🎯 লক্ষ্য: Madhyamik প্রস্তুতি\n\nএই অ্যাপ তোমাকে পড়াশোনা + প্রজেক্ট balance করতে সাহায্য করবে।")

# ✅ Main Title
st.markdown("<h1 style='color:#2E86C1;'>ANOI Assistant 🚀</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#117A65;'>Hello ভাই! আমি ANOI, তোমার AI সহকারী।</h3>", unsafe_allow_html=True)

# ✅ Input box
user_input = st.text_input("✍️ কিছু লিখো:")

# ✅ History memory
if "history" not in st.session_state:
    st.session_state["history"] = []

# ✅ Response section
if user_input:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        st.success(f"ANOI বলছে: {response.text}")
        st.session_state["history"].append((user_input, response.text))
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# ✅ Show history
if st.session_state["history"]:
    st.subheader("📜 History")
    for i, (q, a) in enumerate(st.session_state["history"], 1):
        st.markdown(f"<b>{i}. তুমি:</b> {q}", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#117A65;'>👉 ANOI:</span> {a}", unsafe_allow_html=True)
