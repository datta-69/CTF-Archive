# Bandit Level 10

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 10 → 11  
- **Category:** Linux Basics / Base64 decoding  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit10`  
- **Password:** `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit11**.

---

## 🔍 Observations

The password is stored in `data.txt`.

Key hint:
- The file contains **base64 encoded data**
- We need to decode it to reveal the actual password

---

## 🛠️ Steps

### 1. Connect via SSH

ssh bandit10@bandit.labs.overthewire.org -p 2220

Enter password:

>FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

---

### 2. Check File

>ls

Output:
>data.txt

---

### 3. Decode the File

Use the `base64` command with decode flag:

>base64 -d data.txt

---

## 💡 Discovery

The decoded output reveals the password for the next level:

```bash
bandit11: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr