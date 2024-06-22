def transform(legacy_data):
    points = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    data = {}
    for k, v in legacy_data.items():
        for letter in v:
            data[letter.lower()] = k

    return data
    