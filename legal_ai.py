import streamlit as st
import requests
import os

# Configure layout settings to hide default menus and lock full screen width
st.set_page_config(page_title="LexAI Portal", page_icon="⚖️", layout="wide")

# FORCE THE NAVY, GOLD, AND HIGH-CONTRAST TYPING TEXT COLORS VIA CUSTOM CSS
st.markdown("""
    <style>
        /* Force full layout background to uniform deep dark navy */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stBottom"] {
            background-color: #0A192F !important;
            color: #F8F9FA !important;
        }
        
        /* HARD-WIPE THE DEFAULT TEMPLATE MENUS OUT OF EXISTENCE */
        [data-testid="collapsedControl"], 
        [data-testid="stSidebar"],
        [data-testid="stSidebarCollapseButton"],
        header, .stApp > header {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
        }
        
        /* Enforce elegant legal text styling globally */
        p, span, label, li, div, h1, h2, h3, h4 {
            font-family: 'Times New Roman', Times, serif !important;
        }
        
        /* Premium Multi-Chat Folder Link Styling */
        .chat-folder-box {
            background-color: #172A45;
            border-left: 3px solid #D4AF37;
            padding: 10px;
            margin: 8px 0;
            border-radius: 4px;
        }
        
        /* User Profile Avatar Section at Bottom of Sidebar */
        .user-profile-box {
            display: flex;
            align-items: center;
            padding: 12px;
            background-color: #112240;
            border-radius: 8px;
            border: 1px solid #172A45;
            margin-top: 40px;
        }
        
        /* --- ELIMINATE RE-EMERGING CHAT ROW ICON OVERLAPS --- */
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
        
        /* --- 100% READABLE HIGH-CONTRAST TYPING BAR OVERHAUL --- */
        [data-testid="stBottom"] {
            background-color: #0A192F !important;
            border-top: none !important;
        }
        [data-testid="stChatInput"] {
            background-color: #FFFFFF !important; /* Crisp white input container */
            border: 2px solid #CCD6F6 !important;
            border-radius: 8px !important;
        }
        [data-testid="stChatInput"] textarea {
            color: #0A192F !important; /* Deep black-navy text while typing! */
            background-color: transparent !important;
            font-size: 16px !important;
        }
        [data-testid="stChatInput"] button {
            background-color: #172A45 !important;
            color: #D4AF37 !important;
            border-radius: 4px !important;
        }
    </style>
""", unsafe_allow_html=True)

# CREATE THE WEB GRID USING NATIVE LAUNCH COLS
col_menu, col_space, col_chat = st.columns([3.5, 0.5, 8.0])

# --- FIXED LEFT ENTERPRISE MENU COLUMN ---
with col_menu:
    st.markdown("<h2 style='color:#D4AF37; margin-bottom:5px;'>LEXAI PORTAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8892B0; font-size:12px; margin-top:0px;'>Enterprise Account Dashboard</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #172A45;'>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='color:#D4AF37; font-size:16px;'>YOUR SAVED CONCEPTS</h4>", unsafe_allow_html=True)
    
    # Render native container cards cleanly
    st.markdown("<div class='chat-folder-box'><span style='color:#CCD6F6;'>💬 📑 NDA Analysis & Review</span><br><span style='font-size:11px; color:#8892B0;'>Last edited: Active</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-folder-box' style='border-left-color:#8892B0; opacity:0.6;'><span style='color:#8892B0;'>💬 📜 Trademark Registration</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-folder-box' style='border-left-color:#8892B0; opacity:0.6;'><span style='color:#8892B0;'>💬 💼 Employment Parameters</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-folder-box' style='border-left-color:#8892B0; opacity:0.6;'><span style='color:#8892B0;'>💬 🏛️ Local Regulatory Codes</span></div>", unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: #172A45; margin-top:30px;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#D4AF37; font-size:15px;'>DOCUMENTATION AUDIT GUIDE</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:13px; color:#CCD6F6;'>1. Input queries into active layout layer.<br>2. Local AI engine cross-references parameters instantly.</p>", unsafe_allow_html=True)
    
    # Account panel footer details
    st.markdown("""
        <div class='user-profile-box'>
            <div style='width:35px; height:35px; background-color:#D4AF37; color:#0A192F; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; margin-right:12px;'>U</div>
            <div>
                <span style='font-weight:bold; display:block; font-size:11px; color:#D4AF37;'>Enterprise User</span>
                <span style='color:#F8F9FA; font-size:13px;'>user@companypolicy.com</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- FIXED RIGHT MAIN ASSISTANT CHAT COLUMN ---
with col_chat:
    st.markdown("<h1 style='color:#CCD6F6; font-size: 38px; letter-spacing: 1px; margin-bottom:0px;'>LEXAI CORPORATE ASSISTANT</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#D4AF37; font-style:italic; font-size:15px; margin-top:5px;'>Your privacy is our corporate responsibility.</p>", unsafe_allow_html=True)

    # Compliance Footer Links Section
    st.markdown("""
        <p style='font-size:13px; margin-top:5px; margin-bottom:15px;'>
            <a href='#' style='color:#D4AF37; text-decoration:none; font-weight:bold;'>Privacy Policy</a> &nbsp;|&nbsp; 
            <a href='#' style='color:#D4AF37; text-decoration:none; font-weight:bold;'>Terms of Service</a> &nbsp;|&nbsp; 
            <a href='#' style='color:#D4AF37; text-decoration:none; font-weight:bold;'>Compliance Parameters</a>
        </p>
    """, unsafe_allow_html=True)

    st.write("---")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display past messages cleanly
    for msg in st.session_state.messages:
        prefix = "User Request: " if msg["role"] == "user" else "System Response: "
        with st.chat_message(msg["role"]):
            st.markdown(f"<span style='color:#D4AF37; font-weight:bold;'>{prefix}</span><span style='color:#F8F9FA;'>{msg['content']}</span>", unsafe_allow_html=True)

    # Handle user input using the FREE local Llama engine
    if user_question := st.chat_input("Ask a legal question..."):
        st.chat_message("user").markdown(f"<span style='color:#D4AF37; font-weight:bold;'>User Request: </span><span style='color:#F8F9FA;'>{user_question}</span>", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": user_question})

        with st.chat_message("assistant"):
            with st.spinner("Processing locally on secure enterprise layer..."):
                try:
                    response = requests.post(
                        "http://localhost:11434/api/generate",
                        json={
                            "model": "llama3.2:1b",
                            "prompt": f"Answer as a formal legal assistant: {user_question}",
                            "stream": False
                        }
                    )
                    ai_reply = response.json().get("response", "Error reading response.")
                except Exception:
                    ai_reply = "Could not connect to Ollama. Please make sure the Ollama application (the little llama icon in your top menu bar) is active and running!"
                
                st.markdown(f"<span style='color:#D4AF37; font-weight:bold;'>System Response: </span><span style='color:#F8F9FA;'>{ai_reply}</span>", unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})
