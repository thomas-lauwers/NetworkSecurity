from Crypto.Cipher import DES


def brute_force_plaintext():
    for a in range(256):
        for b in range(256):
            key = namespace + bytes([a, b])
            cipher = DES.new(key, DES.MODE_ECB)
            plaintext = cipher.decrypt(ciphertext)
            pt_decoded = plaintext.decode('ASCII', "ignore")
            if pt_decoded.startswith("cns{"):
                return pt_decoded

    return None


if __name__ == "__main__":
    ciphertext = bytes.fromhex("74eb40cf03b84d0bc4cd2c6e0fe97fb4e70546d3e09c530d35b344e530351bac")
    namespace = b"IOTDEV"

    plain = brute_force_plaintext()
    print(plain)

