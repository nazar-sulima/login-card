from creds import client 

db = client['login-card']

users_collection = db['users']

# users = [{
#     "email": "first@email.com",
#     "password": "password1"
# }, {
#     "email": "second@email.com",
#     "password": "password2" 
# }]

# users_collection.insert_many(users)