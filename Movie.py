class MovieObj:

    user_favorites = {
        "9999": {}
    }

    def __init__(self, m_id, m_title, m_release_date, m_overview, m_img_url):
        self.info = dict(
            movie_id = m_id,
            title = m_title,
            release_date = m_release_date,
            overview = m_overview,
            img_url = m_img_url
        )

    def get_id(self):
        return self.info["Movie_id"]

    def get_str_id(self):
        return str(self.info["Movie_id"])

    def get_title(self):
        return self.info["title"]

    def get_release_date(self):
        return self.info["release_date"]

    def get_overview(self):
        return self.info["overview"]

    def get_img_url(self):
        return self.info["img_url"]

    def print_info(self):
        print(f'   id: {self.info["Movie_id"]}\n    title: {self.info["title"]}\n   release year: {self.info["release_date"]}\n   overview: {self.info["overview"]}')

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