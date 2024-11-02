import hashlib
from mongo import MongoDB

test_email = "ethan.hunt@example.com"

class PasswordHasher:
    def __init__(self):
        self.mongo = MongoDB()
        self.user_password = self.get_user_password(test_email)
        
    def get_user_password(self, email):
        user = self.mongo.find_user(email)
        user_password = user['password']
        return user_password
    
    def hash_password(self, password):
        hash_object = hashlib.sha256(password.encode()) 
        hash_hex = hash_object.hexdigest()
        return hash_hex
    
    def update_all(self):
        users = self.mongo.find_users() 
        for user in users:
            users_password = user['password']
            hashed_password = self.hash_password(users_password)
            self.mongo.update_passwords(user['email'], hashed_password)

ph = PasswordHasher()
        