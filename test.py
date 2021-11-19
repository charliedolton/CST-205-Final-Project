class User:
    ids = 0
    user_id_map = {
        "0000": "test-user"
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password
        if (username == "admin"):
            self.id = 0
        else:
            User.ids += 1
            self.id = User.ids
        User.user_id_map[str(self.id)] = self.username
    
    def get_id(self):
        return self.id

    def get_str_id(self):
        return str(self.id)


class Movie:
    ids = 0

    def __init__(self, title, release_year, description):
        self.title = title
        self.release_year = release_year
        self.description = description
        # self.id = (Movie.ids += 1)

    def print_info(self):
        print(f'   title: {m.title}\n   release year: {m.release_year}\n   description: {m.description}')

admin = User("admin", "admin")
user1 = User("user1", "pass1")
user2 = User("user2", "pass2")

movie0 = Movie("Title0", "0000", "Description0")
movie1 = Movie("Title1", "1111", "Description1")
movie2 = Movie("Title2", "2222", "Description2")

# favorites = []
# favorites.append(dict({str(user1.id): [movie1, movie2]}))
# print(favorites)
# print("----------")
# print("user1's favorites:")
# for m in favorites[0][str(user1.id)]:
#     print("-----")
#     m.print_info()

user_favorites = {
    "0": [movie0]
}

user_favorites[user1.get_str_id()] = [movie1, movie2]
user_favorites[user2.get_str_id()] = [movie2]
# see test-output.txt for current output :D
for id in user_favorites:
    print("----------")
    print(f"{User.user_id_map[id]}'s favorites:")
    for m in user_favorites[id]:
        print("-----")
        m.print_info()