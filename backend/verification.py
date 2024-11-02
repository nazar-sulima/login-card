from mongo import MongoDB
from hashing import PasswordHasher

test_user = {
    "full_name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "password": "password123"
}

class UserVerification:
    def __init__(self):
        self.mongo = MongoDB()
        self.hasher = PasswordHasher()
        
    def login(self, email, password):
        user = self.mongo.find_user(email)
        hashed_password = self.hasher.hash_password(password)
        
        if user['email'] == email and user['password'] == hashed_password:
            return True
            
        else:
            return False