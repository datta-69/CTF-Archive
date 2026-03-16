# Natas Level 11 → Level 12

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 11 → 12  
- **Category:** Web Security / Cryptography & Cookie Manipulation  
- **URL:** http://natas11.natas.labs.overthewire.org  
- **Username:** `natas11`  
- **Password:** `UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk`

---

## 🎯 Objective

Find the password for **natas12** by analyzing how the website encrypts and verifies **user cookies**.

---

## 🔍 Observations

When visiting the page, the following message appears:

> Cookies are protected with XOR encryption.

The page also allows the user to change the **background color**, which stores data in a cookie.

### 1. Inspecting the Cookie

Using browser **Developer Tools (`F12`) → Application → Cookies**, a cookie named:
```
data

is present.

Example cookie value:

HmYkBwozJw4
```

This value is **Base64 encoded**, meaning additional decoding may reveal useful information.

---

## 🛠️ Investigation

### 1. Inspecting the Source Code

Viewing the page source reveals a link:

>index-source.html


Opening it exposes the PHP code used for cookie encryption.

The important part of the code is:

```
function xor_encrypt($in) {
    $key = "<censored>";
    $text = $in;
    $outText = '';

    for($i=0; $i<strlen($text); $i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```
### 2. Understanding the Process
The cookie is processed in the following order:
```
Data is stored as JSON

JSON is XOR encrypted

Result is Base64 encoded
```
Example structure:
```
{"showpassword":"no","bgcolor":"#ffffff"}
The goal is to change:

"showpassword":"no"
to

"showpassword":"yes"
```
### 3. Recovering the XOR Key
Steps:

`Base64 decode the cookie.`

`XOR it with the known plaintext JSON structure.`

`This reveals the XOR key used by the application.`

`Once the key is recovered, we can create our own encrypted cookie.`

### 4. Crafting the Malicious Cookie
Create a modified JSON payload:
```
{"showpassword":"yes","bgcolor":"#ffffff"}
```
Encrypt it using the discovered `XOR key and Base64` encode the result.

You can also do that by making a simple **python script**.

Replace the `data cookie` with this new value.



## 💡 Discovery
### 1. Reloading the Page
After replacing the **cookie** and refreshing the page, the application now believes the user is authorized to see the password.

### 2. Retrieving the Password
The page reveals the credentials for the next level:

```
natas12:yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB