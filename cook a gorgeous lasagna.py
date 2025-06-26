"""Lasagna Time Calculator.

A simple script that calculates:
- remaining bake time
- preparation time based on number of layers
- total elapsed cooking time
"""

# Constants
EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2     # per layer, in minutes


def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the remaining bake time.

    :param elapsed_bake_time: int - minutes already baked.
    :return: int - remaining minutes.

    Example:
    >>> bake_time_remaining(30)
    10
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate preparation time based on the number of layers.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time (minutes).

    Example:
    >>> preparation_time_in_minutes(2)
    4
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate total elapsed time (prep + bake so far).

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - minutes already baked.
    :return: int - total elapsed time (minutes).

    Example:
    >>> elapsed_time_in_minutes(3, 20)
    26
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


if __name__ == "__main__":
    print("Remaining bake time (30 min baked):", bake_time_remaining(30))  # 10
    print("Prep time for 2 layers:", preparation_time_in_minutes(2))       # 4
    print("Total elapsed time (3 layers, 20 min baked):", elapsed_time_in_minutes(3, 20))  # 26
