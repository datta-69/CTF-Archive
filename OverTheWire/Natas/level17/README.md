## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 17 → 18  
- **Category:** Web Security / Time-Based Blind SQL Injection  
- **URL:** http://natas17.natas.labs.overthewire.org  
- **Username:** `natas17`  
- **Password:** `EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC`

---

## 🎯 Objective

Find the password for **natas18** by exploiting a **Time-Based Blind SQL Injection vulnerability**.

---

## 🔍 Observations

The page contains a search field similar to the previous level.

However, unlike Natas15:
- No visible output (no "user exists" message)
- No direct feedback from the query

⚠️ This indicates a **Time-Based Blind SQL Injection**, where responses are inferred using **delays**.

---

## 🛠️ Investigation

### 1. Understanding the Vulnerability

The backend likely executes a query such as:


> * FROM users WHERE username="$input";

We cannot see query results, but we can introduce delays using SQL functions like:

>SLEEP(5)
### 2. Confirming Injection

Test payload:

>natas18" AND SLEEP(5) --

If the response is delayed → SQL injection confirmed.

### 3. Extracting the Password

We extract the password character by character using timing.

Step 1: Check Character

Example:

>natas18" AND IF(SUBSTRING(password,1,1)="a", SLEEP(5), 0) --
```
If delay occurs → correct character
If no delay → incorrect character
```
### 4. Automating the Attack

Using a script speeds up extraction.


## 💡 Discovery
### 1. Extracting Full Password

Using response delay, we reconstruct the password character by character.

### 2. Final Result
```sql

natas18: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP