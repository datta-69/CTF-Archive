# Natas Level 6 → Level 7

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 6 → 7  
- **Category:** Web Security / Source Code Disclosure  
- **URL:** http://natas6.natas.labs.overthewire.org  
- **Username:** `natas6`  
- **Password:** `0RoJwHdSKWFTYR5WuiAewauSuNaBXned`

---

## 🎯 Objective

Find the password for **natas7** by analyzing the website’s source code and identifying how the application validates user input.

---

## 🔍 Observations
Upon visiting the page, a simple input form is displayed asking for a **secret**.

When a value is entered, the page responds with:

> Wrong secret.

This suggests that the application is checking the submitted value against a **hidden secret stored somewhere on the server**.

### 1. Inspecting the Source Code
The first step is to inspect the page source (`Ctrl + U`).  
A link to the PHP source file is visible:

> `index-source.html`

Opening this file reveals the server-side code responsible for validating the input.

---

## 🛠️ Investigation

### 1. Reviewing the Application Code

Inside `index-source.html`, the following code snippet appears:
```
<?
include "includes/secret.inc";

if(array_key_exists("submit", $_POST)) {
    if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
}
?>
```
**2. Understanding the Code**

The application includes a file:

`includes/secret.inc`

This file likely contains the value of the secret used for validation.

**3. Accessing the Included File**

Since the directory structure is not protected, we can directly access the file by navigating to:

>http://natas6.natas.labs.overthewire.org/includes/secret.inc

Opening the file reveals:

```$secret = "FOEIUWGHFEEUHOFUOIU";```

---

## 💡 Discovery
### 1. Submitting the Correct Secret

Return to the main page and submit the discovered secret:

>`FOEIUWGHFEEUHOFUOIU`
### 2. Retrieving the Password

After submitting the correct secret, the page reveals the credentials for the next level:
```php
Access granted. The password for natas7 is bmg8SvU1LizuWjx3y7xkNERkHxGre0GS