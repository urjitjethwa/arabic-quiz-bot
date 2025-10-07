# -*- coding: utf-8 -*-



import streamlit as st

with open("Arabic_Lesson-3-4.txt", encoding="utf-8") as f:
    arabic_text = f.read()
st.session_state["arabic_text"] = arabic_text

st.chat_input("Ask me anything about Arabic lessons")
