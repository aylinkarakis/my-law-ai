import streamlit as st
from openai import OpenAI
import os

# Configure layout settings to hide default menus and clean the screen
st.set_page_config(page_title="LexAI Portal", page_icon="⚖️", layout="wide")

# ADVANCED ENTERPRISE ARCHITECTURE (FIXED OVERLAPS, RE-ENABLED 3-LINES & SIDEBAR)
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
        
        /* --- PROMINENT THREE-LINE HAMBURGER MENU OVERRIDE (FIXED AND STABLE) --- */
        [data-testid="stApp"] header {
            background-color: transparent !important;
        }
        /* Clean up and style the sidebar collapse button area */
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
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-size: 0px !important;
        }
        /* Inject the elegant gold 3-line symbol safely */
        [data-testid="stSidebarCollapseButton"] button::before {
            content: "☰" !important; 
            color: #D4AF37 !important;
            font-size: 22px !important;
            font-weight: bold !important;
            display: block !important;
            position: absolute !important;
            visibility: visible !important;
            opacity: 1 !important;
        }
        /* Ensure all random default text labels inside that button stay hidden */
        [data-testid="stSidebarCollapseButton"] button * {
            display: none !important;
            font-size: 0px !important;
            opacity: 0 !important;
        }
        
        /* --- ELIMINATE CHAT ROW ICON OVERLAPS COMPLETELY --- */
        [data-testid="stChatMessageAvatarContainer"], 
        .stChatMessageIcon, 
        [data-testid="stChatMessage"] svg,
        [data-testid="stChatMessage"] img {
            display: none !important;
            visibility: hidden !important;
            width: 0px !important;
            height: 0px !important;
            opacity: 0 !important;
        }
        
        /* Enforce elegant legal text styling globally */
        p, span, label, li, div {
            color: #CCD6F6 !important;
            font-family: 'Times New Roman', Times, serif !important;
        }
        
        /* Traditional legal block chat style (Clean borders, no icon overlap) */
        [data-testid="stChatMessage"] {
            background-color: #172A45 !important;
            border-left: 3px solid #D4AF37 !important;
            border-radius: 4px !important;
            padding: 15px 20px !important;
            margin: 10px 0 !important;
        }
        /* Fix the interior text padding inside chat rows */
        [data-testid="stChatMessageContent"] {
            margin-left: 0px !important;
            padding-left: 0px !important;
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
        
        /* Premium Multi-Chat Folder Link Styling */
        .chat-folder {
            background-color: #172A45 !important;
            border-left: 3px solid #D4AF37 !important;
            padding: 10px !important;
            margin: 8px 0 !important;
            border-radius: 4px !important;
            font-size: 14px !important;
        }
        
        /* User Profile Avatar Section at Bottom of Sidebar */
        .user-profile {
            display: flex;
            align-items: center;
            padding: 12px;
            background-color: #112240;
            border-radius: 8px;
            border: 1px solid #172A45;
            margin-top: 20px;
        }
        .profile-circle {
            width: 35px;
            height: 35px;
            background-color: #D4AF37;
            color: #0A192F;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-family: serif;
            margin-right: 12px;
            font-size: 16px;
        }
        .profile-email {
            font-size: 13px !important;
            color: #F8F9FA !important;
        }
    </style>
""", unsafe_allow_html=True)

# Set up visual multi-chat session simulation variables
if "active_chat" not in st.session_state:
    st.session_state.active_chat = "NDA Analysis"

# --- SIDEBAR ACCOUNT & MULTI-CHAT DESIGN ---
with st.sidebar:
    st.markdown("<h2 style='color:#D4AF37; font-family:serif; letter-spacing: 1px; margin-bottom:5px;'>LEXAI PORTAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8892B0; font-size:12px; margin-top:0px;'>Enterprise Account Dashboard</p>", unsafe_allow_html=True)
    st.write("---")
    
    # 1. NEW CHAT BUTTON MOCKUP
    st.button("➕ CREATE NEW CONCEIVED WORKSPACE")
    
    st.write("---")
    st.markdown("<h4 style='color:#D4AF37; font-family:serif; margin-bottom:10px;'>YOUR SAVED CONCEPTS</h4>", unsafe_allow_html=True)
    
    # 2. SEPARATE CHAT CONCEPTS SELECTION FOLDERS
    st.markdown("<div class='chat-folder'>💬 📑 NDA Analysis & Review<br><span style='font-size:11px; color:#8892B0;'>Last edited: Active</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-folder' style='border-left-color:#8892B0; opacity:0.6;'>💬 📜 Trademark Registration</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-folder' style='border-left-color:#8892B0; opacity:0.6;'>💬 💼 Employment Contract Parameters</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-folder' style='border-left-color:#8892B0; opacity:0.6;'>💬 🏛️ Local Regulatory Codes</div>", unsafe_allow_html=True)
    
    st.write("---")
    
    # 3. USER PROFILE EMAIL BLOCK WITH PROFILE CIRCLE
    st.markdown("""
        <div class='user-profile'>
            <div class='profile-circle'>U</div>
            <div class='profile-email'>
                <span style='font-weight:bold; display:block; font-size:11px; color:#D4AF37;'>Enterprise User</span>
                user@companypolicy.com
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN CHAT SCREEN DESIGN ---
st.markdown("<h1 style='color:#CCD6F6; font-family:serif; font-size: 38px; letter-spacing: 1px; margin-bottom:0px;'>LEXAI CORPORATE ASSISTANT</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#D4AF37; font-style:italic; font-size:15px; margin-top:5px; font-family:serif;'>Your privacy is our corporate responsibility.</p>", unsafe_allow_html=True)

# Professional Compliance Footer Links Section
st.markdown("""
    <div class='legal-links' style='font-family:serif; margin-top:5px; margin-bottom:15px;'>
        <a href='#'>Privacy Policy</a> &nbsp;|&nbsp; 
        <a href='#'>Terms of Service</a> &nbsp;|&nbsp; 
        <a href='#'>Compliance & Vault Parameters</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages cleanly without avatars or icon labels
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
            # Read the secret key saved in the Streamlit vault
            api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
            client = OpenAI(api_key=api_key)
            
            prompt_context = [
