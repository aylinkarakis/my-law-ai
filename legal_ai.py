import streamlit as st
from openai import OpenAI
import os

# Configure layout settings to hide default menus and clean the screen
st.set_page_config(page_title="LexAI Portal", page_icon="⚖️", layout="wide")

# ULTRA-FORMAL ENTERPRISE CSS OVERRIDE (NO EMOJIS, TRADITIONAL FONT STYLING)
st.markdown("""
    <style>
        /* Force full layout to dark navy */
        .stApp, [data-testid="stAppViewContainer"] {
            background-color: #0A192F !important;
            color: #F8F9FA !important;
        }
        /* Style the sidebar container seamlessly */
        [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {
            background-color: #0D1E36 !important;
            border-right: 1px solid #172A45;
        }
        /* Enforce formal silver-white for body paragraphs and guides */
        p, span, label, li {
            color: #CCD6F6 !important;
            font-family: 'Times New Roman', Times, serif !important;
        }
        /* Strip default emojis/avatars from chat rows completely */
        [data-testid="stChatMessageAvatarContainer"] {
            display: none !important;
        }
        /* Traditional legal block chat style */
        [data-testid="stChatMessage"] {
            background-color: #172A45 !important;
            border-left: 3px solid #D4AF37 !important;
            border-radius: 4px !important;
            padding: 15px !important;
            margin: 10px 0 !important;
        }
        /* Custom Gold Typing text inside the formal input bar */
        [data-testid="stChatInput"] textarea {
            color: #D4AF37 !important;
            background-color: #172A45 !important;
            border: 1px solid #D4AF37 !important;
            font-family: 'Times New Roman', Times, serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR DESIGN (NO GENERIC ICONS) ---
with st.sidebar:
    st.markdown("<h2 style='color:#D4AF37; font-family:serif; letter-spacing: 1px;'>LEXAI SYSTEM</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00E676; font-size:12px; font-weight:bold;'>SECURE ENCRYPTED NODE ACTIVE</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h4 style='color:#D4AF37; font-family:serif;'>DOCUMENTATION AUDIT GUIDE</h4>", unsafe_allow_html=True)
    st.markdown("""
    1. Input precise regulatory or contractual queries below.
    2. System references enterprise cloud parameters instantly.
    3. All queries process through localized transport layers.
    """)

# --- MAIN CHAT SCREEN DESIGN (NO GRAPHICS, PURE CORPORATE GOLD) ---
st.markdown("<h1 style='color:#D4AF37; font-family:serif; font-size: 38px; letter-spacing: 1px; margin-bottom:0px;'>LEXAI CORPORATE ASSISTANT</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#CCD6F6; font-style:italic; font-size:14px; margin-top:0px;'>Secure Cloud-Powered Intelligence for Enterprise Legal Operations.</p>", unsafe_allow_html=True)
st.write("---")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages cleanly without avatars
for msg in st.session_state.messages:
    # Explicit text prefixes replace informal colorful icons
    prefix = "User Request: " if msg["role"] == "user" else "System Response: "
    with st.chat_message(msg["role"]):
        st.markdown(f"<span style='color:#D4AF37; font-weight:bold;'>{prefix}</span>{msg['content']}", unsafe_allow_html=True)

# Handle user input
if user_question := st.chat_input("Ask a legal question..."):
    st.chat_message("user").markdown(f"<span style='color:#D4AF37; font-weight:bold;'>User Request: </span>{user_question}", unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("assistant"):
        try:
            api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
            client = OpenAI(api_key=api_key)
            
            prompt_context = [
                {"role": "system", "content": "You are a professional legal assistant. Answer questions accurately and concisely using standard legal definitions. Make your tone hyper-professional, objective, and formal."},
                {"role": "user", "content": user_question}
            ]
            
            response = client.chat.completions.create(model="gpt-4o-mini", messages=prompt_context)
            ai_reply = response.choices.message.content
        except Exception:
            ai_reply = "Authentication Failure: Could not establish a secure connection to the Cloud AI Engine. Please check your Secret API Key structure."
        
        st.markdown(f"<span style='color:#D4AF37; font-weight:bold;'>System Response: </span>{ai_reply}", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
