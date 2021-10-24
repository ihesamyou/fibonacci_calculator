

def fibonacci_index(index):
    """returns fibonacci sequence with the given index being the last value.
    raises a type error if given index is a string, float, zero or negative number.
    returns a string for given indexes that are 1 and 2."""
    try:
        if type(index) == str or type(index) == float or index < 1:
            raise TypeError
        elif index < 3:
            return f"""[0, 1]
    For getting better results enter a whole number bigger than 2."""
        else:
            initial_sequence = [0, 1]
            while len(initial_sequence) < index:
                next = initial_sequence[-2] + initial_sequence[-1]
                initial_sequence.append(next)
            return initial_sequence

    except TypeError:
        raise TypeError('Please enter a positive whole number.')


def fibonacci_until(values_until):
    """returns all fibonacci sequence values that are less than the given number.
    raises value error if the input is a string or is less than 0.
    for 0 <= value_until <= 1 returns a string."""

    try:
        if type(values_until) == str or values_until < 0:
            raise ValueError
        elif values_until > 1:
            initial_sequence = [0, 1]
            while initial_sequence[-1] + initial_sequence[-2] < values_until:
                next = initial_sequence[-2] + initial_sequence[-1]
                initial_sequence.append(next)
            return initial_sequence
        else:
            return f"""[0, 1]
    For getting better results enter a number bigger than 1."""

    except ValueError:
        raise ValueError('Please enter a positive number since fibonacci sequence only includes zero and positive numbers.')


# print(fibonacci_index(20))
# print('-------------------------------')
# print(fibonacci_until(24))
