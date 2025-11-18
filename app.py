import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("OpenAI Test")

if st.button("Test OpenAI"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Say hello!"}
        ]
    )

    st.write(response.choices[0].message["content"])
