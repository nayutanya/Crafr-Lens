from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Craft Lens API is running!"}

@app.get("/db-test")
def test_db():
    # データベースURLが正しく読み込めているか確認
    db_url = os.getenv("DATABASE_URL")
    return {"database_url_configured": bool(db_url)}