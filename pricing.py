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