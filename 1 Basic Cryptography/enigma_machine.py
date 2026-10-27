class Rotor:
    def __init__(self, string):
        self.str = string

    def advance(self):
        self.str = self.str[1:] + self.str[:1]

if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = "HKV{BSBU-B-SJYZNNB-DNFW-IXH-YTA-RPL-RTXOLWFQ}"
    rotor1 = Rotor("MACHINEBDFGJKLOPQRSTUVWXYZ")
    rotor2 = Rotor("ORBITACDEFGHJKLMNPQSUVWXYZ")
    rotor3 = Rotor("CIPHERABDFGJKLMNOQSTUVWXYZ")

    ciphertext_clean = ciphertext.replace("-", "").replace("{", "").replace("}", "")
    c_length = len(ciphertext_clean)

    plain = ""
    i = 0
    for letter in ciphertext_clean:
        rotor1.advance()
        if i != 0 and i % 25 == 0:
            rotor2.advance()
            if i % 676 == 0:
                rotor3.advance()

        index3 = rotor3.str.index(letter)
        char2 = alphabet[index3]

        index2 = rotor2.str.index(char2)
        char1 = alphabet[index2]

        index1 = rotor1.str.index(char1)
        char = alphabet[index1]

        plain += char
        i += 1

    print(plain)




