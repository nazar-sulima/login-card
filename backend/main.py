# * Other files
from mongo import MongoDB
from verification import UserVerification
from hashing import PasswordHasher

# * FastAPI
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import RedirectResponse

# * GOOGLE
from google.auth.transport.requests import Request as GoogleRequest
from google.oauth2 import id_token

# * Others
import requests
from os import getenv
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# fastapi dev main.py

load_dotenv()

# OAuth 2.0 Endpoint URLs
AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
USER_INFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

class Item(BaseModel):
    full_name: str = None
    email: str = None
    password: str = None

class API:
    def __init__(self):
        self.app = FastAPI()
        self.mongo = MongoDB()
        self.verification = UserVerification()
        self.hasher = PasswordHasher()
        self.client_id = getenv("CLIENT_ID")
        self.client_secret = getenv("CLIENT_SECRET")
        self.redirect_uri = getenv("REDIRECT_URI")
        
    def set_middleware(self):
        origins = [
            "http://localhost:5173", "http://127.0.0.1:5173"
        ]
        
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["GET", "POST", "OPTIONS"],
            allow_headers=["*"]
        )
        
    def set_routes(self):
        @self.app.get("/")
        def welcome():
            return {"message": "Welcome here!"}
        
        @self.app.get("/users")
        def users():
            return self.mongo.all_users
        
        @self.app.post("/login")
        def login(item: Item):
            user = self.verification.login(item.email, item.password)
            if user == True:
                return {"detail": "User found in the db, logging in..."}
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
                return {"detail": "User is successfuly registered!"}
            
        # * GOOGLE LOGIN
        @self.app.get("/google/login")
        def google_login():
            redirect_uri = f"{AUTHORIZATION_URL}?client_id={self.client_id}&response_type=code&redirect_uri={self.redirect_uri}&scope=email profile"
            return RedirectResponse(redirect_uri)
        
        @self.app.get("/auth/callback")
        async def auth_callback(request: Request):
            code = request.query_params.get("code")
            if not code:
                raise HTTPException(status_code=400, detail="Authorization code not provided.")

            token_data = {
                "code": code,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "redirect_uri": self.redirect_uri,
                "grant_type": "authorization_code",
            }

            response = requests.post(TOKEN_URL, data=token_data)
            token_info = response.json()

            access_token = token_info.get("access_token")
            userinfo_response = requests.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {access_token}"}
            )
            userinfo = userinfo_response.json()
            
            print(userinfo)
            
            email = userinfo.get("email")
            name = userinfo.get("name")
            
            existing_user = self.mongo.find_user(email)
            if existing_user:
                return {"detail": "User already exists, logging in"}
            else:
                user_data = {
                    "full_name": name,
                    "email": email,
                    "password": None
                }
                self.mongo.add_user(user_data)
                return {"detail": "User is successfuly registered through Google"}

api = API()
app = api.app
api.set_middleware()
api.set_routes()