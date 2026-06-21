# Bandit Level 8

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 8 → 9  
- **Category:** Linux Basics / Sorting / uniq / grep  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit8`  
- **Password:** `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit9**.

---

## 🔍 Observations

The password is stored in `data.txt`.

Key hint:
- The password appears only **once**
- The file contains many repeated lines

So we need to identify the **unique line**.

---

## 🛠️ Steps

### 1. Connect via SSH

ssh bandit8@bandit.labs.overthewire.org -p 2220

Enter password:

>dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

---

### 2. Check File

>ls

Output:
>data.txt

---

### 3. Find Unique Line

Sort the file and filter unique occurrences:

>sort data.txt | uniq -u

---

## 💡 Discovery

The output shows the password for the next level:

```bash
bandit9: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM