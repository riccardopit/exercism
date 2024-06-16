def label(colors):
    resistance_colors = ["black", "brown", "red", "orange", "yellow",
                         "green", "blue", "violet", "grey", "white"]
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    digit_1 = resistance_colors.index(colors[0])
    digit_2 = resistance_colors.index(colors[1])
    zeros = resistance_colors.index(colors[2])
    resistance = str(int(str(digit_1) + str(digit_2) + "0" * zeros))
    unit = units[resistance.count("000")]
    resistance = resistance.replace("000", "")
    resistance = resistance + " " + unit
    return resistance
