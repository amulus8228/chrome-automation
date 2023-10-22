import requests
import time

while True:
    try:
        response = requests.get("http://www.google.com")
        # You can add code here to process the response if needed.
        print("Request successful")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    
    time.sleep(10)
