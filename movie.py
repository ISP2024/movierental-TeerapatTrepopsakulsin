import logging
from pricing import PriceStrategy


class Movie:
    """
    A movie available for rent.
    """
    REGULAR = PriceStrategy.REGULAR
    NEW_RELEASE = PriceStrategy.NEW_RELEASE
    CHILDRENS = PriceStrategy.CHILDRENS

    def __init__(self, title, strategy):
        # Initialize a new movie.
        if not isinstance(strategy, PriceStrategy):
            log = logging.getLogger()
            log.error(
                f"Movie {self} has unrecognized priceCode {self.get_price_code()}")
            raise TypeError(f"Unrecognized priceCode {self.get_price_code()}")
        self.title = title
        self.price_code = strategy

    def get_price_code(self):
        # get the strategy
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_price(self, days: int) -> float:
        """Compute rental change."""
        return self.price_code.get_price(days)

    def get_rental_points(self, days: int) -> int:
        """Compute the frequent renter points based on movie price code."""
        return self.price_code.get_rental_points(days)
