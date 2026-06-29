def is_armstrong_number(number):
    temp = number
    digits = 0

    # Count the number of digits
    while temp > 0:
        digits += 1
        temp //= 10

    temp = number
    total = 0

    # Calculate the sum of each digit raised to the power
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == number