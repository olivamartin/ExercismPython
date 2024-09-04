def square(number):
    if 1 <= number <= 64:
        return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    acum = 0
    for i in range (64):
        acum +=  2**i
    return acum
