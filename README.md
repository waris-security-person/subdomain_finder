----------
Subdomain Finder
----------------

A simple Python tool to discover valid subdomains of a given domain using a provided wordlist.
It attempts both HTTP and HTTPS requests to check if the subdomains are live.

Features:
- Brute-force subdomain discovery using a wordlist
- Checks both HTTP and HTTPS
- Prints discovered live URLs in real time
- Simple and easy to use

Requirements:
- Python 3.x
- requests library

Install requests with:
    pip install requests

Usage:
1. Save the script (e.g., subdomain_finder.py).
2. Run the script:
    python subdomain_finder.py
3. Enter the target domain name when prompted.
4. Provide the path to a wordlist file when prompted.

Example:
    Enter domain name: example.com
    Select wordlist: wordlist.txt

Example Output:
  _____   __    __   ______    ________   ______       ____       ____    __   ___  
 / ____\  ) )  ( (  (_   _ \  (___  ___) (   __ \     (    )     / ___)  () ) / __) 
( (___   ( (    ) )   ) (_) )     ) )     ) (__) )    / /\ \    / /      ( (_/ /    
 \___ \   ) )  ( (    \   _/     ( (     (    __/    ( (__) )  ( (       ()   (     
     ) ) ( (    ) )   /  _ \      ) )     ) \ \  _    )    (   ( (       () /\ \    
 ___/ /   ) \__/ (   _) (_) )    ( (     ( ( \ \_))  /  /\  \   \ \___   ( (  \ \   
/____/    \______/  (______/     /__\     )_) \__/  /__(  )__\   \____)  ()_)  \_\  

Enter domain name: example.com
Select wordlist: wordlist.txt
Discovered URL: http://test.example.com
Discovered URL: https://test.example.com

Notes:
- This tool only checks whether the subdomains respond to HTTP/HTTPS requests — it does not perform DNS enumeration.
- Some subdomains may block requests or require authentication.
- Use responsibly and only on domains you are authorized to test.

Disclaimer:
This tool is intended for educational and authorized penetration testing purposes only.
The author is not responsible for misuse or illegal activities conducted with this script.
