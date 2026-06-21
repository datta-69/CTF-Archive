# Bandit Level 1

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 1 → 2  
- **Category:** Linux Basics / Special Files  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit1`  
- **Password:** `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit2**.

---

## 🔍 Observations

The password for the next level is stored in a file named `-` in the home directory.

The file name is tricky because `-` is treated as a special argument in Linux commands.

---

## 🛠️ Steps

### 1. Connect via SSH

Use the following command to log in:

ssh bandit1@bandit.labs.overthewire.org -p 2220

When prompted, enter the password:

>ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

---

### 2. List Files

Check the directory contents:

>ls

Output:
```bash
-
```
### 3. Read the File

Directly using cat - will not work because - is interpreted as stdin.

Use one of the following methods:
```
cat ./-

OR

cat < -
 ```
## 💡 Discovery

The file contains the password for the next level:
```
bandit2: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx