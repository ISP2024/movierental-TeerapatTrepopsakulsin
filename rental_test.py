import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
        self.regular_movie = Movie("Air", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", Movie.REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(Movie.REGULAR, m.get_strategy())

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.childrens_movie, 7)
        self.assertEqual(rental.get_price(), 7.5)
        rental = Rental(self.regular_movie, 365)
        self.assertEqual(rental.get_price(), 546.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.rental_points(), 5)
        rental = Rental(self.childrens_movie, 7)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.regular_movie, 365)
        self.assertEqual(rental.rental_points(), 1)
