def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    return sum([digit ** len(digits) for digit in digits]) == number