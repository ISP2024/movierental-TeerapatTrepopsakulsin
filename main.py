# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer

def make_movies():
    """Some sample movies."""
    catalog = MovieCatalog
    movie_name_list = ("A Million Miles Away", "Oppenheimer", "Cinderella", "Bitconned", "Particle Fever")
    return map(lambda x: catalog.get_movie(x), movie_name_list)


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    movies = make_movies()
    for movie in movies:
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
