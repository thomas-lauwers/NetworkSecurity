from Crypto.Cipher import DES


if __name__ == "__main__":
    cipher = bytes.fromhex("74eb40cf03b84d0bc4cd2c6e0fe97fb4e70546d3e09c530d35b344e530351bac")
    namespace = b"IOTDEV"

    for a in range(256):
        for b in range(256):
            key = namespace + bytes([a, b])
            plaintext = DES.new(key, DES.MODE_ECB).decrypt(cipher)
            pt_decoded = plaintext.decode('ASCII', "ignore")
            if pt_decoded.startswith("cns{"):
                print(pt_decoded)
