# Bandit Level 2

## 🚩 Challenge Info

- **Platform:** OverTheWire – Bandit Wargame  
- **Level:** 2 → 3  
- **Category:** Linux Basics / Spaces in Filenames  
- **Host:** bandit.labs.overthewire.org  
- **Port:** 2220  
- **Username:** `bandit2`  
- **Password:** `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

---

## 🎯 Objective

Log into the server using SSH and find the password for **bandit3**.

---

## 🔍 Observations

The password for the next level is stored in a file named:

> --spaces in this filename--

The filename contains spaces, which makes it tricky to handle in Linux commands.

---

## 🛠️ Steps

### 1. Connect via SSH

Use the following command to log in:

ssh bandit2@bandit.labs.overthewire.org -p 2220

When prompted, enter the password:

>263JGJPfgU6LtdEvgfWU1XP5yac29mFx

---

### 2. List Files

Check the directory contents:

>ls -la 

Output:

> --spaces in this filename--

---

### 3. Read the File

Because the filename contains spaces, it must be handled properly.

Use either escaping or quotes:

>cat "./--spaces in this filename--"

OR

> cat ./\-\-spaces\ in\ this\ filename--

---

## 💡 Discovery

The file contains the password for the next level:

```bash
bandit3: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx