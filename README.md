# Excel Query Bot

An AI-powered Excel Query Bot that allows users to upload CSV/XLSX files and ask questions about the data. Built using **FastAPI**, **LangChain**, and **Gemini API (free version - `gemini-1.5-flash`)**, with a **Streamlit** frontend.

## Features
- Upload **CSV/XLSX** files.
- Ask natural language questions about your data.
- Uses **Google Gemini API (free version)** for querying.
- Backend: **FastAPI**
- Frontend: **Streamlit**

## Folder Structure
```
📂 excel-query-bot
├── 📂 backend
│   ├── main.py          # FastAPI server
│   ├── query_handler.py # Query processing logic
│   ├── requirements.txt # Backend dependencies
├── 📂 frontend
│   ├── app.py           # Streamlit frontend
├── .env                 # API key configuration
├── README.md            # Project documentation
```

## Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/excel-query-bot.git
cd excel-query-bot
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv  # Windows/Linux/Mac
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Your Google Gemini API Key
Create a **.env** file in the root folder and add:
```
GEMINI_API_KEY=your_google_gemini_api_key
```

### 5️⃣ Run the FastAPI Backend
```bash
uvicorn backend.main:app --reload
```
- API will be available at: `http://127.0.0.1:8000`

### 6️⃣ Run the Streamlit Frontend
```bash
streamlit run frontend/app.py
```
- The app will open in your browser.

## Usage
1. Upload a **CSV/XLSX** file.
2. Enter a question (e.g., "What is the total sales?").
3. Click **Submit Query**.
4. The AI will process the query and return an answer.
