# Natas Level 21 → Level 22

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 21 → 22  
- **Category:** Web Security / Session Manipulation (Multi-Application Interaction)  
- **URL:** http://natas21.natas.labs.overthewire.org  
- **Username:** `natas21`  
- **Password:** `BPhv63cKE1lkQl04cE5CuFTzXe15NfiH`

---

## 🎯 Objective

Find the password for **natas22** by exploiting **session handling across multiple applications**.

---

## 🔍 Observations

The page contains:

- A message:  
  > You are logged in as a regular user.

- A link to another application:  
  > **Experimenter**

Clicking it redirects to:


> http://natas21-experimenter.natas.labs.overthewire.org


### 1. Experimenter Application

This application allows setting values via URL parameters:

Example:

``` id="d7m2kp"
?admin=1
```
However, setting admin=1 here does not immediately affect the main site.

## 🛠️ Investigation
### 1. Understanding the Vulnerability

Both applications share the same ***session*** storage.

Main app checks: **admin=1**
Experimenter app allows setting arbitrary session variables

This creates a cross-application ***session*** manipulation vulnerability.

### 2. Exploiting the Experimenter

Navigate to:

> http://natas21-experimenter.natas.labs.overthewire.org/?admin=1

This sets the session variable:
```
admin=1
```
in the shared ***session***.

### 3. Using the Same Session

Now return to the main application:

>http://natas21.natas.labs.overthewire.org

Ensure the same session cookie **(PHPSESSID)** is used.

## 💡 Discovery
### 1. Admin Access

The main application now detects:

>You are an admin.

because the session variable `admin=1` was set via the experimenter app.

### 2. Retrieving the Password

The page reveals the credentials for the next level:
```
natas22:d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz
```