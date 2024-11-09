import hashlib
from mongo import MongoDB

class PasswordHasher:
    def __init__(self):
        self.mongo = MongoDB()
    
    def hash_password(self, password):
        hash_object = hashlib.sha256(password.encode()) 
        hash_hex = hash_object.hexdigest()
        return hash_hex