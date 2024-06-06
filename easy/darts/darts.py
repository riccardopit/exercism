def score(x, y):
    r_outer = 10
    r_middle = 5
    r_inner = 1
    
    r = (x**2 + y**2)**0.5

    if r > r_outer:
        return 0
    if r > r_middle:
        return 1
    if r > r_inner:
        return 5
    return 10