from mongo import MongoDB
from verification import UserVerification
from hashing import PasswordHasher
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from os import getenv
import requests

# * GOOGLE
from google.auth.transport.requests import Request as GoogleRequest
from google.oauth2 import id_token

# fastapi dev main.py

load_dotenv()

# OAuth 2.0 Endpoint URLs
AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
USER_INFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

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
        self.client_id = getenv("CLIENT_ID")
        self.client_secret = getenv("CLIENT_SECRET")
        self.redirect_uri = getenv("REDIRECT_URI")
        
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
            
        # * GOOGLE LOGIN
        @self.app.get("/google/login")
        def google_login():
            redirect_uri = f"{AUTHORIZATION_URL}?client_id={self.client_id}&response_type=code&redirect_uri={self.redirect_uri}&scope=email profile"
            print("🐍 File: backend/main.py | Line: 74 | google_login ~ redirect_uri",redirect_uri)
            print(RedirectResponse(redirect_uri))
            return RedirectResponse(redirect_uri)
        
        @self.app.get("/auth/callback")
        async def auth_callback(request: Request):
            print("Request: ", vars(request))
            print("\nApp: ", vars(request['app']))
            code = request.query_params.get("code")
            if not code:
                raise HTTPException(status_code=400, detail="Authorization code not provided.")

            # Exchange authorization code for access token
            token_data = {
                "code": code,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "redirect_uri": self.redirect_uri,
                "grant_type": "authorization_code",
            }

            response = requests.post(TOKEN_URL, data=token_data)
            # async with httpx.AsyncClient() as client:
            #     response = await client.post(TOKEN_URL, data=token_data)
            token_info = response.json()

            # Use access token to get user info
            access_token = token_info.get("access_token")
            # idinfo = id_token.verify_oauth2_token(access_token, GoogleRequest(), getenv("CLIENT_ID"))
            userinfo_response = requests.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {access_token}"}
            )
            userinfo = userinfo_response.json()

            # return {"email": idinfo.get("email"), "name": idinfo.get("name")}
            return {"email": userinfo.get("email"), "name": userinfo.get("name")}
            
            
        
api = API()
app = api.app
api.set_routes()