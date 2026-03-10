# Natas Level 2 → Level 3

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 2 → 3  
- **Category:** Web Security / Directory Indexing  
- **URL:** http://natas2.natas.labs.overthewire.org  
- **Username:** `natas2`  
- **Password:** `TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI`

---

## 🎯 Objective

Find the password for **natas3**.

---

## 🔍 Observations

Upon logging in, the page displays:
> "There is nothing on this page."

- No text is visible.
- Viewing the source code reveals an image tag: `<img src="files/pixel.png">`.
- This hints at a directory named `/files/` existing on the server.

---

## 🛠️ Investigation

1. **Inspect Source:** I viewed the page source (`Ctrl+U`) and saw the subdirectory `/files/`.
2. **Directory Traversal:** I attempted to access the directory directly by navigating to:
   `http://natas2.natas.labs.overthewire.org/files/`
3. **Directory Indexing:** The server has "Directory Indexing" enabled, which lists all files inside that folder.

---

## 💡 Discovery

Inside the `/files/` directory, there are two files:
- `pixel.png`
- `users.txt`

Opening `users.txt` reveals the following content:
```text
# This file contains passwords for users of natas
# 
# natas:password
# ...
natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH