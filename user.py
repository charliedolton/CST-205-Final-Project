from database import Database

class User:
    ids = Database.get_num_users()
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
            User.ids += 1
            self.id = User.ids
        Database.id_to_user_map[str(self.id)] = [self.username, self.email, self.password, self.icon_url]
        Database.user_to_id_map[self.username] = self.id
    
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
