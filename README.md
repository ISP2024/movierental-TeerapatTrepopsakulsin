## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
>2.1) code smells: Message Chains    
2.2) design principle: Separation of Concerns, because Movie should not handle information about price 

>5.2) Implement price_code_for_movie in Rental class    
> Explanation:
> - Movie should not handle information about price (Single Responsibility Principle)
> - PriceStrategy should contain only strategy and how to compute price, not movie information (Single Responsibility Principle)
> - Rental have movie and already need to use the PriceStrategy data (High Cohesion)