# Bandit Level 9

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 9 → 10  
- **Category:** Linux Basics / Strings / grep / binary data  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit9`  
- **Password:** `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit10**.

---

## 🔍 Observations

The password is stored in `data.txt`.

Key hints:
- The file contains **non-readable / binary-like data**
- The password is in **human-readable strings**
- We need to extract readable text from the file

So the correct approach is to use the `strings` command.

---

## 🛠️ Steps

### 1. Connect via SSH

ssh bandit9@bandit.labs.overthewire.org -p 2220

Enter password:

>4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

---

### 2. Check File

>ls

Output:
>data.txt

---

### 3. Extract Readable Strings

Use the `strings` command to filter readable text:

>strings data.txt

To narrow it down, you can combine with grep:

>strings data.txt | grep "="

---

## 💡 Discovery

The output contains the password for the next level:

```bash
bandit10: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey