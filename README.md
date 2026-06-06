# 🛡️ Phishing Detection Tool

A beginner-friendly cybersecurity project developed in Python that analyzes URLs and email content for common phishing indicators. The tool uses rule-based detection techniques and risk scoring to help identify potentially malicious links and phishing emails.

## 📌 Overview

Phishing attacks are among the most common cyber threats, often tricking users into revealing sensitive information such as passwords, banking credentials, and personal data.

This project demonstrates how phishing attempts can be detected using simple yet effective heuristic checks without relying on machine learning, databases, or external libraries.

## ✨ Features

### URL Analysis

The tool analyzes URLs and checks for:

* IP addresses instead of domain names
* Excessively long URLs
* Multiple subdomains
* Suspicious keywords such as:

  * login
  * verify
  * update
  * secure
  * account
  * password
  * bank
* URL shortening services

### Email Analysis

The tool scans email content for:

* Urgent or threatening language
* Requests for sensitive information
* Suspicious links
* Common phishing phrases

### Risk Scoring System

Each suspicious indicator contributes to a risk score.

| Score Range | Classification |
| ----------- | -------------- |
| 0 – 30      | Safe           |
| 31 – 70     | Suspicious     |
| 71 – 100    | Phishing       |

### Result Explanation

The tool provides:

* Risk score
* Threat classification
* Detailed reasons for flagging content

## 🛠 Technologies Used

* Python 3
* re (Regular Expressions)
* urllib.parse
* datetime

No external dependencies are required.

## 📂 Project Structure

```text
phishing-detector/
│
├── phishing_detector.py
│
├── modules/
│   ├── __init__.py
│   ├── url_checker.py
│   ├── email_checker.py
│   ├── risk_scoring.py
│   └── utils.py
│
├── samples/
│   ├── safe_email.txt
│   ├── phishing_email.txt
│   ├── safe_urls.txt
│   └── phishing_urls.txt
│
├── reports/
│   └── analysis_log.txt
│
├── README.md
└── requirements.txt
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/phishing-detector.git
cd phishing-detector
```

Run the program:

```bash
python phishing_detector.py
```

## 💻 Usage

After starting the application, choose one of the available options:

```text
1. Analyze URL
2. Analyze Email
3. Exit
```

### Example URL Scan

```text
Enter URL:
http://192.168.1.1/login

Risk Score: 85
Classification: PHISHING
```

### Example Email Scan

```text
URGENT!

Your account has been suspended.
Verify now using the link below:
http://fake-bank-login.com
```

Output:

```text
Risk Score: 90
Classification: PHISHING
```

## 🎯 Learning Objectives

This project helps beginners understand:

* Phishing attack techniques
* URL analysis
* Email threat detection
* Risk scoring systems
* Python modular programming
* Cybersecurity fundamentals

## ⚠ Disclaimer

This project is intended for educational and learning purposes only. It is not designed to replace professional email security solutions, web filtering systems, or enterprise threat detection platforms.

## 👨‍💻 Author

Developed as a cybersecurity learning project to demonstrate phishing detection using Python and rule-based analysis techniques.

## 📜 License

This project is released under the MIT License.
