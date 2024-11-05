import requests
import os
import argparse

def download_file(url, output_dir, filename=None, timeout=10):
    """Download a file from a given URL."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Check if the request was successful
        # Save the file with a specified or default name
        file_path = os.path.join(output_dir, filename or os.path.basename(url))
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

def main(args):
    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Load the list of URLs or URL patterns
    if args.url_file:
        with open(args.url_file, "r") as f:
            urls = f.read().splitlines()
    else:
        urls = [args.url_pattern]

    # Load wordlists if provided
    fuzz1_list = load_wordlist(args.fuzz1_wordlist) if args.fuzz1_wordlist else [""]
    fuzz2_list = load_wordlist(args.fuzz2_wordlist) if args.fuzz2_wordlist else [""]

    # Download each combination of URLs with wordlists
    for url_pattern in urls:
        for fuzz1 in fuzz1_list:
            for fuzz2 in fuzz2_list:
                url = url_pattern.replace("FUZZ1", fuzz1).replace("FUZZ2", fuzz2)
                filename = f"{fuzz1}-{fuzz2}-{os.path.basename(url)}"
                download_file(url, args.output_dir, filename=filename, timeout=args.timeout)

def load_wordlist(filepath):
    """Load a wordlist from a file."""
    with open(filepath, "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download files from URL patterns with FUZZ placeholders.")
    parser.add_argument("-u", "--url-pattern", help="Base URL with FUZZ1 and/or FUZZ2 as placeholders")
    parser.add_argument("-o", "--output-dir", default="./downloaded_files", help="Directory to save downloaded files")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="Timeout for HTTP requests in seconds")
    parser.add_argument("-f1", "--fuzz1-wordlist", help="Wordlist file for FUZZ1 placeholder")
    parser.add_argument("-f2", "--fuzz2-wordlist", help="Wordlist file for FUZZ2 placeholder")
    parser.add_argument("--url-file", help="File with list of URL patterns (each on a new line)")
    
    args = parser.parse_args()
    main(args)
