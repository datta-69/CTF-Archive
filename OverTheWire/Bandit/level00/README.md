# Bandit Level 0 → Level 1

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 0 → 1  
- **Category:** Linux Basics / SSH Access  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit0`  
- **Password:** `bandit0`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit1**.

---

## 🔍 Observations

This is the **starting level**, designed to teach basic SSH access and simple file reading.

After logging in, It's in the home directory of `bandit0`.

---

## 🛠️ Steps

### 1. Connect via SSH

Use the following command to log in:


ssh bandit0@bandit.labs.overthewire.org -p 2220

When prompted, enter the password:

>bandit0

### 2. List Files

After logging in, check the directory contents:

>ls

Output: `readme`
### 3. Read the File

Open the file using `cat`:

>cat readme

## 💡 Discovery

The file contains the password for the next level:
```bash
bandit1: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If