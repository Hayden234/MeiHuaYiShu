import os

import streamlit as st
from zhipuai import ZhipuAI
from langchain.schema import AIMessage, HumanMessage

ZhipuAI_API_KEY = os.getenv('ZhipuAI_API_KEY')   # 读取系统设置的环境变量

# 加载模型
model = ZhipuAI(api_key=ZhipuAI_API_KEY) # 填写您自己的APIKey

def get_response(prompt):
    response = model.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "Generating response..."}  # Add placeholder content
        ],
    )
    return response.choices[0].message 

st.set_page_config(page_title="Welcome to ASL", layout="wide")
st.title("😃~欢迎来到，梅花易数智能体")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.container():
    st.header("遇事不决问梅梅")
    for message in st.session_state["messages"]:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)
    prompt = st.chat_input("请输入2个数字和你想问的问题...")
    if prompt:
        st.session_state["messages"].append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        ai_message = get_response(prompt)
        st.session_state["messages"].append(AIMessage(content=ai_message.content))
        with st.chat_message("assistant"):
            st.markdown(ai_message.content)
