import requests
import sys

# Define a function to check a single URL
def check_url(url):
    """Checks a single URL and prints its status."""
    try:
        # We strip() to remove any newline characters
        url = url.strip() 
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"[UP] {url} is online!")
        else:
            print(f"[DOWN] {url} returned status code: {response.status_code}")
            
    except requests.ConnectionError:
        print(f"[DOWN] {url} failed to connect.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred with {url}: {e}")

# --- Main part of the script ---
SITES_FILE = "sites.txt"

try:
    # 'with open' safely opens and closes the file
    with open(SITES_FILE, 'r') as file:
        # .readlines() gives us a list of all lines
        urls = file.readlines() 
        
    if not urls:
        print(f"Error: {SITES_FILE} is empty.")
        sys.exit(1)

    # Loop through the list of URLs and check each one
    for url in urls:
        check_url(url)

except FileNotFoundError:
    print(f"Error: Could not find the file named {SITES_FILE}")
    sys.exit(1)
except Exception as e:
    print(f"Error: Failed to read file: {e}")
    sys.exit(1)
