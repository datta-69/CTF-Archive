# Natas Level 3 → Level 4

## 🚩 Challenge Info

- **Platform:** OverTheWire – Natas Wargame  
- **Level:** 3 → 4  
- **Category:** Web Security / Directory Indexing  
- **URL:** http://natas3.natas.labs.overthewire.org  
- **Username:** `natas3`  
- **Password:** `3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH`

---

## 🎯 Objective

Find the password for **natas4** by identifying and accessing directories hidden from search engine crawlers.

---

## 🔍 Observations
Upon visiting the site, the page displays:
> "There is nothing on this page."

### 1. Source Code Inspection
In web security, the first step is to check the underlying source code (`Ctrl + U`). Inside the HTML, a developer comment was discovered:
```html

### 2. Understanding the Hint

The comment refers to robots.txt. This is a standard text file used by websites to communicate with search engine crawlers (like Google or Bing). It provides instructions on which parts of the site the bots are disallowed from indexing.


---

## 🛠️ Investigation
### 1. Accessing the Robots File
The robots.txt file is traditionally located in the root directory of the web server. I accessed it by navigating to:

http://natas3.natas.labs.overthewire.org/robots.txt

### 2. Analyzing the File Content
The file contained the following instructions:

User-agent: *
Disallow: /s3cr3t/
User-agent: *: These rules apply to every crawler/bot on the internet.

Disallow: /s3cr3t/: This tells bots to stay away from and not list the /s3cr3t/ folder in search results.

Security Insight: For an attacker, a Disallow entry acts as a roadmap. If a developer attempts to hide a folder from search engines using this method, it often contains sensitive or non-public information.

## 💡 Discovery
1. Accessing the Hidden Directory
I manually navigated to the "secret" directory by appending the path discovered in the robots file to the base URL:

http://natas3.natas.labs.overthewire.org/s3cr3t/

2. Exploiting Directory Indexing
The server was misconfigured to allow Directory Indexing. Instead of receiving a "403 Forbidden" error, I was presented with a list of the files stored within that folder.

Inside the folder, I found a file named users.txt. Opening this file revealed the credentials for the next level:

Plaintext
natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ