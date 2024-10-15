# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air"),
        Movie("Oppenheimer"),
        Movie("Frozen"),
        Movie("Bitconned"),
        Movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    movies = make_movies()
    price_strategy = (Rental.NEW_RELEASE, Rental.REGULAR, Rental.CHILDRENS)
    for i in range(len(movies)):
        customer.add_rental(Rental(movies[i], days, price_strategy[i%3]))
        days = (days + 2) % 5 + 1
    print(customer.statement())
