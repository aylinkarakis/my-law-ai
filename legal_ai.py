import streamlit as st
import requests
import os

# Configure layout settings
st.set_page_config(page_title="LexAI Assistant", page_icon="⚖️", layout="wide")

# FORCE THE NAVY AND GOLD COLORS VIA VISUAL DESIGN BLOCKS
st.markdown("""
    <style>
        /* Force background colors */
        .stApp {
            background-color: #0A192F !important;
            color: #F8F9FA !important;
        }
        /* Style the sidebar container */
        [data-testid="stSidebar"] {
            background-color: #172A45 !important;
            color: #F8F9FA !important;
        }
        /* Style text color inside sidebar labels */
        [data-testid="stSidebar"] *, .stCaption {
            color: #CCD6F6 !important;
        }
        /* Style headings and buttons to Gold */
        h1, h2, h3, .stButton>button {
            color: #D4AF37 !important;
        }
        /* Make chat bubbles easily readable */
        [data-testid="stChatMessage"] {
            background-color: #172A45 !important;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Define folder path
folder_path = os.path.expanduser("~/Desktop/legal_documents")

# --- SIDEBAR DESIGN ---
with st.sidebar:
    st.image("https://icons8.com", width=80)
    st.markdown("<h2 style='color:#D4AF37;'>LexAI Portal</h2>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h3 style='color:#D4AF37;'>🌐 System Status</h3>", unsafe_allow_html=True)
    st.success("🟢 AI Core Active (Llama)")
    
    st.markdown("<h3 style='color:#D4AF37;'>📁 Loaded Knowledge Base</h3>", unsafe_allow_html=True)
    
    # List text files visually in the sidebar
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        if files:
            for file in files:
                st.caption(f"📄 {file}")
        else:
            st.caption("No .txt files found in folder.")
    else:
        st.caption("Folder not found.")
        
    st.write("---")
    st.markdown("<h3 style='color:#D4AF37;'>💡 User Guide</h3>", unsafe_allow_html=True)
    st.markdown("""
    1. Drop plain text rules (.txt) into your `legal_documents` folder.
    2. Ask the AI to analyze specific rules or clauses.
    3. The AI scans documents locally to ensure complete privacy.
    """)

# --- MAIN CHAT SCREEN DESIGN ---
st.markdown("<h1 style='color:#D4AF37;'>⚖️ LexAI Corporate Assistant</h1>", unsafe_allow_html=True)
st.write("Secure, offline legal document intelligence for your enterprise.")

# Function to read text from files
def load_legal_knowledge():
    if not os.path.exists(folder_path):
        return ""
    combined_text = ""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                combined_text += f.read() + "\n"
    return combined_text

knowledge_base = load_legal_knowledge()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if user_question := st.chat_input("Ask a question about your documents..."):
    st.chat_message("user").markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("assistant"):
        with st.spinner("Analyzing corporate documentation..."):
            try:
                full_prompt = f"""
                You are a professional legal assistant. 
                Use the following document text to answer the question accurately. 
                If the answer cannot be found in the text, rely on your general legal knowledge but mention that it wasn't in the provided documents.
                
                DOCUMENT TEXT:
                {knowledge_base[:4000]}
                
                QUESTION:
                {user_question}
                """
                
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama3.2:1b",
                        "prompt": full_prompt,
                        "stream": False
                    }
                )
                ai_reply = response.json().get("response", "Error reading response.")
            except Exception:
                ai_reply = "Could not connect to Ollama. Make sure the Ollama app is open and running!"
            
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
