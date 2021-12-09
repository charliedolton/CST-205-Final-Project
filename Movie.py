class Movie:

    user_favorites = {
        "0000": []
    }

    def __init__(self, id, title, release_date, overview):
        self.id
        self.title = title
        self.release_date = release_date
        self.overview = overview

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_release_date(self):
        return self.release_date

    def get_overview(self):
        return self.overview

    def print_info(self):
        print(f'   id: {self.id}\n    title: {self.title}\n   release year: {self.release_date}\n   overview: {self.overview}')

    def add_newUser(str_user_id):
        Movie.user_favorites[str_user_id] = []

    def add_favorite(str_user_id, movie):
        tuple = (movie.get_id(), movie.get_title(), movie.get_overview(), movie.get_release_date())
        user_favorites[str_user_id].append()