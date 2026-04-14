# 🏠 AI Rent Agreement Explainer Bot

An AI-powered chatbot that explains rent agreement clauses in simple language and highlights potential risks using RASA and Gemini API.


## 🚀 Features

- 💬 Chat-based interface (Streamlit)
- 🧠 AI-powered clause explanation
- ⚠️ Risk detection (LOW / MEDIUM / HIGH)
- 🔄 Multi-turn conversation using RASA
- 📄 Document upload support (PDF / TXT)
- 🔐 Privacy-friendly (no data stored)


## 🧠 Tech Stack

- RASA (Conversation Management)
- Gemini API (LLM for explanation)
- Streamlit (Frontend UI)
- Python


## ⚙️ How It Works

1. User interacts via chat interface  
2. RASA detects user intent (greeting / clause / risk)  
3. For legal queries → custom action is triggered  
4. Gemini API processes the clause  
5. Response returned with:
   - Simple explanation  
   - Risk points  
   - Risk level
  

## ⚠️ Disclaimer

This bot provides AI-generated explanations for educational purposes only.  
It does not constitute legal advice.


## 🎯 Future Improvements

- Automatic clause detection from documents  
- Highlight risky terms  
- Deployment on cloud (Render / Railway)  
- User session history  
