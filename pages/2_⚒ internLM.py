import streamlit as st

if "InternLM_API_KEY" not in st.session_state:
    st.session_state["InternLM_API_KEY"] = ""

if "InternLM_ENVIRONMENT" not in st.session_state:
    st.session_state["InternLM_ENVIRONMENT"] = ""

st.set_page_config(page_title="InternLM Settings", layout="wide")

st.title("InternLM Settings")

InternLM_api_key = st.text_input("API key", value=st.session_state["InternLM_API_KEY"], max_chars=None, key=None, type="default")
environment = st.text_input("Environment", value=st.session_state["InternLM_ENVIRONMENT"], max_chars=None, key=None, type="default")

saved = st.button("Save")

if saved:
    st.session_state["InternLM_API_KEY"] = InternLM_api_key
    st.session_state["InternLM_ENVIRONMENT"] = environment