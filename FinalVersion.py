# Password Checker v2 - Cleaned and Commented
# Uses methods, checks entropy, sequences, repeats, common passwords
# Colorama for feedback, math for entropy, re for regex

from colorama import Fore, Style, init
import math
import re

init(autoreset=True)  # Automatically reset color after each print

# Load common passwords into a list
with open("1000_passwords.txt") as file:
    common_passwords = file.read().splitlines()


# -------------------------
# Individual check methods
# -------------------------
def common_check(p):
    """Check if password is among the top 1000 common passwords."""
    if p in common_passwords:
        return Fore.RED + "Password is in top 1000 most used passwords"
    return Fore.GREEN + "True"

def lowercase_check(p):
    """Check for at least one lowercase letter."""
    return Fore.GREEN + "True" if re.search(r"[a-z]", p) else Fore.RED + "False"

def uppercase_check(p):
    """Check for at least one uppercase letter."""
    return Fore.GREEN + "True" if re.search(r"[A-Z]", p) else Fore.RED + "False"

def number_check(p):
    """Check for at least one number."""
    return Fore.GREEN + "True" if re.search(r"\d", p) else Fore.RED + "False"

def symbol_check(p):
    """Check for at least one symbol."""
    pattern = r"[!@#$%^&*`?\[\]{}\",.><:']"
    return Fore.GREEN + "True" if re.search(pattern, p) else Fore.RED + "False"

def length_check(p):
    """Check if password has at least 8 characters."""
    return Fore.GREEN + "True" if len(p) >= 8 else Fore.RED + "False"

def repeat_check(p):
    """Check if there are no 3 repeated characters in a row."""
    return Fore.RED + "False" if re.search(r"(.)\1{2}", p) else Fore.GREEN + "True"

def sequence_check(p):
    """Check if there are no sequential characters (abc, 123, cba, 321)."""
    for i in range(len(p) - 2):
        if ord(p[i]) + 1 == ord(p[i + 1]) and ord(p[i + 1]) + 1 == ord(p[i + 2]):
            return Fore.RED + "False"
        if ord(p[i]) - 1 == ord(p[i + 1]) and ord(p[i + 1]) - 1 == ord(p[i + 2]):
            return Fore.RED + "False"
    return Fore.GREEN + "True"


# -------------------------
# Entropy calculation
# -------------------------
def entropy_check(p):
    """Estimate password entropy in bits."""
    base = 0
    # Count character sets used
    if "True" in lowercase_check(p):
        base += 26
    if "True" in uppercase_check(p):
        base += 26
    if "True" in number_check(p):
        base += 10  # Include 0-9
    if "True" in symbol_check(p):
        base += 32  # Approximate symbol set

    if base == 0:
        return "Entropy cannot be calculated"

    bits = round(math.log(base ** len(p), 2))
    if bits >= 60:
        return f"Password entropy: {Fore.GREEN}{bits} bits - Good Job!"
    return f"Password entropy: {Fore.RED}{bits} bits - Aim for 60+ bits"


# -------------------------
# Combined checks
# -------------------------
def password_check(p):
    """Run all checks and display results."""
    print("Has lowercase:", lowercase_check(p))
    print("Has uppercase:", uppercase_check(p))
    print("Has number:", number_check(p))
    print("Has symbol:", symbol_check(p))
    print("8+ characters:", length_check(p))
    print("No repeats (aaa, 111):", repeat_check(p))
    print("No sequences (abc, 123):", sequence_check(p))
    print("Uncommon password:", common_check(p))
    print(entropy_check(p))


def password_good_enough(p):
    """Return final assessment if all required checks pass."""
    checks = [
        lowercase_check(p),
        uppercase_check(p),
        number_check(p),
        symbol_check(p),
        length_check(p),
        repeat_check(p),
        sequence_check(p),
        common_check(p),
    ]
    if Fore.RED + "False" in checks or "top 1000" in checks:
        return Fore.RED + "One or more checks failed"
    return Fore.GREEN + "Password sufficient!"


# -------------------------
# Main program
# -------------------------
if __name__ == "__main__":
    password = input("Enter new password: ")
    password_check(password)
    print(password_good_enough(password))