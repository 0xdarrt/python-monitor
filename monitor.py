import requests
import sys
import argparse  # New: For parsing command-line arguments
import logging   # New: For writing to a log file

def setup_logging(log_file):
    """Configures the logging system."""
    # Set the logging level and format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),  # Log to a file
            logging.StreamHandler(sys.stdout) # Also log to the console
        ]
    )

def check_url(url):
    """Checks a single URL and logs its status."""
    try:
        url = url.strip()
        if not url.startswith(('http://', 'https://')):
            url = f'https://{url}' # Add https:// if missing
            
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            logging.info(f"[UP] {url} is online!")
        else:
            logging.warning(f"[DOWN] {url} returned status code: {response.status_code}")
            
    except requests.ConnectionError:
        logging.error(f"[DOWN] {url} failed to connect.")
    except Exception as e:
        logging.error(f"An unexpected error occurred with {url}: {e}")

# --- Main part of the script ---
if __name__ == "__main__":
    # 1. Set up the argument parser
    parser = argparse.ArgumentParser(description="Website Uptime Monitor")
    parser.add_argument(
        '-f', '--file',  # The long and short name for the argument
        type=str,
        required=True, # This argument is no longer optional
        help="Path to the file containing URLs to check (one per line)."
    )
    parser.add_argument(
        '-l', '--log',
        type=str,
        default='monitor.log', # If no log file is given, use 'monitor.log'
        help="Path to the output log file."
    )
    
    args = parser.parse_args()
    
    # 2. Set up logging
    setup_logging(args.log)
    
    # 3. Read the file and run the checks
    logging.info(f"Starting monitor run. Reading from: {args.file}")
    try:
        with open(args.file, 'r') as file:
            urls = file.readlines()
            
        if not urls:
            logging.error(f"Error: {args.file} is empty.")
            sys.exit(1)

        for url in urls:
            check_url(url)
        
        logging.info("Monitor run finished.")

    except FileNotFoundError:
        logging.error(f"Error: Could not find the file named {args.file}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error: Failed to read file: {e}")
        sys.exit(1)
