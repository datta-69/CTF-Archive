# Natas Level 18 → Level 19

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 18 → 19  
- **Category:** Web Security / Session Management (Session ID Brute Force)  
- **URL:** http://natas18.natas.labs.overthewire.org  
- **Username:** `natas18`  
- **Password:** `xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP`

---

## 🎯 Objective

Find the password for **natas19** by exploiting weak **session management** and brute-forcing session IDs.

---

## 🔍 Observations

The page contains a login form.

- Any credentials entered → **Login fails**
- Message displayed:
  
> You are logged in as a regular user. Login as an admin to retrieve credentials.

### 1. Session Behavior

Using **Developer Tools → Application → Cookies**, we observe a session cookie:

**PHPSESSID**

The value appears to be a **numeric session ID**, for example:

`id="m2z9rt"`

`119`

### 2. Hypothesis
Session IDs are predictable and sequential.

Admin sessions likely exist within a small range

## 🛠️ Investigation
### 1. Understanding the Vulnerability

The application does not properly secure session IDs.

Instead of random, high-entropy values, it uses incremental numeric IDs, making them vulnerable to brute force.

### 2. Brute-Forcing Session IDs

We iterate through possible session IDs and check which one belongs to an admin using burpsuite.

We also can do this by using a script speeds up extraction.



## 💡 Discovery
### 1. Finding the Admin Session

By iterating through session IDs, we eventually find one that returns:

You are an admin.

### 2. Retrieving the Password

The page reveals the credentials for the next level:
```
natas19:tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr