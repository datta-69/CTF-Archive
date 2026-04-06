# Natas Level 23 → Level 24

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 23 → 24  
- **Category:** Web Security / PHP Type Juggling  
- **URL:** http://natas23.natas.labs.overthewire.org  
- **Username:** `natas23`  
- **Password:** `3xk7QpL9mN2aV5s8D1cR4tY6wZ0bFhUe`

---

## 🎯 Objective

Find the password for **natas24** by exploiting a **PHP type juggling vulnerability**.

---

## 🔍 Observations

The page contains a simple input field for a password.

When incorrect input is provided, the response is:

> Wrong password.

### 1. Inspecting the Source Code

Viewing the page source (`Ctrl + U`) reveals the following PHP logic:

```php
if (strstr($_GET["passwd"], "iloveyou") && ($_GET["passwd"] > 10)) {
    echo "Access granted. The password for natas24 is <censored>";
} else {
    echo "Wrong password";
}
```
---
## 🛠️ Investigation
### 1. Understanding the Conditions

The application checks two conditions:

Input must contain the string:
**iloveyou**

Input must be greater than:
**10**
### 2. Identifying the Vulnerability

PHP performs type juggling when comparing different data types.

When a string is compared to a number:
~~~
PHP attempts to convert the string to a number
If the string starts with non-numeric characters → it becomes 0
~~~

Example:

>"iloveyou" > 10   // false (treated as 0 > 10)

### 3. Crafting the Payload

We need:

A string that contains **"iloveyou"**
Starts with a numeric value greater than **10**.

Payload:
```
11iloveyou
```
Explanation:
~~~
**strstr() → finds "iloveyou" ✅
"11iloveyou" → converted to integer 11 ✅
11 > 10 → TRUE ✅**
~~~
### 4. Sending the Request
>http://natas23.natas.labs.overthewire.org/?passwd=11iloveyou

---
## 💡 Discovery
### 1. Condition Bypass

The crafted input satisfies both conditions due to PHP type juggling.

### 2. Retrieving the Password

The page reveals:

natas24:MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd