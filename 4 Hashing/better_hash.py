def rol(x, n):
    return ((x << n) | (x >> (8 - n))) & 0xff

def ror(x, n):
    return ((x >> n) | (x << (8 - n))) & 0xff

def better_hash(msg):
    state = bytearray(msg.encode())

    for rnd in range(8):

        for i in range(len(state)):
            state[i] ^= (rnd * 41 + i * 17) & 0xff
            state[i] = rol(state[i], (rnd + i) & 7)

        for i in range(1, len(state)):
            state[i] ^= state[i - 1]

        state = state[1:] + state[:1]

    return state.hex()

def recover_flag(target_hex):
    state = bytearray.fromhex(target_hex)

    for rnd in range(7, -1, -1):
        # Reverse Step 3
        state = state[-1:] + state[:-1]

        # Reverse Step 2
        for i in range(len(state) - 1, 0, -1):
            state[i] ^= state[i - 1]

        # Reverse Step 1
        for i in range(len(state)):
            state[i] = ror(state[i], (rnd + i) & 7)
            state[i] ^= (rnd * 41 + i * 17) & 0xff

    return state.decode()

if __name__ == "__main__":
    target = "5f070b54361613bca31a123e95321cff154ba64f549bb34fdc7688f10efb569aed4ccbd6ba"
    flag = recover_flag(target)
    print(f"FLAG: {flag}")
    print(f"Verification: {better_hash(flag) == target}")
