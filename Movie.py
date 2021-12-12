class MovieObj:

    user_favorites = {
        "9999": {}
    }

    def __init__(self, id, title, release_date, overview, img_url):
        self.id
        self.title = title
        self.release_date = release_date
        self.overview = overview
        self.img_url = img_url

    def get_id(self):
        return self.id

    def get_str_id(self):
        return str(self.id)

    def get_title(self):
        return self.title

    def get_release_date(self):
        return self.release_date

    def get_overview(self):
        return self.overview

    def get_img_url(self):
        return self.img_url

    def print_info(self):
        print(f'   id: {self.id}\n    title: {self.title}\n   release year: {self.release_date}\n   overview: {self.overview}')

    def add_newUser(str_user_id):
        Movie.user_favorites[str_user_id] = {}

    def add_favorite(str_user_id, movieObj):
        # tuple = (movieObj.get_id(), movieObj.get_title(), movieObj.get_overview(), movieObj.get_release_date())
        user_favorites[str_user_id][movieObj.get_str_id()] = {
            "title": movieObj.get_title(),
            "overview": movieObj.get_overview(),
            "release_date": movieObj.get_release_date(),
            "img_url": movieObj.get_img_url()
        }