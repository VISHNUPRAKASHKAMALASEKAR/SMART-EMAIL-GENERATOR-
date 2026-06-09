import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6JMgmS4BmHPOMe26ph1RZ3hs_Pp4akKwYSh5HA-am7PCA")

model = genai.GenerativeModel("gemini-2.5-flash")

topic = st.text_input("Email Topic")

if st.button("Generate"):
    prompt = "Write a professional email about " + topic
    response = model.generate_content(prompt)
    st.write(response.text)