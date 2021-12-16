from database import Database

class MovieObj:

    def __init__(self, m_id, m_title, m_release_date, m_overview, m_img_url):
        self.movie_id = m_id,
        self.title = m_title,
        self.release_date = m_release_date,
        self.overview = m_overview,
        self.img_url = m_img_url

    def get_id(self):
        return self.movie_id

    def get_str_id(self):
        return str(self.movie_id)

    def get_title(self):
        return self.title

    def get_release_date(self):
        return self.release_date

    def get_overview(self):
        return self.overview

    def get_img_url(self):
        return self.img_url
    
    def get_info(self):
        return self.info

    def print_info(self):
        print(f'   id: {self.movie_id}\n    title: {self.title}\n   release year: {self.release_date}\n   overview: {self.overview}')