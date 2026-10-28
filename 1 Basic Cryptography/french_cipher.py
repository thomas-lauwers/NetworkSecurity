from utils.constants import ALPHABET

if __name__ == "__main__":
    ciphertext = "eeg{kjgiflceha-sje-oxvksz-lzaa-ikqni}"
    key = "croissant"
    k_len = len(key)

    inverse = {val: k for k, val in ALPHABET.items()}

    plaintext = ""
    j = 0
    for i in range(len(ciphertext)):
        if ciphertext[i] not in ALPHABET:
            plaintext += ciphertext[i]
            continue

        new_letter_pos = (ALPHABET.get(ciphertext[i]) - ALPHABET.get(key[j % k_len])) % 26
        plaintext += inverse[new_letter_pos]
        j += 1

    print(plaintext)