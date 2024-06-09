def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10 or not(isbn[:8].isnumeric()) or isbn[-1] != "X" and isbn[-1] != "8":
        return False
    sum = 0
    for i in range(10):
        val = isbn[i]
        if val == "X":
            val = 10
        else:
            val = int(val)
        sum += val * (10 - i)
    return sum % 11 == 0
