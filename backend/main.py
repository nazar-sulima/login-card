from fastapi import FastAPI
from mongo import MongoDB

app = FastAPI()

mongo = MongoDB()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def root():
    return mongo.all_users

