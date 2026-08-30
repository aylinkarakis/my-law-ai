import streamlit as st
from openai import OpenAI
import os

# Configure layout settings to hide default menus and clean the screen
st.set_page_config(page_title="LexAI Portal", page_icon="⚖️", layout="wide")

# ADVANCED ENTERPRISE ARCHITECTURE (TOTAL STRING DELETION & SEAMLESS OVERRIDES)
st.markdown("""
    <style>
        /* Force full layout background to uniform deep dark navy */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stBottom"] {
            background-color: #0A192F !important;
            color: #F8F9FA !important;
        }
        /* Style the sidebar container seamlessly */
        [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {
            background-color: #0D1E36 !important;
            border-right: 1px solid #172A45;
        }
        
        /* --- HARD-WIPE EVERY ACCIDENTAL HEADER STRING OUT OF EXISTENCE --- */
        [data-testid="collapsedControl"], 
        span[data-testid="stHeaderActionElements"],
        header, .stApp > header {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            font-size: 0px !important;
            color: transparent !important;
            width: 0px !important;
            height: 0px !important;
        }
        
        /* --- BRAND NEW HAND-BUILT THREE-LINE MENU ICON (ISOLATED RULES) --- */
        [data-testid="stSidebarCollapseButton"] button {
            background-color: #172A45 !important;
            border: 1px solid #D4AF37 !important;
            border-radius: 4px !important;
            padding: 5px !important;
            margin-left: 10px !important;
            margin-top: 10px !important;
            min-height: 40px !important;
            min-width: 45px !important;
            position: relative !important;
        }
        /* Force the stubborn default internal labels to completely hide */
        [data-testid="stSidebarCollapseButton"] button * {
            font-size: 0px !important;
            color: transparent !important;
            display: none !important;
            opacity: 0 !important;
        }
        /* Pure independent vector text injection for the 3 lines */
        [data-testid="stSidebarCollapseButton"] button::before {
            content: "☰" !important; 
            color: #D4AF37 !important;
            font-size: 22px !important;
            font-weight: bold !important;
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            opacity: 1 !important;
            visibility: visible !important;
        }
        
        /* Enforce elegant legal text styling globally */
        p, span, label, li {
            color: #CCD6F6 !important;
            font-family: 'Times New Roman', Times, serif !important;
        }
        /* Strip avatars from chat entries */
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
        
        /* --- PROMINENT ICE-BLUE TYPING BAR OVERHAUL --- */
        [data-testid="stBottom"] {
            background-color: #0A192F !important;
            border-top: none !important;
        }
        [data-testid="stChatInput"] {
            background-color: #172A45 !important;
            border: 2px solid #CCD6F6 !important;
            border-radius: 8px !important;
        }
        [data-testid="stChatInput"] textarea {
            color: #CCD6F6 !important;
            background-color: transparent !important;
            font-family: 'Times New Roman', Times, serif !important;
            font-size: 16px !important;
        }
        [data-testid="stChatInput"] button {
            background-color: #CCD6F6 !important;
            color: #0A192F !important;
            border-radius: 4px !important;
        }
        
        /* Stylized legal footer links text */
        .legal-links a {
            color: #D4AF37 !important;
            text-decoration: none !important;
            font-weight: bold;
            font-size: 13px;
        }
        .legal-links a:hover {
            text-decoration: underline !important;
        }
        
        /* Historical Shortcut Link Styling */
        .history-link {
            background-color: #172A45 !important;
            border-left: 2px solid #CCD6F6 !important;
            padding: 8px !important;
            margin: 5px 0 !important;
            border-radius: 2px !important;
            font-size: 13px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history early so sidebar can read it
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- SIDEBAR DESIGN (AUTOMATED CHAT HISTORY BOXES) ---
with st.sidebar:
    st.markdown("<h2 style='color:#D4AF37; font-family:serif; letter-spacing: 1px;'>LEXAI SYSTEM</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00E676; font-size:12px; font-weight:bold;'>SECURE ENCRYPTED NODE ACTIVE</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h4 style='color:#D4AF37; font-family:serif;'>ACTIVE CHAT SESSION LOGS</h4>", unsafe_allow_html=True)
    user_queries = [msg["content"] for msg in st.session_state.messages if msg["role"] == "user"]
    
    if user_queries:
        for idx, query in enumerate(user_queries, 1):
            short_query = query[:25] + "..." if len(query) > 25 else query
            st.markdown(f"<div class='history-link'>📁 Session Request {idx}:<br><span style='color:#FFF; font-style:italic;'>\"{short_query}\"</span></div>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#8892B0; font-size:13px; font-style:italic;'>No active queries in current transport terminal layer.</p>", unsafe_allow_html=True)
        
    st.write("---")
    st.markdown("<h4 style='color:#D4AF37; font-family:serif;'>DOCUMENTATION AUDIT GUIDE</h4>", unsafe_allow_html=True)
    st.markdown("""
    1. Input precise regulatory or contractual queries below.
    2. System references enterprise cloud parameters instantly.
    3. All queries process through localized transport layers.
    """)

# --- MAIN CHAT SCREEN DESIGN ---
st.markdown("<h1 style='color:#CCD6F6; font-family:serif; font-size: 38px; letter-spacing: 1px; margin-bottom:0px;'>LEXAI CORPORATE ASSISTANT</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#D4AF37; font-style:italic; font-size:15px; margin-top:5px; font-family:serif; letter-spacing: 0.5px;'>Your privacy is our corporate responsibility.</p>", unsafe_allow_html=True)

# Professional Compliance Footer Links Section
st.markdown("""
    <div class='legal-links' style='font-family:serif; margin-top:5px; margin-bottom:15px;'>
        <a href='#'>Privacy Policy</a> &nbsp;|&nbsp; 
        <a href='#'>Terms of Service</a> &nbsp;|&nbsp; 
        <a href='#'>Compliance & Vault Parameters</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# Display past messages cleanly without avatars
for msg in st.session_state.messages:
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
