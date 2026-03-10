# Natas Level 0 → Level 1

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 0 → 1  
- **Category:** Web Security / Source Code Disclosure  
- **URL:** http://natas0.natas.labs.overthewire.org  
- **Username:** `natas0`  
- **Password:** `natas0`

---

## 🎯 Objective

Find the password for **natas1**.

---

## 🔍 Observations

After logging in with the provided credentials, the webpage shows:

> "You can find the password for the next level on this page."

However, the password is **not visible** on the page. This indicates it might be **hidden in the page source**.

---

## 🛠️ Investigation

Since the password is not visible in the rendered page, inspect the HTML source:

1. Right-click anywhere on the page → **View Page Source**  
2. Or press `Ctrl + U` (Windows/Linux) or `Cmd + Option + U` (Mac)  

Look for **comments, hidden text, or unusual elements**.

---

## 💡 Discovery

Inside the HTML source code, the password is found inside an **HTML comment** at the bottom:

```html
<!--The password for natas1 is 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq -->