import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch 

load_dotenv()

# tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"));

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over the internet

#     Args:
#         query (str): The search query.

#     Returns:
#         str: The search results.
#     """
#     # Here you would implement the actual search logic, e.g., using an API.
#     print(f"Searching for: {query}")
#     response = tavily.search(query=query)
#     return response

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    thinking_budget=0,
    max_output_tokens=1024,
)

tools = [TavilySearch()]

agent = create_agent(
    model=llm,
    tools=tools,
)


def main() -> None:
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": HumanMessage(content="Iam looking for ai engineering jobs in the indian cities on linkedin and list their details")}
    )
    print(result)


if __name__ == "__main__":
    main()