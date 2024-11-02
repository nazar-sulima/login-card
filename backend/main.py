from fastapi import FastAPI, HTTPException
from mongo import MongoDB
from pydantic import BaseModel
from verification import UserVerification

# fastapi dev main.py

class Item(BaseModel):
    full_name: str
    email: str
    password: str

class API:
    def __init__(self):
        self.app = FastAPI()
        self.mongo = MongoDB()
        self.verification = UserVerification()
        
    def set_routes(self):
        @self.app.get("/")
        def welcome():
            return {"message": "Hello WOrld"}
        
        @self.app.get("/users")
        def users():
            return self.mongo.all_users
        
        @self.app.post("/login")
        def login(item: Item):
            user = self.verification.login_user(item.email, item.password)
            return user
            # return {
            #     "full_name": item.full_name,
            #     "email": item.email,
            #     "password": item.password
            # }
        
api = API()
app = api.app
api.set_routes()