import streamlit as st
from openai import OpenAI
import os

# Configure layout settings
st.set_page_config(page_title="LexAI Assistant", page_icon="⚖️", layout="wide")

# FORCE THE NAVY, GOLD, AND CRISP WHITE TEXT COLORS VIA CUSTOM CSS
st.markdown("""
    <style>
        /* Force main page background and main text color to white */
        .stApp {
            background-color: #0A192F !important;
            color: #F8F9FA !important;
        }
        /* Style the sidebar container */
        [data-testid="stSidebar"] {
            background-color: #172A45 !important;
        }
        /* Force all sidebar text and subheaders to light silver/white */
        [data-testid="stSidebar"] *, .stMarkdown, p, span, label {
            color: #F8F9FA !important;
        }
        
        /* --- YOUR CUSTOM GOLD TYPING TEXT FIX --- */
        [data-testid="stChatInput"] textarea {
            color: #D4AF37 !important; /* Gold text while typing! */
            background-color: #172A45 !important; /* Deep navy input box */
        }
        
        /* Style headings to Gold */
        h1, h2, h3, .stButton>button {
            color: #D4AF37 !important;
        }
        /* Make chat bubbles navy with white text so they pop */
        [data-testid="stChatMessage"] {
            background-color: #172A45 !important;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            color: #F8F9FA !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR DESIGN ---
with st.sidebar:
    st.image("https://icons8.com", width=80)
    st.markdown("<h2 style='color:#D4AF37;'>LexAI Portal</h2>", unsafe_allow_html=True)
    st.write("---")
    st.subheader("🌐 System Status")
    st.success("🟢 Cloud AI Core Active")
    st.write("---")
    st.subheader("💡 User Guide")
    st.markdown("""
    1. Ask the AI to analyze specific rules or clauses.
    2. The AI uses enterprise cloud security to process your queries.
    """)

# --- MAIN CHAT SCREEN DESIGN ---
st.markdown("<h1 style='color:#D4AF37;'>⚖️ LexAI Corporate Assistant</h1>", unsafe_allow_html=True)
st.write("Secure, cloud-powered legal document intelligence for your enterprise.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if user_question := st.chat_input("Ask a legal question..."):
    st.chat_message("user").markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("assistant"):
        with st.spinner("Querying legal database..."):
            try:
                # Read the secret key we saved in the Streamlit vault
                api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
                client = OpenAI(api_key=api_key)
                
                prompt_context = [
                    {"role": "system", "content": "You are a professional legal assistant. Answer questions accurately and concisely using standard legal definitions. Make sure all your response text layout formats cleanly."},
                    {"role": "user", "content": user_question}
                ]
                
                response = client.chat.completions.create(model="gpt-4o-mini", messages=prompt_context)
                ai_reply = response.choices.message.content
            except Exception as e:
                ai_reply = "Could not connect to the cloud AI brain. Please double-check your API key inside the Streamlit Secrets vault!"
            
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
