# Bandit Level 3

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 3 → 4  
- **Category:** Linux Basics / Hidden Files  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit3`  
- **Password:** `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit4**.

---

## 🔍 Observations

The password for the next level is stored in a hidden file inside the `inhere` directory.

Hidden files in Linux start with a dot (`.`) and are not shown by default using `ls`.

---

## 🛠️ Steps

### 1. Connect via SSH

Use the following command to log in:

ssh bandit3@bandit.labs.overthewire.org -p 2220

When prompted, enter the password:

>MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

---

### 2. Go to the Target Directory

Move into the directory:

>cd inhere

---

### 3. List Hidden Files

Since the file is hidden, use:

>ls -a

Output will show a hidden file like:

> ...Hiding-From-You

---

### 4. Read the File

Use:

>cat ...Hiding-From-You

---

## 💡 Discovery

The file contains the password for the next level:

```bash
bandit4: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ