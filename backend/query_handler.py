import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_data(file_path):
    """Load CSV or XLSX file into a Pandas DataFrame."""
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format!")

def process_query(file_path, query):
    """Processes user query using LangChain and Gemini API."""
    df = load_data(file_path)
    
    prompt = f"""
    Given the following table, answer the query based on the data:
    
    {df.head().to_string()}
    
    Query: {query}
    """
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text if response else "I couldn't process that query."
