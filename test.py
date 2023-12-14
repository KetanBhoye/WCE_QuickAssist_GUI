import requests

url = 'http://64.227.142.116:5055/webhook'  # Replace with your Droplet's IP and port
data = {
    "message": "Hello"  # You can customize the payload here
}

try:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Success! Response:")
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.RequestException as e:
    print("Request failed:", e)
