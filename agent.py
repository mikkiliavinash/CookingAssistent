from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from tools import web_serch
from prompts import SystemPrompt

modelgpt = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    max_tokens=200
)

Shot_term_memory = InMemorySaver()

cooking_agent = create_agent(
    model=modelgpt,
    system_prompt=SystemPrompt,
    tools=[web_serch],
    checkpointer=Shot_term_memory
)