import socket

def solve():
    host, port = "cns-test.idlab.uantwerpen.be", 50001
    
    s = socket.create_connection((host, port), timeout=5)
    data = b""
    while b"Submit" not in data:
        chunk = s.recv(4096)
        if not chunk: break
        data += chunk
    
    lines = data.decode().splitlines()
    pending = next(lines[i+1] for i, l in enumerate(lines) if "pending" in l).strip()
    raw = bytes.fromhex(pending)
    nonce, ciphertext = raw[:8], raw[8:]
    
    fmt = '{"from":"alice","to":"bob","amount":"%s"}'
    amt_len = len(ciphertext) - len(fmt % "")
    
    if amt_len > 0:
        old_p = (fmt % ("0" * amt_len)).encode()
        new_p = '{"from":"alice","to":"bob","amount":"99999"}'.encode()
        
        payload = nonce + bytes(c ^ p1 ^ p2 for c, p1, p2 in zip(ciphertext, old_p, new_p))
        s.sendall(payload.hex().encode() + b"\n")
        
        resp = b""
        try:
            while True:
                chunk = s.recv(4096)
                if not chunk: break
                resp += chunk
        except: pass
        
        if b"cns{" in resp:
            print(resp.decode())
            s.close()
            return
    s.close()

if __name__ == "__main__":
    solve()