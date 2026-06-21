# Bandit Level 5

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 5 → 6  
- **Category:** Linux Basics / File Properties / Find Command  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit5`  
- **Password:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit6**.

---

## 🔍 Observations

The password is stored somewhere inside the `inhere` directory.

Key hints:
- The file is **human-readable**
- It is **1033 bytes in size**
- It is **not executable**

So we need to search based on file properties.

---

## 🛠️ Steps

### 1. Connect via SSH

ssh bandit5@bandit.labs.overthewire.org -p 2220

Enter password:

>4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

---

### 2. Go to Directory

>cd inhere

---

### 3. Find the Correct File

Use the `find` command with size filtering:

>find . -type f -size 1033c

---

### 4. Read the File

Once the file is found, display its contents:

>cat ./maybehere07/.file2 

---

## 💡 Discovery

The file contains the password for the next level:

```bash
bandit6: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG