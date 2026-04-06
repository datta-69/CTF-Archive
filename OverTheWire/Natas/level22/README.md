# Natas Level 22 → Level 23

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 22 → 23  
- **Category:** Web Security / HTTP Redirect Bypass  
- **URL:** http://natas22.natas.labs.overthewire.org  
- **Username:** `natas22`  
- **Password:** `9bUZ0dKpX2hF8sLw6Q3mN7rT1yC4eV5Z`

---

## 🎯 Objective

Find the password for **natas23** by bypassing an **HTTP redirect**.

---

## 🔍 Observations

Visiting the page normally does not show any useful information.

However, inspecting the request behavior reveals that the server performs an **HTTP redirect**.

### 1. Testing with Parameters

Appending a parameter:

``` id="revelio"
http://natas22.natas.labs.overthewire.org/?revelio
```
Triggers a redirect response.

### 2. Behavior Analysis

The application sends a `redirect` header:

Location: /
``` id="revelio"
http://natas22.natas.labs.overthewire.org/
```
This prevents the browser from displaying the actual content returned by the server.

---

## 🛠️ Investigation

### 1. Understanding the Vulnerability

The server executes something like:

```php
if(isset($_GET['revelio'])) {
    header("Location: /");
}
```
However, execution does not stop after the `redirect`.

The server still processes and outputs sensitive data, but the browser never displays it due to the redirect.

### 2. Bypassing the Redirect

We need to prevent automatic redirection.

- **Method 1**: Using curl
```
curl -u natas22:d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz \
http://natas22.natas.labs.overthewire.org/?revelio

```
- **Method 2**: Using Burp Suite
Intercept the request
Send it to Repeater
Disable *`redirect`* following
View raw response.

---
## 💡 Discovery
### 1. Capturing the Response

By preventing the **redirect**, we can view the actual server response.

### 2. Retrieving the Password

The response contains:
```
natas23:dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs
```