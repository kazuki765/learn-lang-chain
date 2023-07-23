import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
  SystemMessage,
  HumanMessage,
  AIMessage
)
from dotenv import load_dotenv

load_dotenv(verbose=True)

def main():
  llm = ChatOpenAI(temperature=0.8)
  
  st.set_page_config(
    page_title="GPT WEB",
    page_icon="🤖"
  )
  st.header("GPT")
  
  if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant.")
    ]

  container = st.container()
  with container:
    with st.form(key="form", clear_on_submit=True):
      user_input = st.text_area(label="question: ", key="input", height=100)
      submit_button = st.form_submit_button(label="send")
      
    if submit_button and user_input:
      st.session_state.messages.append(HumanMessage(content=user_input))
      with st.spinner("ChatGPT is typing ..."):
        response = llm(st.session_state.messages)
      st.session_state.messages.append(AIMessage(content=response.content))
      
  messages = st.session_state.get('messages', [])
  for message in messages:
      if isinstance(message, AIMessage):
          with st.chat_message('assistant'):
              st.markdown(message.content)
      elif isinstance(message, HumanMessage):
          with st.chat_message('user'):
              st.markdown(message.content)
      else:  # isinstance(message, SystemMessage):
          st.write(f"System message: {message.content}")

if __name__ == '__main__':
    main()