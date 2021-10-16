

def fibonacci_index(index: int) -> int:
    """returns fibonacci sequence with the given index being the last value.
    raises a type error if given index is a string, float or zero.
    returns a string for given indexes that are 1 and 2."""

    if type(index) == str or type(index) == float or index < 1:
        raise TypeError('Please enter a positive whole number.')
    elif index < 3:
        return f"""[0, 1]
For getting better results enter a whole number bigger than 2."""
    else:
        initial_sequence = [0, 1]
        while len(initial_sequence) < index:
            next = initial_sequence[-2] + initial_sequence[-1]
            initial_sequence.append(next)
        return initial_sequence


def fibonacci_until(values_until: int or float) -> int or float:
    """returns all fibonacci sequence values that are less than the given number.
    raises value error if the given number is less than 0.
    for 0 <= value_until <= 1 returns a string."""

    if type(values_until) == str or values_until < 0:
        raise ValueError(
            'Please enter a positive number since fibonacci sequence only includes zero and positive numbers.')
    elif values_until > 1:
        initial_sequence = [0, 1]
        while initial_sequence[-1] + initial_sequence[-2] < values_until:
            next = initial_sequence[-2] + initial_sequence[-1]
            initial_sequence.append(next)
        return initial_sequence
    else:
        return f"""[0, 1]
For getting better results enter a number bigger than 1."""


# print(fibonacci_index(20))
# print('-------------------------------')
# print(fibonacci_until(24))
