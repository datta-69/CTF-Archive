# Natas Level 15 → Level 16

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 15 → 16  
- **Category:** Web Security / Blind SQL Injection  
- **URL:** http://natas15.natas.labs.overthewire.org  
- **Username:** `natas15`  
- **Password:** `SdqIqBsFcz3yotlNYErZSZwblkm0lrvx`

---

## 🎯 Objective

Find the password for **natas16** by exploiting a **Blind SQL Injection vulnerability**.

---

## 🔍 Observations

The page contains a search field asking for a username.

When submitting a valid username:

> This user exists.

When invalid:

> This user doesn't exist.

⚠️ The application does **not display query results**, only a **true/false response**, indicating a **Blind SQL Injection vulnerability**.

---

## 🛠️ Investigation

### 1. Understanding the Vulnerability

The backend likely runs a query such as:

```sql
SELECT * FROM users WHERE username="$input";
```
Since input is not sanitized, we can inject SQL conditions.

### 2. Confirming SQL Injection

Test payload:
```
natas16" AND "1"="1

→ Response: User exists

natas16" AND "1"="2

→ Response: User doesn't exist
```
**✅ This confirms Blind SQL Injection.**

### 3. Extracting the Password

We extract the password character by character using conditions.

Step 1: Determine Length
>natas16" AND LENGTH(password)=32 --

If response is **true** → correct length.

Step 2: Extract Characters

We use:

>natas16" AND SUBSTRING(password,1,1)="a

Repeat for each position and character until the full password is recovered.

### 4. Automation (Recommended)

Using a script speeds up extraction.

---

## 💡 Discovery
### 1. Extracting Full Password

By iterating through each character position, we reconstruct the full password.

### 2. Retrieving the Password

Final result:
```
natas16:hPkjKYviLQctEW33QmuXL6eDVfMW4sGo