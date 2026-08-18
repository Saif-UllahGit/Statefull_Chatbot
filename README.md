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

## 📂 Project Structure

```text
stateful-chatbot/
│
├── streamlit_frontend_databasse.py
├── langgraph_backend_databasse.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── chatbot.db
Run: streamlit run streamlit_frontend_databasse.py

