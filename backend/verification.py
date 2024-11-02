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
        
    def login_user(self, email, password):
        user = self.mongo.find_user(email)
        print(user)
        hashed_password = self.hasher.hash_password(password)
        print(hashed_password)
        
        if user['email'] == email and user['password'] == hashed_password:
            print("User found in database!")
            
        else:
            print("User is not in database. Please register")
            
uv = UserVerification()
uv.login_user(test_user["email"], test_user["password"])