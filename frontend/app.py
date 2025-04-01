import streamlit as st
import requests

st.title("Excel Query Bot")

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["csv", "xlsx"])
user_query = st.text_input("Enter your query")

if st.button("Submit Query"):
    if uploaded_file and user_query:
        files = {"file": uploaded_file.getvalue()}
        data = {"user_query": user_query}
        
        response = requests.post("http://127.0.0.1:8000/query/", files=files, data=data)
        
        if response.status_code == 200:
            st.write("### Response:")
            st.write(response.json().get("response", "No response received."))
        else:
            st.error("Failed to get a response. Please check the backend.")
