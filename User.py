class User:
    ids = 0
    id_to_user_map = {
        "0000": ["test-user", "test-pass"]
    }
    user_to_id_map = {
        "test-user": "0000"
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password
        if (username == "admin"):
            self.id = 0
        else:
            User.ids += 1
            self.id = User.ids
        User.id_to_user_map[str(self.id)] = self.username
        User.user_to_id_map[self.username] = self.id
    
    def get_id(self):
        return self.id

    def get_str_id(self):
        return str(self.id)

    def get_username(self):
        return self.username

    def get_password(self):

    def add_user(newUser):
        User.id_to_user_map[newUser.get_str_id()] = [newUser.get_username, newUser.get_password]
        User.user_to_id_map[newUser.get_username()] = newUser.get_id