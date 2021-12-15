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
## -------------------------------------------------------------

import json

user_favs = {
  '9999': {
    '196': {
      'title': 'Back to the Future Part III',
      'overview': 'The final installment of the Back to the Future trilogy finds Marty digging the trusty DeLorean out of a mineshaft and looking for Doc in the Wild West of 1885. But when their time machine breaks down, the travelers are stranded in a land of spurs. More problems arise when Doc falls for pretty schoolteacher Clara Clayton, and Marty tangles with Buford Tannen.',
      'release_date':'05/25/1990',
      'img_url': None}
  }
}
print(f'type(user_favs): {type(user_favs)}\n\n')
print(f'user_favs: {user_favs}\n\n')

for x in user_favs:
  for movie_id in user_favs[x]:
    movie1 = json.dumps(user_favs[x][movie_id], indent=4)
    movie2 = json.loads(movie1)
    print(f'movie2: {movie2}\n\n')
    print(f'title: {movie2["title"]}\n\n')
    print(f'overview: {movie2["overview"]}\n\n')
    print(f'release_date: {movie2["release_date"]}')