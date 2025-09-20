import requests

print(r""" 
  _____   __    __   ______    ________   ______       ____       ____    __   ___  
 / ____\  ) )  ( (  (_   _ \  (___  ___) (   __ \     (    )     / ___)  () ) / __) 
( (___   ( (    ) )   ) (_) )     ) )     ) (__) )    / /\ \    / /      ( (_/ /    
 \___ \   ) )  ( (    \   _/     ( (     (    __/    ( (__) )  ( (       ()   (     
     ) ) ( (    ) )   /  _ \      ) )     ) \ \  _    )    (   ( (       () /\ \    
 ___/ /   ) \__/ (   _) (_) )    ( (     ( ( \ \_))  /  /\  \   \ \___   ( (  \ \   
/____/    \______/  (______/     /__\     )_) \__/  /__(  )__\   \____)  ()_)  \_\  
                                                                                    
 """)

domain = input("Enter domain name: ")
file = open(input("Select wordlist: "),'r')
content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        requests.get(url1)
        print(f"Discovered URL: {url1}")
        requests.get(url2)
        print(f"Discovered URL: {url2}")

    except Exception as err:
        print(f"An error occur as {err}")