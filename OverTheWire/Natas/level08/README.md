# Natas Level 8 → Level 9

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 8 → 9  
- **Category:** Web Security / Encoding & Source Code Analysis  
- **URL:** http://natas8.natas.labs.overthewire.org  
- **Username:** `natas8`  
- **Password:** `xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q`

---

## 🎯 Objective

Find the password for **natas9** by analyzing the website’s source code and decoding the hidden **secret value** used for authentication.

---

## 🔍 Observations
Upon visiting the page, an input form appears asking for a **secret**.

When a value is submitted, the application responds with:

> Wrong secret.

This suggests the application is comparing the input against a **hidden encoded secret**.

### 1. Inspecting the Source Code
Viewing the page source (`Ctrl + U`) reveals a link to the server-side code:

> `index-source.html`

Opening this file exposes the PHP code used by the application.

---

## 🛠️ Investigation

### 1. Reviewing the Application Code

Inside `index-source.html`, the following PHP snippet appears:

> $encodedSecret = "3d3d516343746d4d6d6c315669563362";

The code later performs several decoding steps:
```
$secret = base64_decode(strrev(hex2bin($encodedSecret)));
```
### 2. Understanding the Decoding Process

The encoded **secret** undergoes three transformations:
```
Hexadecimal decoding (hex2bin)

String reversal (strrev)

Base64 decoding (base64_decode)
```
To obtain the original **secret**, we reverse these steps.

### 3. Decoding the Secret

***Step 1 — Convert Hex to ASCII***

>3d3d516343746d4d6d6c315669563362  →  ==QcCtmMml1ViV3b

***Step 2 — Reverse the String***

>b3ViV1lmMmtCcQ==

***Step 3 — Base64 Decode***

>oubWYf2kBq
---
## 💡 Discovery
### 1. Submitting the Decoded **Secret**

Return to the main page and submit:

>oubWYf2kBq

### 2. Retrieving the Password

After submitting the correct secret, the page reveals the credentials for the next level:
```php
natas9:ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t