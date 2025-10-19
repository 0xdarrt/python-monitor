import requests
import sys

URL = "https://google.com"

try:
	response = requests.get(URL, timout=5)
	if response.status_code == 200:
        print(f"[UP] {URL} is online!")
    	else:
        print(f"[DOWN] {URL} returned status code: {response.status_code}")
except requests.ConnectionError:
    print(f"[DOWN] {URL} failed to connect.")
except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}")
    sys.exit(1) # Exit with an error code

