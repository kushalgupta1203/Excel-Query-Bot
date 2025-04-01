from fastapi import FastAPI, UploadFile, File, Form
from backend.query_handler import process_query
import shutil
import os
from dotenv import load_dotenv

# Load environment variables from the root folder
load_dotenv(dotenv_path=os.path.abspath(os.path.join(os.getcwd(), ".env")))

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/query/")
async def query(file: UploadFile = File(...), user_query: str = Form(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        response = process_query(file_path, user_query)
        
        return {"response": response}
    
    except Exception as e:
        print("Error:", str(e))  # Print error in backend logs
        return {"error": str(e)}
