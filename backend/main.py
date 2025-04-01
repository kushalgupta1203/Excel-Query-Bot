from fastapi import FastAPI, UploadFile, File, Form
from query_handler import process_query
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/query/")
async def query(file: UploadFile = File(...), user_query: str = Form(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    response = process_query(file_path, user_query)
    
    return {"response": response}
