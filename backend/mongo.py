from creds import client

class MongoDB:
    def __init__(self):
        self.db = client['login-card']
        self.users_collection = self.db['users']
        self.all_users = self.find_users()
        # self.user_password = self.find_user()
        
    def find_users(self):
        users_cursor = self.users_collection.find({})
        all_users = []
        for user in users_cursor:
            user['_id'] = str(user['_id'])
            all_users.append(user)
        return all_users
    
    def find_user(self, email):
        user_info = self.users_collection.find_one({"email": email})
        user_password = None
        if user_info:
            user_password = user_info.get("password")
        return user_password

            
