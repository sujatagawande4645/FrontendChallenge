import requests

url = "http://127.0.0.1:5000/upload"
files = {'file': open(r'C:\Users\Alpha\Desktop\upload.txt', 'rb')}

try:
    response = requests.post(url, files=files)
    response.raise_for_status()  # Raise an error for 4xx and 5xx status codes
    print(response.json())
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)
