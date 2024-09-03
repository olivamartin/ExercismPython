"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 5
PREPARATION_TIME = 10

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.

"""Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

def bake_time_remaining(time_lapsed):
    """
    Returns the remaining bake time given 
    the time lapsed
    """
    return EXPECTED_BAKE_TIME - time_lapsed
    
#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

def preparation_time_in_minutes(number_of_layers):
    """
    Returns the preparation time in minutes
    given an amount of layers of the lasagna
    """
    return PREPARATION_TIME * number_of_layers
    
#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Returns the elapsed time in minutes depending 
    on the number of layers and the elapsed bake
    time 
    """
    return preparation_time_in_minutes(3) + elapsed_bake_time
   