import streamlit as st
import requests

st.caption("⚠️ This bot explains legal clauses. Not legal advice.")

import PyPDF2

uploaded_file = st.file_uploader("📄 Upload Rent Agreement", type=["pdf", "txt"])

if uploaded_file:
    text = ""

    if uploaded_file.type == "application/pdf":
        pdf = PyPDF2.PdfReader(uploaded_file)
        for page in pdf.pages:
            text += page.extract_text()
    else:
        text = uploaded_file.read().decode("utf-8")

    st.success("✅ File uploaded successfully")

    # Auto-send to chat (optional)
    if st.button("Analyze Document"):
        st.session_state.messages.append({"role": "user", "content": text})
        
st.set_page_config(page_title="Rent Agreement Bot", layout="centered")

st.title("🏠 Rent Agreement Explainer Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to RASA
    payload = {
        "sender": "user",
        "message": user_input
    }

    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json=payload
    )

    bot_response = response.json()

    bot_text = ""
    for msg in bot_response:
        if "text" in msg:
            bot_text += msg["text"] + "\n"

    # Show bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_text})

    with st.chat_message("assistant"):
        st.markdown(bot_text)