"""
Lasagna cooking time calculator.

This module provides functions to calculate preparation time,
bake time remaining, and total elapsed time for cooking a lasagna.
"""
# Constants
EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME_PER_LAYER = 2  # in minutes per layer

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers.
    
    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - total prep time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME_PER_LAYER

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time (prep + bake).
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - total time spent (prep + baking).
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time

# Example usage:
print(bake_time_remaining(30))           # Should return 10
print(preparation_time_in_minutes(2))    # Should return 4
print(elapsed_time_in_minutes(3, 20))    # Should return 26
