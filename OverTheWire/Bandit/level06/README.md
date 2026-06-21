# Bandit Level 6

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 6 → 7  
- **Category:** Linux Basics / Find Command / File Permissions  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit6`  
- **Password:** ` HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit7**.

---

## 🔍 Observations

The password for the next level is stored somewhere on the server, not necessarily in the home directory.

Key hints:
- Owned by user `bandit7`
- Owned by group `bandit6`
- Exactly 33 bytes in size

This requires searching the entire filesystem using `find`.

---

## 🛠️ Steps

### 1. Connect via SSH

ssh bandit6@bandit.labs.overthewire.org -p 2220

Enter password:

> HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

---

### 2. Search for the File

Use the `find` command with multiple filters:

>find / -user bandit7 -group bandit6 -size 33c 2>/dev/null

---

### 3. Read the File

Once the correct file path is found, read it:

> cat /var/lib/dpkg/info/bandit7.password

---

## 💡 Discovery

The file contains the password for the next level:

```bash
bandit7: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj