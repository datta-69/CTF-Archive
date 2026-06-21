# Bandit Level 11

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 11 → 12  
- **Category:** Linux Basics / ROT13 / tr command  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit11`  
- **Password:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit12**.

---

## 🔍 Observations

The password is stored in `data.txt`.

Key hint:
- The file content is **ROT13 encoded**
- ROT13 shifts letters by 13 positions in the alphabet
- We need to decode it back to normal text

---

## 🛠️ Steps

### 1. Connect via SSH

ssh bandit11@bandit.labs.overthewire.org -p 2220

Enter password:

>dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

---

### 2. Check File

>ls

Output:
>data.txt

---

### 3. Decode ROT13

Use the `tr` command:

>cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

---

## 💡 Discovery

The decoded output reveals the password for the next level:

```bash
bandit12: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4