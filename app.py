import streamlit as st

st.title("My first app")
name = st.text_input("Your name")
if name:
    st.write(f"Hello, {name}!")