we create a pascal_triangle(n) function that generates a pascal's triangle of size n using the mathematical formula for combination. The function starts by defining an empty list called matrix, which will later be used to store the rows of the triangle.

The function then enters a for loop that will iterate n times. Each iteration of the loop corresponds to a row in the triangle. Within this for loop, the function defines another list called rows, which will be used to store the elements of the current row.

#!/usr/bin/python3
""" Returns a list of lists of integers. """


def factorial(n):
    """ Factorial function. """
    # Base condition to end recursion
    if n == 0:
        return 1
    else:  # n is greater than 0
        return (n * factorial(n-1))


def comb(a, b):
    """ Calculate combination of 2 numbers. """
    # Floor division to get integer as classic division returns float value
    return factorial(a) // (factorial(b) * (factorial(a - b)))


def pascal_triangle(n):
    """ Representing the Pascals triangle of n. """
    # Define matrix
    matrix = []

    # Empty list if n is less than or equal to 0
    if n <= 0:
        return matrix

    # n stands for number of rows so we loop through n
    for x in range(n):
        # Define inner list
        new = []
        for y in range(x + 1):
            # Find the combination of x and y
            result = comb(x, y)
            # Append result to inner list
            new.append(result)
        # Append inner list to matrix
        matrix.append(new)
    # Return list of list
    return matrix