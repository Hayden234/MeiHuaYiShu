import streamlit as st

if "ZHIPUAI_API_KEY" not in st.session_state:
    st.session_state["ZHIPUAI_API_KEY"] = ""
    
st.set_page_config(page_title = "ZhipuAI Settings", layout="wide")

st.title("ZhipuAI Settings")

zhipiai_api_key = st.text_input("API key", value=st.session_state["ZHIPUAI_API_KEY"], max_chars=None, key=None, type="password")

saved = st.button("Save")

if saved:
    st.session_state["ZHIPUAI_API_KEY"] = zhipiai_api_key