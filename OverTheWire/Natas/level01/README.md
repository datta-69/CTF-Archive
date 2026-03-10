# Natas Level 1 → Level 2

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 1 → 2  
- **Category:** Web Security / Source Code Disclosure  
- **URL:** http://natas1.natas.labs.overthewire.org  
- **Username:** `natas1`  
- **Password:** `0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq`

---

## 🎯 Objective

Find the password for **natas2**.

---

## 🔍 Observations

Upon logging in, the page says:

> "You can find the password for the next level in the source code of this page."

This clearly hints that the **password is hidden in the page source**.

---

## 🛠️ Investigation

Since the page mentions “source code,” inspect it:

1. Right-click anywhere on the page → **View Page Source**  
2. Or press `Ctrl + U` (Windows/Linux) or `Cmd + Option + U` (Mac)

Look for **HTML comments** or any hidden text.

---

## 💡 Discovery

Inside the HTML source code, the password is found in an **HTML comment**:

```html
<!--The password for natas2 is TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI -->