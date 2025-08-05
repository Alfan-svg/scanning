from itertools import product

def generate_wordlist(basenames, prefixes, suffixes, extensions, output_file):
    wordlist = set()

    for base in basenames:
        # Kombinasi Prefix + Base + Suffix + Ext
        for pre, suf, ext in product(prefixes, suffixes, extensions):
            word = f"{pre}{base}{suf}{ext}".strip()
            wordlist.add(word)

    # Simpan ke file
    with open(output_file, 'w') as f:
        for word in sorted(wordlist):
            f.write(f"{word}\n")

    print(f"[+] Wordlist berhasil dibuat: {output_file}")
    print(f"Total Entries: {len(wordlist)}")

if __name__ == "__main__":
    # Base names yang umum
    basenames = [
        "admin", "login", "dashboard", "config", "backup", "db", "test", "dev", "user", "hidden", "private"
    ]

    # Variasi prefix dan suffix
    prefixes = ["", "old_", "new_", "dev_", "backup_", "test_", "hidden_"]
    suffixes = ["", "_old", "_2023", "_v1", "_backup", "_dev"]
    extensions = ["", ".php", ".html", ".bak", ".zip", ".tar.gz", ".sql", ".txt"]

    # Generate Wordlist
    generate_wordlist(basenames, prefixes, suffixes, extensions, "custom_wordlist.txt")
