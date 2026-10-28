import json
import hashlib
import socket
from datetime import datetime, timezone

def canonicalize(payment):
    return json.dumps(
        payment,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")

def solve():
    # Use current time to satisfy "within the previous minute" requirement
    now = datetime.now(timezone.utc).isoformat().split(".")[0] + "Z"
    
    base_payment = {
        "from_account": "SIM-ALICE",
        "to_account": "SIM-BOB",
        "amount": 10,
        "currency": "EUR",
        "timestamp": now
    }

    seen = {}
    print(f"Searching for collision with timestamp {now}...")
    
    for i in range(1000000):
        ref = str(i)
        p = base_payment.copy()
        p["reference"] = ref
        
        c = canonicalize(p)
        h = hashlib.sha256(c).digest()[:4]
        
        if h in seen:
            p1 = seen[h]
            p2 = p
            print(f"Collision found at i={i}!")
            print(f"P1: {json.dumps(p1)}")
            print(f"P2: {json.dumps(p2)}")
            print(f"Fingerprint: {h.hex()}")
            
            # Send to server
            host, port = "cns-test.idlab.uantwerpen.be", 50003
            print(f"Connecting to {host}:{port}...")
            s = socket.create_connection((host, port), timeout=10)
            
            # The server might send some intro text first
            s.sendall(canonicalize(p1) + b"\n")
            s.sendall(canonicalize(p2) + b"\n")
            
            resp = b""
            try:
                while True:
                    chunk = s.recv(4096)
                    if not chunk: break
                    resp += chunk
            except socket.timeout:
                pass
            except Exception as e:
                print(f"Error receiving: {e}")
            
            output = resp.decode()
            print(output)
            s.close()
            return
        
        seen[h] = p

if __name__ == "__main__":
    solve()
