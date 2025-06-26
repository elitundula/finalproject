#SSL Verification Errors in the Requests Library
import requests

url = "https://expired.badssl.com/"

# This will cause an SSL error because the certificate is expired
try:
    print("Trying with SSL verification (default)...")
    response = requests.get(url)
    print("Success!")
    print(response.text[:200]) 
except requests.exceptions.SSLError as e:
    print("SSL Error occurred:")
    print(e)

# 🟡 This bypasses SSL verification
print("\nTrying with SSL verification turned off...")
response = requests.get(url, verify=False)
print("Request succeeded (insecure):")
print(response.text[:200])
