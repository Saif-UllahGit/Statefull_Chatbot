from typing import TypedDict, Annotated
import os
import sqlite3

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# Load .env
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=api_key,
)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


# Checkpointer
conn = sqlite3.connect(
    "Database.dp",
    check_same_thread=False
)

checkpointer = SqliteSaver(conn=conn)


# Build graph
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)


# Compile graph
chatbot = graph.compile(checkpointer=checkpointer)


def retreive_all_thread():
    all_thread = set()

    for checkpoint in checkpointer.list(None):
        all_thread.add(
            checkpoint.config["configurable"]["thread_id"]
        )

    return list(all_thread)