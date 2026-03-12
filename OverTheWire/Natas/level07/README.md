# Natas Level 7 → Level 8

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 7 → 8  
- **Category:** Web Security / Local File Inclusion (LFI)  
- **URL:** http://natas7.natas.labs.overthewire.org  
- **Username:** `natas7`  
- **Password:** `bmg8SvU1LizuWjx3y7xkNERkHxGre0GS`

---

## 🎯 Objective

Find the password for **natas8** by analyzing how the website loads pages and exploiting a **Local File Inclusion (LFI)** vulnerability.

---

## 🔍 Observations
Upon visiting the page, two navigation links are visible:

- **Home**
- **About**

Clicking these links changes the URL:


>http://natas7.natas.labs.overthewire.org/index.php?page=home

and

>http://natas7.natas.labs.overthewire.org/index.php?page=about


This suggests the application dynamically loads pages using the **`page` parameter**.

### 1. Inspecting the Source Code
Viewing the page source (`Ctrl + U`) reveals a helpful comment:
```
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```

This indicates that the password is stored on the server in the following file:


`/etc/natas_webpass/natas8`

---

## 🛠️ Investigation

### 1. Understanding the Vulnerability

The application appears to include files based on the value of the `page` parameter.  
This means the server may be executing something similar to:


`include($_GET['page']);`

If user input is not properly validated, it can lead to a **Local File Inclusion (LFI)** vulnerability.

### 2. Exploiting LFI

Since we know the location of the password file, we attempt to include it directly by modifying the URL:

>http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8

---
## 💡 Discovery
### 1. Accessing the Password File

After navigating to the modified URL, the server includes the file and displays its contents.

### 2. Retrieving the Password

The page reveals the credentials for the next level:
```php
natas8:xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q