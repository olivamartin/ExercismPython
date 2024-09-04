def is_armstrong_number(number):
    number_str = str(number)
    total = 0
    digits = [int(digit) for digit in number_str]
    length = len(digits)

    for i in digits:
        total += i**length

    return total == number