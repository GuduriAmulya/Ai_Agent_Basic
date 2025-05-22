#setup groq and tabily api key
import os
from dotenv import load_dotenv
load_dotenv()
# os.load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
#setup llm tool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)# search from google


# setup ai agent
#use langgraph
from langgraph.prebuilt import create_react_agent  #first reason then act
from langchain_core.messages.ai import AIMessage
# system_prompt="Act like an AI chatbot who is smart and cool"
def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)
    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm, #use this llm
        tools=tools, #search real time internet
        state_modifier=system_prompt

    )
    # query="Tell me about trends in vibecoders"
    state={"messages":query}
    print(state)
    response=agent.invoke(state)#is an obj
    messages=response.get("messages")
    ai_message=[message.content for message in messages if isinstance(message,AIMessage)] #only ai-response list
    return ai_message[-1]
    # print(ai_message[-1])





