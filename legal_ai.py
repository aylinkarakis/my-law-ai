import streamlit as st
from openai import OpenAI
import os

# Configure layout settings to hide default menus and lock full screen width
st.set_page_config(page_title="LexAI Portal", page_icon="⚖️", layout="wide", initial_sidebar_state="collapsed")

# ABSOLUTE FOOLPROOF ENTERPRISE DESIGN (Side Menu Hidden, Hard-Coded 2-Column Grid)
st.markdown("""
    <style>
        /* Force full layout background to uniform deep dark navy */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stBottom"] {
            background-color: #0A192F !important;
            color: #F8F9FA !important;
        }
        
        /* HARD-WIPE EVERY ACCIDENTAL TRACK OF THE BUILT-IN TEMPLATE HIDING CHANNELS */
        [data-testid="collapsedControl"], 
        [data-testid="stSidebar"],
        [data-testid="stSidebarCollapseButton"],
        header, .stApp > header {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            width: 0px !important;
            height: 0px !important;
        }
        
        /* Enforce elegant legal text styling globally */
        p, span, label, li, div {
            color: #CCD6F6 !important;
            font-family: 'Times New Roman', Times, serif !important;
        }
        
        /* --- HAND-BUILT HARD-CODED SIDE PANEL INNER CONTAINERS --- */
        .custom-sidebar {
            background-color: #0D1E36 !important;
            border: 1px solid #172A45;
            border-radius: 8px;
            padding: 20px;
            height: 85vh;
        }
        
        /* Premium Multi-Chat Folder Link Styling */
        .chat-folder {
            background-color: #172A45 !important;
            border-left: 3px solid #D4AF37 !important;
            padding: 12px !important;
            margin: 10px 0 !important;
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
            margin-top: 40px;
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
        
        /* Traditional legal block chat style (Clean borders, no icon overlap) */
        [data-testid="stChatMessage"] {
            background-color: #172A45 !important;
            border-left: 3px solid #D4AF37 !important;
            border-radius: 4px !important;
            padding: 15px 20px !important;
            margin: 10px 0 !important;
        }
        /* Strip default avatars from chat entries */
        [data-testid="stChatMessageAvatarContainer"] {
            display: none !important;
        }
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
    </style>
""", unsafe_allow_html=True)

# CREATE THE PERFECT MULTI-COLUMN WEB GRID USING NATIVE STREAMLIT LAYOUTS
col_menu, col_space, col_chat = st.columns([3.5, 0.5, 8.0])

# --- FIXED LEFT Enterprise MENU COLUMN ---
with col_menu:
    st.markdown("""
        <div class='custom-sidebar'>
            <h2 style='color:#D4AF37; font-family:serif; letter-spacing: 1px; margin-bottom:5px;'>LEXAI PORTAL</h2>
            <p style='color:#8892B0; font-size:12px; margin-top:0px;'>Enterprise Account Dashboard</p>
            <hr style='border-color: #172A45; margin: 15px 0;'>
            
            <h4 style='color:#D4AF37; font-family:serif; margin-bottom:10px; font-size:16px;'>YOUR SAVED CONCEPTS</h4>
            <div class='chat-folder'>💬 📑 NDA Analysis & Review<br><span style='font-size:11px; color:#8892B0;'>Last edited: Active</span></div>
            <div class='chat-folder' style='border-left-color:#8892B0; opacity:0.6;'>💬 📜 Trademark Registration</div>
            <div class='chat-folder' style='border-left-color:#8892B0; opacity:0.6;'>💬 💼 Employment Contract Parameters</div>
            <div class='chat-folder' style='border-left-color:#8892B0; opacity:0.6;'>💬 🏛️ Local Regulatory Codes</div>
            
            <hr style='border-color: #172A45; margin: 25px 0;'>
            <h4 style='color:#D4AF37; font-family:serif; font-size:15px;'>DOCUMENTATION AUDIT GUIDE</h4>
            <p style='font-size:13px; line-height:1.4;'>1. Input regulatory queries into active layer.<br>2. Cloud engine cross-references compliance parameters instantly.</p>
            
            <div class='user-profile'>
                <div class='profile-circle'>U</div>
                <div class='profile-email'>
                    <span style='font-weight:bold; display:block; font-size:11px; color:#D4AF37;'>Enterprise User</span>
                    user@companypolicy.com
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- FIXED RIGHT MAIN ASSISTANT CHAT COLUMN ---
with col_chat:
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
                
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": f"Answer as a formal legal assistant: {user_question}"}]
                )
                ai_reply = response.choices.message.content
            except Exception:
                ai_reply = "Authentication Failure: Could not establish a secure connection to the Cloud AI Engine. Please check your Secret API Key structure inside your Streamlit Secrets box."
            
            st.markdown(f"<span style='color:#D4AF37; font-weight:bold;'>System Response: </span>{ai_reply}", unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
