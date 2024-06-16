def value(colors):
    resistance_colors = ["black", "brown", "red", "orange", "yellow",
                         "green", "blue", "violet", "grey", "white"]
    digit_1 = resistance_colors.index(colors[0])
    digit_2 = resistance_colors.index(colors[1])
    resistance = int(str(digit_1) + str(digit_2))
    return resistance
