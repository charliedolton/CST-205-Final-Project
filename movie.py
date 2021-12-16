from database import Database

class MovieObj:

    def __init__(self, m_id, m_title, m_release_date, m_overview, m_img_url):
        self.info = dict(
            movie_id = m_id,
            title = m_title,
            release_date = m_release_date,
            overview = m_overview,
            img_url = m_img_url
        )

    def get_id(self):
        return self.info["movie_id"]

    def get_str_id(self):
        return str(self.info["movie_id"])

    def get_title(self):
        return self.info["title"]

    def get_release_date(self):
        return self.info["release_date"]

    def get_overview(self):
        return self.info["overview"]

    def get_img_url(self):
        return self.info["img_url"]
    
    def get_info(self):
        return self.info

    def print_info(self):
        print(f'   id: {self.info["movie_id"]}\n    title: {self.info["title"]}\n   release year: {self.info["release_date"]}\n   overview: {self.info["overview"]}')