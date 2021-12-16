from database import Database

class User:
    # id_to_user_map = {
        # "9999": {
        #     "username": "test-user",
        #     "email": "testuser@email.com", 
        #     "password": "test-pass",
        #     "iconUrl": "https://www.pexels.com/photo/food-wood-people-school-3843284/",
        #     "about": "It's a classic, that's what it is.",
        #     "kind": "default-kind"
        # }
    # }
    # user_to_id_map = {
    #     # username: user_id
    #     "test-user": "9999"
    # }

    def __init__(self, username, email, password, icon_url):
        self.username = username
        self.email = email
        self.password = password
        self.icon_url = icon_url
        if (username == 'admin'):
            self.id = 0
        else:
            self.id = Database.get_num_users() + 1
    
    def get_id(self):
        return self.id

    def get_str_id(self):
        return str(self.id)

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_icon_url(self):
        return self.icon_url
