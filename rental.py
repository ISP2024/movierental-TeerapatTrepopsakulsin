import logging
import datetime
from pricing import PriceStrategy


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    REGULAR = PriceStrategy.REGULAR
    NEW_RELEASE = PriceStrategy.NEW_RELEASE
    CHILDRENS = PriceStrategy.CHILDRENS
    
    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = self.price_code_for_movie()

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def is_new_release(self) -> bool:
        return self.movie.year == datetime.datetime.now().year

    def is_childrens(self) -> bool:
        return self.movie.is_genre("Children") or self.movie.is_genre("Childrens")

    def price_code_for_movie(self):
        if self.is_new_release():
            return self.NEW_RELEASE
        if self.is_childrens():
            return self.CHILDRENS
        return self.REGULAR

    def get_price_code(self):
        # get the price_code(strategy)
        return self.price_code

    def get_price(self) -> float:
        """Compute rental change."""
        return self.get_price_code().get_price(self.get_days_rented())

    def get_rental_points(self) -> int:
        """Compute the frequent renter points based on movie price code."""
        return self.get_price_code().get_rental_points(self.get_days_rented())
