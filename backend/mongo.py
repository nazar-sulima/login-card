from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = MongoClient(getenv('MONGODB'))

class MongoDB:
    def __init__(self):
        self.db = client['login-card']
        self.users_collection = self.db['users']
        self.all_users = self.find_users()
        
    def find_users(self):
        users_cursor = self.users_collection.find({})
        all_users = []
        for user in users_cursor:
            user['_id'] = str(user['_id'])
            all_users.append(user)
        return all_users
    
    def find_user(self, email):
        user_info = self.users_collection.find_one({"email": email})
        if user_info:
            user_info['_id'] = str(user_info['_id'])
            return user_info
        
    def add_user(self, user_data):
        self.users_collection.insert_one(user_data)
        print("User successfuly added to the database!")