import unittest
import datetime
from rental import Rental
from movie import Movie, MovieCatalog


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Air1", datetime.datetime.now().year, ["Adventure"])
        self.regular_movie = Movie("Air2", 2016, ["Adventure"])
        self.childrens_movie = Movie("Air3", 2016, ["Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = self.regular_movie
        self.assertEqual("Air2", m.title)
        self.assertEqual(2016, m.year)
        self.assertEqual(["Adventure"], m.genre)

    def test_movie_methods(self):
        self.assertTrue(self.new_movie.is_genre("AdveNture"))
        self.assertFalse(self.regular_movie.is_genre("Action"))

    def test_movie_catalog(self):
        catalog = MovieCatalog
        # Get the first movie named 'Mulan'
        old_movie = catalog.get_movie("Mulan")
        self.assertEqual(old_movie, Movie(title='Mulan', year=1998, genre=['Animation', 'Action', 'Children']))

        # Get 'Mulan' released in 2020
        movie = catalog.get_movie("Mulan", 2020)
        self.assertEqual(movie, Movie(title='Mulan', year=2020, genre=['Action', 'Adventure', 'Children']))

        no_movie = catalog.get_movie("Lanmu")
        self.assertIsNone(no_movie)

    def test_rental_attributes(self):
        r = Rental(self.regular_movie, 1)
        self.assertEqual(Rental.REGULAR, r.get_price_code())

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
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.childrens_movie, 7)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 365)
        self.assertEqual(rental.get_rental_points(), 1)
