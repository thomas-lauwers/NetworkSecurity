from constants import ALPHABET

if __name__ == "__main__":
    ciphertext = "fqv{iluvw-fkdoohqjh}"

    inverse = {val: k for k, val in ALPHABET.items()}

    letter1_value = ALPHABET.get(ciphertext[0])
    shift_amt = ALPHABET.get('c') - letter1_value

    plaintext = ""
    for letter in range(len(ciphertext)):
        if ciphertext[letter] not in ALPHABET:
            plaintext += ciphertext[letter]
            continue

        new_letter_value = (ALPHABET.get(ciphertext[letter]) + shift_amt) % 26
        new_letter = inverse[new_letter_value]
        plaintext += new_letter

    print(plaintext)
