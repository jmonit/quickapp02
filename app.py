import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]


response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response["choices"][0]["message"]["content"])

