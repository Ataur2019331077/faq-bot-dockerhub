from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os

# Load environment variables from .env file 
load_dotenv()



with open("faq.txt", "r") as f:
    # Read the contents of the file
    faq = f.read()


def make_prompt(user_input: str):
    # Create a prompt for the LLM
    return f"""
    You are a helpful assistant. Answer the user's question based on the following FAQ text:

    {faq}

    User: {user_input}
    Assistant:
    """
    


class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

import os
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_KEY")

llm = init_chat_model("google_genai:gemini-2.0-flash")

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")

graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    user_input = make_prompt(user_input)
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            #print("Assistant:", value["messages"][-1].content)
            return value["messages"][-1].content


# while True:
#     try:
#         user_input = input("User: ")
#         if user_input.lower() in ["quit", "exit", "q"]:
#             print("Goodbye!")
#             break
#         prompt = make_prompt(user_input)

#         stream_graph_updates(prompt)
#     except:
#         break

