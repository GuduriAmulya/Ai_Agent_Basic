#setup ui
import streamlit as st

st.set_page_config(page_title="LangGraph Agen UI",layout="centered")
st.title("AI chatbot agent")
st.write("Create and interact with AI Agent")


system_prompt=st.text_area("Define your AI Agent",height=70,placeholder="Type your prompt here...")

MODEL_NAMES_GROQ=["llama-3.3-70b-versatile","llama3-70b-8192"]
MODEL_NAMES_OPENAI=["gpt-4o-mini"]

provider=st.radio("Select Provider: ",{"Groq","OpenAI"})
if provider=="Groq":
    selected_model=st.selectbox("Select Groq Mode: ",MODEL_NAMES_GROQ)
elif provider=="OpenAI":
    selected_model=st.selectbox("Select OpenAI Model: ",MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")
user_query=st.text_area("Enter your query",height=100,placeholder="Ask anything!")
API_URL="http://127.0.0.1:9999/chat"
if st.button("Ask Agent"):
    #get resp from backend and show here
    if user_query.strip():
        # connect with backend url
        import requests

        payload={ "model_name":selected_model,
        "model_provider":provider,
        "system_prompt":system_prompt,
        "messages":[user_query],
        "allow_search":allow_web_search
        }
        response=requests.post(API_URL,json=payload)
        
        # response="Hi, this is dummy response.."
        if response.status_code==200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response**{response_data}")

#connect with backend via url..
