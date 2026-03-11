# Natas Level 4 → Level 5

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 4 → 5  
- **Category:** Web Security / HTTP Referer Header  
- **URL:** http://natas4.natas.labs.overthewire.org  
- **Username:** `natas4`  
- **Password:** `QryZXc2e0zahULdHrtHxzyYkj59kUxLQ`

---

## 🎯 Objective

Find the password for **natas5** by bypassing the access restriction based on the **HTTP Referer header**.

---

## 🔍 Observations
Upon visiting the page, the following message is displayed:

> Access disallowed. You are visiting from "" while authorized users should come only from  
> http://natas5.natas.labs.overthewire.org/

### 1. Understanding the Error Message
The message indicates that the server expects visitors to arrive from a specific page:
> `http://natas5.natas.labs.overthewire.org/`

This means the server is checking the **HTTP Referer header** to verify the source of the request.

### 2. What is the Referer Header?

The **Referer header** is part of the `HTTP request` and indicates the URL of the page that made the request.

Example request header:


Referer: http://natas5.natas.labs.overthewire.org/


However, since HTTP headers are **controlled by the client**, they can easily be modified by attackers.

---

## 🛠️ Investigation

### 1. Inspecting the Request
Using browser developer tools or an intercepting proxy (like Burp Suite), we can inspect the `HTTP request` sent to the server.

The request does **not contain the required Referer header**, which is why access is denied.

### 2. Modifying the Referer Header
To bypass the restriction, I manually add the expected **Referer header** to the request.

Example using `curl`:
```
curl -u natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ \
-H "Referer: http://natas5.natas.labs.overthewire.org/" \
http://natas4.natas.labs.overthewire.org
```

This sends a request that pretends to come from the required page.

**Security Insight:**\
Relying on the **Referer header** for authentication or authorization is insecure because it can easily be manipulated by the client.

---

## 💡 Discovery

**1. Sending the Modified Request**

After sending the request with the correct **Referer header**, the server grants access to the page.

**2. Retrieving the Password**

The page reveals the credentials for the next level:
```bash
Access granted. The password for natas5 is 0n35PkggAPm2zbEpOU802c0x0Msn1ToK