import cipher


if __name__ == "__main__":
    ciphertext = "22135cc0b9daa9e717f98a998e6ee5e92655e1a88f"
    known_plaintext = b"STATUS: SERVER ONLINE"
    secret_text = "12296eef9eece6b42dd2bf90aa63b6d21a7cc98b95c78b4b01d833d628a941b82fb65176b4ed3c3f64"

    cipher_bytes = bytes.fromhex(ciphertext)
    secret_bytes = bytes.fromhex(secret_text)

    known_keystream = bytes(p ^ c for p, c in zip(known_plaintext, cipher_bytes))


    for seed in range(cipher.M):
        first_state = (cipher.A * seed + cipher.C) % cipher.M
        if ((first_state >> 16) & 0xff) != known_keystream[0]:
            continue

        if cipher.generate_keystream(seed, len(known_keystream)) == known_keystream:
            print("Recovered seed:", seed)
            flag = cipher.decrypt(secret_bytes, seed)
            print("Plaintext:", flag.decode())
            break



