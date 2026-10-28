if __name__ == "__main__":
    cipher = "fqv{iluvw-fkdoohqjh}"
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
     'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    inverse = {val: k for k, val in alphabet.items()}

    letter1_value = alphabet.get(cipher[0])
    shift_amt = alphabet.get('c') - letter1_value

    plaintext = ""
    for letter in range(len(cipher)):
        if cipher[letter] not in alphabet:
            plaintext += cipher[letter]
            continue

        new_letter_value = (alphabet.get(cipher[letter]) + shift_amt) % 26
        new_letter = inverse[new_letter_value]
        plaintext += new_letter

    print(plaintext)
