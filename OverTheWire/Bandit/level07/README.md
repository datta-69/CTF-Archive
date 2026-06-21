# Bandit Level 7

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 7 → 8  
- **Category:** Linux Basics / grep / File Searching  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit7`  
- **Password:** `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit8**.

---

## 🔍 Observations

The password for the next level is stored in a file named `data.txt`.

The file is large, so manually searching is inefficient.  
We are given a hint that the password is next to the word **“millionth”**.

So we need to filter the content using `grep`.

---

## 🛠️ Steps

### 1. Connect via SSH

ssh bandit7@bandit.labs.overthewire.org -p 2220

Enter password:

>morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

---

### 2. Check File

>ls

Output:
>data.txt

---

### 3. Search for the Password

Use `grep` to find the required line:

>grep "millionth" data.txt

---

## 💡 Discovery

The line contains the password for the next level:

```bash
bandit8: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc