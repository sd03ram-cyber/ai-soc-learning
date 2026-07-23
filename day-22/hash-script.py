#!/usr/bin/env python3
"""
File Hash Computer — MD5, SHA1, SHA256.
Useful for malware analysis: compute hash, look it up on VirusTotal.
Usage: python3 hash-script.py <file_path>
Example: python3 hash-script.py malware.exe
"""

import hashlib
import sys
import os


def compute_hashes(filepath):
    """Compute MD5, SHA1, SHA256 for a file."""
    if not os.path.isfile(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    sha256_hash = hashlib.sha256()
    
    # Read file in chunks (efficient for large files)
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):  # Python 3.8+ walrus operator
            md5_hash.update(chunk)
            sha1_hash.update(chunk)
            sha256_hash.update(chunk)
    
    return {
        'md5': md5_hash.hexdigest(),
        'sha1': sha1_hash.hexdigest(),
        'sha256': sha256_hash.hexdigest(),
    }


def print_hashes(filepath, hashes):
    """Print hashes in a readable format."""
    print(f"\n[File: {os.path.basename(filepath)}]")
    print(f"  MD5:    {hashes['md5']}")
    print(f"  SHA1:   {hashes['sha1']}")
    print(f"  SHA256: {hashes['sha256']}")
    print()
    print("Next step: Look up the SHA256 hash on VirusTotal.com")
    print("  → If >45/60 vendors flag it, it's malware")
    print("  → If 0 vendors flag it, it's likely clean or novel malware")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hash-script.py <file_path>")
        print("Example: python3 hash-script.py malware.exe")
        sys.exit(1)
    
    filepath = sys.argv[1]
    hashes = compute_hashes(filepath)
    print_hashes(filepath, hashes)
