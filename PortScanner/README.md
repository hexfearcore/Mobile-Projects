
# 🔎 Port Scanner - by HEXFEARCORE

A powerful, fast, and beginner-friendly **command-line port scanning tool** written in **Python 3**, created for Termux, Android IDEs, or any terminal environment.

> Part of the [Mobile-Projects](https://github.com/hexfearcore/Mobile-Projects) CLI tool series.

---

## 🚀 Features

- ✅ Scan any IP or domain name
- ✅ Define custom port ranges (e.g., 1–1000)
- ✅ Fast multithreaded scanning
- ✅ Colored output using `colorama`
- ✅ Built entirely with Python 3
- ✅ Designed to run in Termux / Android IDEs

---
---

## 🔧 Installation (Termux / Mobile IDE)

1. **Install Python**
```bash
pkg install python -y
git clone https://github.com/hexfearcore/Mobile-Projects.git
cd Mobile-Projects/PortScanner
pip install -r requirements.txt
```

## Usage 
```bash
python port-scanner.py <target> -p <start>-<end>
eg: python port-scanner.py 192.168.0.1 -p 1-100
```
