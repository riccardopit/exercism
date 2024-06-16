def resistor_label(colors):
    resistance_colors = ["black", "brown", "red", "orange", "yellow",
                         "green", "blue", "violet", "grey", "white"]
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    tolerance_percentages = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
                             "brown": 1, "red": 2, "gold": 5, "silver": 10}
    if len(colors) == 1 and "black" in colors:
        return "0 ohms"
    digit_1 = str(resistance_colors.index(colors[0]))
    digit_2 = str(resistance_colors.index(colors[1]))
    if len(colors) > 4:
        digit_3 = str(resistance_colors.index(colors[2]))
    else:
        digit_3 = ""
    digits = digit_1 + digit_2 + digit_3
    zeros = "0" * resistance_colors.index(colors[-2])
    resistance = int(digits + zeros)
    units_index = 0
    while resistance > 1000:
        resistance = resistance / 1000
        units_index += 1
    if int(resistance) == resistance: resistance = int(resistance)
    unit = units[units_index]
    tolerance = tolerance_percentages[colors[-1]]
    resistance = f"{resistance} {unit} ±{tolerance}%"
    return resistance
