class MovieObj:

    user_favorites = {
        "0000": ["12", "26", "69"]
    }

    def __init__(self, id, title, release_year, description):
        self.id
        self.title = title
        self.release_year = release_year
        self.description = description

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_release_year(self):
        return self.release_year

    def get_description(self):
        return self.description

    def print_info(self):
        print(f'   id: {self.id}\n    title: {self.title}\n   release year: {self.release_year}\n   description: {self.description}')

    def add_favorite(str_user_id, int_movie_id):
        user_favorites[str_user_id].append()