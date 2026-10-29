import hashlib

USERNAME = "user"
REALM = "PythonRTSP"
NONCE = "4874a055c3f4390506d99e6c51a9e3e360cbef8a62abd7079e11faddcb70a38c"
URI = "rtsp://cns-test.idlab.uantwerpen.be:50002/video"
METHOD = "DESCRIBE"
RESPONSE = "b3539154c5b784bba2c47a1a6c7c4ab0"

WORDLIST = "rockyou.txt"


def md5_hex(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()


def rtsp_digest(password: str) -> str:
    ha1 = md5_hex(f"{USERNAME}:{REALM}:{password}")
    ha2 = md5_hex(f"{METHOD}:{URI}")
    return md5_hex(f"{ha1}:{NONCE}:{ha2}")


if __name__ == "__main__":
    with open(WORDLIST, "r", errors="ignore") as f:
        for line in f:
            password = line.rstrip("\r\n")
            if rtsp_digest(password) == RESPONSE:
                print(f"Password found: {password}")
                break
        else:
            print("Password not found in wordlist.")