import socket
import hashlib

def solve():
    host, port = "cns-test.idlab.uantwerpen.be", 50006
    s = socket.create_connection((host, port), timeout=5)
    
    data = b""
    while b"CURRENT CODE:" not in data:
        chunk = s.recv(4096)
        if not chunk: break
        data += chunk
    
    lines = data.decode().splitlines()
    current_code = ""
    for line in lines:
        if "CURRENT CODE:" in line:
            current_code = line.split(":")[-1].strip()
            break
            
    if not current_code:
        print("Failed to find current code")
        return

    print(f"Current code: {current_code}")
    
    # Calculate next code: SHA-256 of the current code bytes
    next_code = hashlib.sha256(bytes.fromhex(current_code)).hexdigest()
    print(f"Predicted next code: {next_code}")
    
    # Send prediction
    s.sendall(next_code.encode() + b"\n")
    
    # Receive response (flag)
    resp = b""
    try:
        while True:
            chunk = s.recv(4096)
            if not chunk: break
            resp += chunk
    except socket.timeout:
        pass
        
    print(resp.decode())
    s.close()

if __name__ == "__main__":
    solve()
