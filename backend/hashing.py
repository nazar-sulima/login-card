import hashlib
from mongo import MongoDB

class PasswordHasher:
    def __init__(self, email):
        self.mongo = MongoDB()
        self.email = email
        self.user_password = self.get_user_password()
        
    def get_user_password(self):
        user_password = self.mongo.find_user(self.email)
        return user_password
    
    def hash_password(self):
        hash_object = hashlib.sha256(self.user_password.encode())  # Convert string to bytes
        hash_hex = hash_object.hexdigest()
        return "SHA-256 Hash:", hash_hex

ph = PasswordHasher("ethan.hunt@example.com")
print("ph.get_user_password: ", ph.get_user_password())
print(ph.hash_password())
        