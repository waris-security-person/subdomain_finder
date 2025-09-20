#!/usr/bin/env python3
import socket
import requests
import sys

BANNER = r"""
  _____   __    __   ______    ________   ______       ____       ____    __   ___  
 / ____\  ) )  ( (  (_   _ \  (___  ___) (   __ \     (    )     / ___)  () ) / __) 
( (___   ( (    ) )   ) (_) )     ) )     ) (__) )    / /\ \    / /      ( (_/ /    
 \___ \   ) )  ( (    \   _/     ( (     (    __/    ( (__) )  ( (       ()   (     
     ) ) ( (    ) )   /  _ \      ) )     ) \ \  _    )    (   ( (       () /\ \    
 ___/ /   ) \__/ (   _) (_) )    ( (     ( ( \ \_))  /  /\  \   \ \___   ( (  \ \   
/____/    \______/  (______/     /__\     )_) \__/  /__(  )__\   \____)  ()_)  \_\  
"""

print(BANNER)

domain = input("Enter domain name (example: example.com): ").strip().rstrip(".")
wordlist_path = input("Select wordlist (example: list.txt): ").strip()

# Basic validation
if not domain:
    print("No domain provided. Exiting.")
    sys.exit(1)

try:
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        subdomains = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"Wordlist file not found: {wordlist_path}")
    sys.exit(1)

# Optional: set a simple User-Agent
HEADERS = {"User-Agent": "SubDomainFinder/1.0 (+https://example.com)"}
TIMEOUT = 5  # seconds

for sub in subdomains:
    hostname = f"{sub}.{domain}"
    try:
        # DNS check first
        ip = socket.gethostbyname(hostname)
        print(f"[DNS] Resolved {hostname} -> {ip}")
    except socket.gaierror:
        # DNS lookup failed — skip HTTP checks
        print(f"[DNS] Not found: {hostname}")
        continue

    # Try HTTP and HTTPS
    for scheme in ("http", "https"):
        url = f"{scheme}://{hostname}"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
            print(f"[FOUND] {url} -> {resp.status_code} ({len(resp.content)} bytes)")
        except requests.exceptions.RequestException as e:
            # Any requests-related error (timeout, SSL error, connection refused, etc.)
            print(f"[ERROR] {url} -> {e}")
