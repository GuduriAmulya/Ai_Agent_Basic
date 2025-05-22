# setup pydantic model
from pydantic import BaseModel       # send the paramters with fixed standard, so that communication is not hampered
from typing import List
class RequestState(BaseModel):# requeststate class inherits BaseModel
    model_name:str
    model_provider:str
    system_prompt:str
    messages:List[str] #type list of type str
    allow_search:bool  #allow_searching_internt bool



# setup ai agent from frontend
#take input from frontend and send resp accordingly
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
app=FastAPI(title="LangGraph AI Agent")
ALLOWED_MODEL_NAMES=["llama3-70b-8192","compound-beta-mini","llama-3.3-70b-versatile","gpt-4o-mini"]
@app.post("/chat")
def chat_endpoint(request:RequestState): # any objec(data) whichever comes should abide by the RequestState class
    """
    API endpoint to interact with chatbot using lAngGrah and search tools(Tavily)
    it dynamically selects model specified in the request
    """
    print("Received model name: ",request.model_name)
    print("Allowed: ",ALLOWED_MODEL_NAMES)

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name, Select valid Ai model"}
    
    #from frontend we get
    llm_id=request.model_name
    query=request.messages
    allow_search=request.allow_search
    system_prompt=request.system_prompt
    provider=request.model_provider
    print(query)
    #Create  AI Agent and get response from it
    response=get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider)
    return response #use this response show in frontend



# run app and swagger test
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=9999)




