import pandas as pd

class User:
    ids = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.ids += 1
        self.id = User.ids

class Movie:
    ids = 0

    def __init__(self, title, release_year, description):
        self.title = title
        self.release_year = release_year
        self.description = description
        # self.id = (Movie.ids += 1)

    def print_info(self):
        print(f'   title: {m.title}\n   release year: {m.release_year}\n   description: {m.description}')


user1 = User("user1", "pass1")
user2 = User("user2", "pass2")

movie1 = Movie("Title1", "1111", "Description1")
movie2 = Movie("Title2", "2222", "Description2")

favorites = []
favorites.append(dict({str(user1.id): [movie1, movie2]}))
print(favorites)
print("user1's favorites:")
for m in favorites[0][str(user1.id)]:
    print("-----")
    m.print_info()