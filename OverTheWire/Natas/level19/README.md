# Natas Level 19 → Level 20

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 19 → 20  
- **Category:** Web Security / Session Management (Encoded Session IDs)  
- **URL:** http://natas19.natas.labs.overthewire.org  
- **Username:** `natas19`  
- **Password:** `tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr`

---

## 🎯 Objective

Find the password for **natas20** by exploiting weak **session management with encoded session IDs**.

---

## 🔍 Observations

The page contains a login form similar to the previous level.

- Any login attempt → regular user
- Goal: become **admin**

### 1. Inspecting Cookies

Using **Developer Tools → Application → Cookies**, we observe:


```PHPSESSID```

Example value:
```
username=1 or password=admin
PHPSESSID = 312d61646d696e
```
This looks like a hex-encoded string, not a simple number.

## 🛠️ Investigation
### 1. Decoding the Session ID

Convert the hex value:
```
312d61646d696e to 1-admin
```
This reveals the session format:

`<session_id>-<username>`

### 2. Understanding the Vulnerability

The application encodes **session** data as:

>sessionID-username

Then converts it into hex format.

This means we can forge our own session.
### 3. Brute-Forcing Session IDs

We iterate through possible session IDs and check which one belongs to an admin using burpsuite.

We also can do this by using a script speeds up extraction.

### 4. Crafting an Admin Session

We create:

>281-admin

Convert to hex:

>3238312d61646d696e

### 5. Setting the Cookie

Replace the PHPSESSID cookie with:

>3238312d61646d696e

Refresh the page.

---
## 💡 Discovery
### 1. Admin Access

After modifying the cookie, the server recognizes us as:

You are an admin.

### 2. Retrieving the Password

The page reveals the credentials for the next level:
```
natas20:p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw
