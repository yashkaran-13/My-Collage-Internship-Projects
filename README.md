# 🔐 Cyber Security Python Tools

Two beginner-friendly cyber security utilities written in **pure Python** —
no external libraries, no installation required beyond Python 3.

Built as part of a Cyber Security internship program.

---

## 📂 Projects

| File | Description |
|------|-------------|
| `password_strength_checker.py` | Evaluates password strength and gives improvement tips |
| `port_scanner.py` | Multi-threaded TCP port scanner with service detection |

---

## 1️⃣ Password Strength Checker

### What it does
Analyzes any password and returns a **score out of 8** with a strength label
(**VERY WEAK → WEAK → MODERATE → STRONG**), plus specific tips to improve it.

### Scoring criteria
| Check | Points |
|-------|--------|
| Length ≥ 8 characters | +2 |
| Length ≥ 12 characters | +3 (instead of +2) |
| Lowercase letters (a–z) | +1 |
| Uppercase letters (A–Z) | +1 |
| Digits (0–9) | +1 |
| Special characters (!@#$%...) | +2 |
| Repeating characters (e.g. `aaa`, `111`) | −1 |

It also blocks a built-in list of **15+ commonly leaked passwords**
(`123456`, `qwerty`, `letmein`, …), scoring them 0 instantly.

### How to run
```bash
python password_strength_checker.py
```
Then type any password at the prompt. The password is never displayed back —
only masked as `****`. Type `q` to quit.

### Example output
```
Password Strength Checker
Type 'q' to quit.

Enter a password to check: =============================================
Password : *************
Score    : 8/8
Strength : STRONG
Great job! This is a strong password.
=============================================
```

### Example — weak password
```
Password : ******
Score    : 0/8
Strength : VERY WEAK
Tips to improve:
   - This is a well-known weak password. Choose something unique.
```

---

## 2️⃣ Port Scanner

### What it does
Scans a target host for **open TCP ports** using raw sockets and reports which
common services are listening (SSH, HTTP, HTTPS, MySQL, RDP, etc.).

### Features
- 🚀 **Multi-threaded** — scans up to 100 ports concurrently with `ThreadPoolExecutor`
- 🌐 Accepts **hostname or IP** (auto-resolves via DNS)
- 🏷️ Identifies **14 common services** by port number
- ⏱️ Configurable connection timeout
- 📊 Clean scan summary with timestamp

### How to run
```bash
# Scan a target (default range: ports 1–1024)
python port_scanner.py <target>

# Scan a custom port range
python port_scanner.py <target> <start_port> <end_port>
```

### Examples
```bash
# Scan your own machine
python port_scanner.py 127.0.0.1 1 1024

# Scan a website's common ports
python port_scanner.py example.com 1 1000
```

### Example output
```
--------------------------------------------------
Target : 127.0.0.1 (127.0.0.1)
Ports  : 1 - 1024
Time   : 2026-10-16 18:59:04
--------------------------------------------------
[OPEN] Port 22     -> SSH
--------------------------------------------------
Scan complete. 1 open port(s) found.
--------------------------------------------------
```

### Recognized services
FTP (21) · SSH (22) · Telnet (23) · SMTP (25) · DNS (53) · HTTP (80) ·
POP3 (110) · IMAP (143) · HTTPS (443) · SMB (445) · MySQL (3306) ·
RDP (3389) · HTTP-Alt (8080)

---

## 🛠️ Requirements

- **Python 3.7+** — uses only the standard library (`socket`, `re`,
  `concurrent.futures`, `datetime`, `sys`)

No pip install needed. Download the files and run.

---

## ⚠️ Disclaimer

These tools are for **educational and defensive security purposes only**.

- The port scanner must only be used on systems **you own or have explicit
  written permission to test**. Unauthorized scanning may be illegal in your
  jurisdiction.
- The password checker runs entirely locally — no password you type is ever
  sent anywhere.

---

## 🚀 Quick Start

```bash
# 1. Clone or download this repository
git clone https://github.com/yashkaran-13/My-Collage-Internship-Projects.git
cd My-Collage-Internship-Projects

# 2. Try the password checker
python password_strength_checker.py

# 3. Scan your own machine
python port_scanner.py 127.0.0.1 1 1024
```
