from mongo import MongoDB
from verification import UserVerification
from hashing import PasswordHasher
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

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
        self.hasher = PasswordHasher()
        
    def set_routes(self):
        @self.app.get("/")
        def welcome():
            return {"message": "Hello WOrld"}
        
        @self.app.get("/users")
        def users():
            return self.mongo.all_users
        
        @self.app.post("/login")
        def login(item: Item):
            user = self.verification.login(item.email, item.password)
            if user == True:
                return "Success"
            else:
                raise HTTPException(status_code=400, detail="Invalid email or password.")
            
        @self.app.post("/register")
        def register(item: Item):
            if self.mongo.find_user(item.email):
                raise HTTPException(status_code=400, detail="User already exists")
            else:
                hashed_password = self.hasher.hash_password(item.password)
                user_data = {
                    "full_name": item.full_name,
                    "email": item.email,
                    "password": hashed_password
                }
                
                self.mongo.add_user(user_data)
                return "Success"
        
api = API()
app = api.app
api.set_routes()