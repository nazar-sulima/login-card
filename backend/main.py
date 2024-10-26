from fastapi import FastAPI
from mongo import MongoDB

# fastapi dev main.py

class API:
    def __init__(self):
        self.app = FastAPI()
        self.mongo = MongoDB()
        
    def routes(self):
        @self.app.get("/")
        async def welcome():
            return {"message": "Hello WOrld"}
        
        @self.app.get("/users")
        async def users():
            return self.mongo.all_users
        
api = API()

# app = FastAPI()

# mongo = MongoDB()

# @app.get("/")
# async def welcome():
#     return {"message": "Hello World"}

# @app.get("/users")
# async def users():
#     return mongo.all_users

