def sum_of_multiples(limit, multiples):
    multiples_all = set()
    for multiple in multiples:
        if multiple > 0:
            for mul in range(multiple, limit, multiple):
                multiples_all.add(mul)
    return sum(multiples_all)
    