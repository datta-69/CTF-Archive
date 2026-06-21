# Bandit Level 4

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 4 → 5  
- **Category:** Linux Basics / File Types / Hidden Data  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit4`  
- **Password:** `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit5**.

---

## 🔍 Observations

Inside the `inhere` directory, there are multiple files.  
Only one of them contains human-readable text, while the others are binary data.

The task is to identify the correct file type.

---

## 🛠️ Steps

### 1. Connect via SSH

Use the following command:

ssh bandit4@bandit.labs.overthewire.org -p 2220

When prompted, enter the password:

>2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

---

### 2. Go to the Directory

>cd inhere

---

### 3. Identify File Types

Check what type each file is:

>file ./*

This will show which file contains ASCII text.

---

### 4. Read the Correct File

Once the human-readable file is identified, use:

>cat ./-file07

---

## 💡 Discovery

The correct file contains the password for the next level:

```bash
bandit5: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
