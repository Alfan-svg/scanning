import requests

def load_wordlist(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Wordlist file '{file_path}' not found.")
        exit()

def scan_directories(domain, wordlist):
    print(f"\nScanning directories/files on: {domain}\n")
    found_paths = []

    for word in wordlist:
        url = f"{domain}/{word}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[FOUND] {url}")
                found_paths.append(url)
            elif response.status_code in [301, 302]:
                print(f"[REDIRECT] {url} --> {response.headers.get('Location')}")
            else:
                print(f"[{response.status_code}] {url}")
        except requests.RequestException:
            print(f"[ERROR] Failed to access {url}")
    
    return found_paths

def main():
    print("=== Directory & File Enumerator ===")
    domain = input("Enter domain (e.g., https://example.com): ").strip()

    if not domain.startswith("http"):
        domain = "http://" + domain  # Default to HTTP if no scheme provided

    wordlist = load_wordlist("wordlist.txt")
    found = scan_directories(domain, wordlist)

    print("\n=== Scan Finished ===")
    if found:
        print("Accessible directories/files found:")
        for path in found:
            print(f"- {path}")
    else:
        print("No accessible directories/files found in wordlist.")

if __name__ == "__main__":
    main()
