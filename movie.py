import csv
from dataclasses import dataclass
from typing import Collection


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def __str__(self):
        return f"{self.title} ({self.year})"

    def is_genre(self, string: str) -> bool:
        return string.lower() in map(lambda x: x.lower(), self.genre)


class MovieCatalog:
    _instance = None

    @classmethod
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_movie(title, year=None) -> Movie:
        with open('movies.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if title == row['title'] and (year == int(row['year']) or not year):
                    return Movie(title=row['title'], year=int(row['year']), genre=row['genres'].split('|'))
