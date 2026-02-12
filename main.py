from fastapi import FastAPI
from services import analyze_handmade_image  # さっき作ったservices.pyを読み込む
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Craft Lens API is running!"}

@app.get("/test-ai")
def test_ai():
    # 確実に読み込める別の画像URL（例としてWikipediaの猫の画像など）
    test_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg"
    
    # AIを呼び出す
    result = analyze_handmade_image(test_url)
    return {"ai_analysis": result}