def steps(number):
    if number > 0:
        i = 0
        while number != 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number + 1
            i+=1
        return i
    else: 
        raise ValueError("Only positive integers are allowed")

print(steps(1))
print(steps(12))
print(steps(1000000))

