# Natas Level 16 → Level 17

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 16 → 17  
- **Category:** Web Security / Command Injection (Filtered)  
- **URL:** http://natas16.natas.labs.overthewire.org  
- **Username:** `natas16`  
- **Password:** `hPkjKYviLQctEW33QmuXL6eDVfMW4sGo`

---

## 🎯 Objective

Find the password for **natas17** by exploiting a **command injection vulnerability with input filtering**.

---

## 🔍 Observations

The page contains a search box:

> Find words containing:

This looks similar to previous grep-based challenges.

### 1. Input Behavior
- Normal input returns matching words.
- Special characters like `;`, `|`, `&` are **blocked**.

### 2. Hypothesis
Even though dangerous characters are filtered, the backend likely still executes a command such as:

>grep -i `<input>` dictionary.txt

So we need a bypass technique.

## 🛠️ Investigation
### 1. Understanding the Filter

The application filters common command injection characters:

`; | &`

However, it does not block command substitution:

`$( )`

This allows us to inject commands inside $().

### 2. Exploiting Command Injection

We use command substitution to execute:

>cat /etc/natas_webpass/natas17

Payload:

>$(cat /etc/natas_webpass/natas17)
### 3. Blind Extraction Technique

The output is not directly visible, so we use a blind technique.

We test characters one by one:

>$(grep ^a /etc/natas_webpass/natas17)
```
If output changes → correct character

If no change → incorrect character
```
### 4. Automating the Attack

Using a script speeds up extraction.


## 💡 Discovery
### 1. Extracting the Password

Using **blind command injection**, we reconstruct the password character by character.

### 2. Final Result
```bash
natas17:EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC