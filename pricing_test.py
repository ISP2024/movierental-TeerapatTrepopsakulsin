import unittest
import datetime
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("new", datetime.datetime.now().year, ["Adventure"])
        self.regular_movie = Movie("reg", 2016, ["Adventure"])
        self.childrens_movie = Movie("child", 2016, ["Children"])

    def test_pricing_for_new_movie(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.price_code_for_movie(), Rental.NEW_RELEASE)

    def test_pricing_for_regular_movie(self):
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.price_code_for_movie(), Rental.REGULAR)

    def test_pricing_for_childrens_movie(self):
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.price_code_for_movie(), Rental.CHILDRENS)
