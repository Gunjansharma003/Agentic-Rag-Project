import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

def web_search(query):
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY not found in .env file")

    client = TavilyClient(api_key=api_key)

    response = client.search(query=query, max_results=3)

    results = []

    for result in response["results"]:
        results.append(result["content"])

    return results