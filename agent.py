import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from langchain.tools import Tool

from tools.pdf_tool import pdf_search
from tools.web_tool import web_search
from tools.text_tool import text_search

# Load environment variables
load_dotenv()

# Initialize LLM (Groq)
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# Define tools
tools = [
    Tool(
        name="PDF Search",
        func=pdf_search,
        description="Use this tool to answer questions from PDF documents"
    ),
    Tool(
        name="Web Search",
        func=web_search,
        description="Use this tool for latest or real-time information from the internet"
    ),
    Tool(
        name="Text Search",
        func=text_search,
        description="Use this tool to answer questions from local text notes"
    )
]

# Initialize agent (no AgentType needed)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    verbose=True,
    handle_parsing_errors=True
)

# Function to run agent
def run_agent(query):
    try:
        response = agent.run(query)
        return response
    except Exception as e:
        return f"Error: {str(e)}"