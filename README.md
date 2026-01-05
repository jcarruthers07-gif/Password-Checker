# Password Strength Checker

A Python-based password checker that evaluates password strength using multiple security criteria. Provides **real-time feedback** with color-coded output, helping users create stronger passwords.

## Features
- Detects presence of **lowercase and uppercase letters**
- Ensures **numbers** and **symbols** are included
- Enforces **minimum length** of 8 characters
- Checks for **repeated characters** (e.g., "aaa", "111")
- Detects **sequential characters** (e.g., "abc", "123", "cba", "321")
- Compares against the **top 1000 common passwords**
- Estimates **password entropy in bits** and provides recommendations
- Provides **color-coded terminal feedback** for readability

## Tools & Technologies
- **Python 3**  
- **Colorama** for colored terminal output  
- **Regex (re)** for pattern matching  
- **Math** for entropy calculation  

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jcarruthers07-gif/password-checker.git
