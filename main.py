import requests
from bs4 import BeautifulSoup

# CONSTANTS:
URL = "https://www.empireonline.com/movies/features/best-movies-2/"


class Top100Movies:

    def __init__(self):
        self.response = requests.get(url=URL)
        self.response.raise_for_status()
        self.movies_url = self.response.text
        print(self.response.status_code)

        self.movies()

    def movies(self):
        try:
            soup = BeautifulSoup(self.movies_url, "html.parser")
        except ConnectionError:
            return ConnectionError

        else:
            movies = soup.findAll(name="h3", class_="title")
            movies_titles = [movie.getText() for movie in movies]
            with open("top_100_movies.txt", mode="w") as file:
                for movie in movies_titles:
                    file.write(f"{movie}\n")


Top100Movies()
