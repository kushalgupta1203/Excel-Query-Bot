import streamlit as st
import requests

st.title("Excel Query Bot")

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["csv", "xlsx"])
user_query = st.text_input("Enter your query")

if st.button("Submit Query"):
    if uploaded_file and user_query:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        data = {"user_query": user_query}
        
        response = requests.post("http://127.0.0.1:8000/query/", files=files, data=data)
        
        st.write("### Full API Response:")
        st.json(response.json())  # Log full response

        if response.status_code == 200:
            st.write("### Answer:")
            st.write(response.json().get("response", "No response received."))
        else:
            st.error(f"Error {response.status_code}: {response.text}")
