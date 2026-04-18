# Natas Level 24 → Level 25

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 24 → 25  
- **Category:** Web Security / PHP Input Validation Bypass  
- **URL:** http://natas24.natas.labs.overthewire.org  
- **Username:** `natas24`
- **Password:** `MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd`

---

## 🎯 Objective

Find the password for **natas25** by exploiting improper **input validation** in PHP.

---

## 🔍 Observations

The page asks for a password through a GET parameter:

``` id="user"```

>?passwd=

When a normal value is supplied, the page returns:

Wrong password.

### 1. Inspecting the Source Code

Viewing the page source (Ctrl + U) reveals logic similar to:
```
if(array_key_exists("passwd", $_REQUEST)) {
    if(!strcmp($_REQUEST["passwd"], "<secret>")) {
        echo "Access granted...";
    } else {
        echo "Wrong password";
    }
}
```
---
## 🛠️ Investigation
### 1. Understanding the Vulnerability

The application uses:

>strcmp()

to compare the user input with the secret password.

Normally:
```
strcmp("abc","abc") → 0
strcmp("abc","xyz") → non-zero
```
Then the result is negated:

>!strcmp(...)

So if strcmp() returns 0, access is granted.

### 2. Identifying the Bug

If passwd is sent as an array instead of a string:

>?passwd[]=test

Then strcmp() receives an invalid type.

In older PHP behavior, this may generate a warning and return NULL.

Then:

**!NULL**

becomes:

**TRUE**

✅ Authentication bypass achieved.

### 3. Sending the Payload

Use the following URL:

>http://natas24.natas.labs.overthewire.org/?passwd[]=test
---
## 💡 Discovery
### 1. Bypassing Authentication

Because of improper type handling, the password check succeeds without knowing the real password.

### 2. Retrieving the Password

The page reveals:
```
natas25: ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws