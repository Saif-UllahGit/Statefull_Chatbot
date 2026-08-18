# 🤖 Stateful AI Chatbot

A stateful AI chatbot built with **Python, LangGraph, Google Gemini, Streamlit, and SQLite**.

Unlike a basic chatbot, this application can maintain conversation state and preserve chat history across sessions using **LangGraph checkpointing and SQLite**.

## 🚀 Features

- 💬 Context-aware conversations
- 🧠 Persistent conversation memory
- 🔄 Multiple conversation threads
- 💾 SQLite-based state persistence
- 🤖 Google Gemini LLM integration
- ⚡ LangGraph workflow
- 🎨 Interactive Streamlit UI
- 🔐 Environment variable support for API keys

## 🛠️ Tech Stack

- **Python**
- **LangGraph**
- **LangChain**
- **Google Gemini**
- **Streamlit**
- **SQLite**
- **python-dotenv**

## 🏗️ How It Works

The chatbot uses **LangGraph** to manage the conversation workflow.

The basic flow is:

User Message
↓
LangGraph
↓
Chatbot Node
↓
Google Gemini
↓
Response
↓
SQLite Checkpoint
↓
Conversation State Saved

The saved state allows the chatbot to continue conversations while maintaining previous context.

## ▶️ How to Run the Application

### 1. Create and activate the virtual environment

```bash
python -m venv venv
```

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API Key

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Make sure `.env` is included in `.gitignore` and never upload your API key to GitHub.

### 4. Run the Streamlit Frontend

The Streamlit interface is located in:

```text
streamlit_frontend_database.py
```

Run it using:

```bash
streamlit run streamlit_frontend_databasse.py
```

After running the command, Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your browser to interact with the chatbot.

### 📁 Main Project Files

```text
stateful-chatbot/
│
├── streamlit_frontend_database.py   # Streamlit user interface
├── langgraph_backend_database.py    # LangGraph chatbot backend
├── requirements.txt                 # Project dependencies
├── .env                             # API key (do not upload)
├── .gitignore
└── README.md
```


