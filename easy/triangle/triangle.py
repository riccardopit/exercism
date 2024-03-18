def isTriangle(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b and all([side != 0 for side in sides])
    
def equilateral(sides):
    if isTriangle(sides):
        a, b, c = sides
        return a == b == c
    return False


def isosceles(sides):
    if isTriangle(sides):
        a, b, c = sides
        return a == b or a == c or b == c
    return False


def scalene(sides):
    if isTriangle(sides):
        a, b, c = sides
        return a != b and a != c and b != c
    return False
