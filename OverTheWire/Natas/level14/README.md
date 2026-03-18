# Natas Level 14 → Level 15

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 14 → 15  
- **Category:** Web Security / SQL Injection  
- **URL:** http://natas14.natas.labs.overthewire.org  
- **Username:** `natas14`  
- **Password:** `z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ`

---

## 🎯 Objective

Find the password for **natas15** by exploiting a **SQL Injection vulnerability** in the login form.

---

## 🔍 Observations

The page contains a **login form** asking for:

- Username  
- Password  

When invalid credentials are entered, the response is:

> Access denied.

This suggests that the application is validating input against a database.

---

## 🛠️ Investigation

### 1. Understanding the Vulnerability

The application likely constructs a SQL query similar to:

```sql
SELECT * FROM users WHERE username="$username" AND password="$password";
```

If user input is not sanitized, it becomes vulnerable to SQL Injection.

### 2. Testing for Injection

Try the following payload in the login fields:

Username:

" OR 1=1 -- 

Password:

anything
### 3. Explanation of Payload
```
" OR 1=1 -- 

" → Closes the existing string

OR 1=1 → Always evaluates to TRUE

-- → Comments out the rest of the query
```
This transforms the query into:
```
SELECT * FROM users WHERE username="" OR 1=1 -- " AND password="anything";
```
Since `1=1` is always true, authentication is bypassed.

---
## 💡 Discovery
### 1. Login Bypass

After submitting the payload, the application grants access without valid credentials.

### 2. Retrieving the Password

The page reveals the credentials for the next level:
```
natas15:SdqIqBsFcz3yotlNYErZSZwblkm0lrvx
