import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action"])
        self.regular_movie = Movie("Air", 2016, ["Adventure"])
        self.childrens_movie = Movie("Frozen", 2014, ["Action", "Drama"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2016, ["Adventure"])
        self.assertEqual("Air", m.title)
        self.assertEqual(2016, m.year)
        self.assertEqual(["Adventure"], m.genre)

    def test_movie_methods(self):
        self.assertTrue(self.new_movie.is_genre("acTion"))
        self.assertFalse(self.regular_movie.is_genre("Action"))

    def test_rental_attributes(self):
        r = Rental(self.regular_movie, 1, Rental.REGULAR)
        self.assertEqual(Rental.REGULAR, r.get_price_code())

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.childrens_movie, 7, Rental.CHILDRENS)
        self.assertEqual(rental.get_price(), 7.5)
        rental = Rental(self.regular_movie, 365, Rental.REGULAR)
        self.assertEqual(rental.get_price(), 546.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.childrens_movie, 7, Rental.CHILDRENS)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 365, Rental.REGULAR)
        self.assertEqual(rental.get_rental_points(), 1)
