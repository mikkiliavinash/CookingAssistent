from tavily import TavilyClient
from langchain.tools import tool
from typing import Dict, Any

tavily_client = TavilyClient()
@tool
def web_serch(query : str) ->Dict[str, Any]:
    """Search the Web for current Flues and Harmful food and more information"""
    return tavily_client.search(query)
