class User:
    ids = 0
    # id_to_user_map = {
    #     # user_id: [username, email, password, icon_url]
    #     "0000": ["test-user", "testuser@email.com", "test-pass", "https://www.pexels.com/photo/food-wood-people-school-3843284/ "]
    # }
    # user_to_id_map = {
    #     # username: user_id
    #     "test-user": "0000"
    # }
    id_to_user_map = {}
    user_to_id_map = {}
    
    current_username = None
    current_user_id = None
    is_authenticated = False

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
        User.id_to_user_map[str(self.id)] = [self.username, self.email, self.password, self.icon_url]
        User.user_to_id_map[self.username] = self.id
    
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

    def get_user_to_id_map():
        return User.user_to_id_map

    def get_id_to_user_map():
        return User.id_to_user_map

    def add_user(newUser):
        User.id_to_user_map[newUser.get_str_id()] = [newUser.get_username(), newUser.get_email(), newUser.get_password()]
        User.user_to_id_map[newUser.get_username()] = newUser.get_id()
