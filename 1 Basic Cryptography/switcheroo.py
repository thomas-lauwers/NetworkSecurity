if __name__ == "__main__":
    plain =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"
    ciphertext = "EFL{STZZTK-LGXH}"

    plaintext = ""
    for letter in ciphertext:
        cipher_pos = cipher.find(letter)
        if cipher_pos is -1:
            plaintext += letter
            continue

        plain_letter = plain[cipher_pos]
        plaintext += plain_letter

    print(plaintext)