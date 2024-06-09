def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text_rotated = ""
    for letter in text:
        if not letter.isalpha():
            text_rotated += letter
            continue
        upper = False
        if letter.isupper():
            letter_lwr = letter.lower()
            upper = True
        else:
            letter_lwr = letter
        index = alphabet.index(letter_lwr) + key
        if index > len(alphabet) - 1:
            index -= len(alphabet)
        if upper:
            text_rotated += alphabet[index].upper()
        else:
            text_rotated += alphabet[index]
        
    return text_rotated
