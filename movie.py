import logging
from enum import Enum


class PriceStrategy(Enum):
    # The types of movies
    # (price_code, starter_price, starter_duration, price_multiplier, starter_point, point_multiplier).
    REGULAR = [0, 2.0, 2, 1.5, 1, 0]
    NEW_RELEASE = [1, 0.0, 0, 3, 0, 1]
    CHILDRENS = [2, 1.5, 3, 1.5, 1, 0]

    def __str__(self):
        return self.name

    def compute_price(self, days: int) -> float:
        amount = self.value[1]
        if days > self.value[2]:
            amount += self.value[3] * (days - self.value[2])
        return amount

    def compute_rental_points(self, days: int) -> int:
        return self.value[4] + days * self.value[5]

    @property
    def price_code(self):
        return self.value[0]


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
                f"Movie {self} has unrecognized priceCode {self.get_strategy()}")
            raise TypeError(f"Unrecognized priceCode {self.get_strategy()}")
        self.title = title
        self.strategy = strategy
        self.price_code = self.strategy.price_code

    def get_strategy(self):
        # get the strategy
        return self.strategy

    def get_price_code(self):
        # get the strategy
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_price(self, days: int) -> float:
        """Compute rental change."""
        return self.strategy.compute_price(days)

    def get_rental_points(self, days: int) -> int:
        """Compute the frequent renter points based on movie price code."""
        return self.strategy.compute_rental_points(days)
