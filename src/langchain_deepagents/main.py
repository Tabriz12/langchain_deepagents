from typing import Literal

from deepagents import create_deep_agent

# from langchain.chat_models import init_chat_model
# from langgraph.types import Command
from tavily import TavilyClient

from config import settings

tavily_client = TavilyClient(api_key=settings.tavily_api_key)


# print(sys.path)


def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )


# System prompt to steer the agent to be an expert researcher
research_instructions = """
You are an expert researcher. Your job is to conduct 
thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering 
information.

## `internet_search`

Use this to run an internet search for a given query. 
You can specify the max number of results to return, the topic, 
and whether raw content should be included.
"""

agent = create_deep_agent(tools=[internet_search], system_prompt=research_instructions)


result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

print(result["messages"][-1].content)
