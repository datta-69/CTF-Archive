# Natas Level 5 → Level 6

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 5 → 6  
- **Category:** Web Security / Cookies & Authentication  
- **URL:** http://natas5.natas.labs.overthewire.org  
- **Username:** `natas5`  
- **Password:** `0n35PkggAPm2zbEpOU802c0x0Msn1ToK`

---

## 🎯 Objective

Find the password for **natas6** by analyzing how the website uses **cookies for authentication**.

---

## 🔍 Observations
Upon visiting the page, the following message is displayed:

> Access disallowed. You are not logged in.

### 1. Inspecting Browser Cookies
Since the page mentions authentication, the next logical step is to inspect the **cookies stored by the browser**.

Using **Developer Tools (`F12`) → Application → Storage → Cookies**, a cookie named:

```
loggedin=0

was found.
```

### 2. Understanding the Cookie

The value of this cookie determines whether the user is authenticated.


**loggedin=0**

- `0` → User is not logged in  
- `1` → User is logged in

This means the application is relying on a **client-side cookie** to control authentication.

---

## 🛠️ Investigation

### 1. Modifying the Cookie
Since cookies are stored on the client side, they can easily be modified.

Change the cookie value from:

```
loggedin=0 → loggedin=1
```

This can be done through **Developer Tools** or by using browser extensions that modify cookies.

### 2. Refresh the Page
After modifying the cookie, reload the page.

**Security Insight:**  
Client-side cookies should never be trusted for authentication without proper validation on the server.

---

## 💡 Discovery

### 1. Access Granted
After refreshing the page with the modified cookie, the server now treats the user as authenticated.

### 2. Retrieving the Password
The page reveals the credentials for the next level:

```html
Access granted. The password for natas6 is 0RoJwHdSKWFTYR5WuiAewauSuNaBXned