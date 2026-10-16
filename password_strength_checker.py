"""
Password Strength Checker
-------------------------
A simple tool that evaluates how strong a password is based on:
  - Length
  - Use of uppercase & lowercase letters
  - Use of digits
  - Use of special characters
  - Detection of common weak passwords / patterns
"""

import re

COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "abc123",
    "111111", "letmein", "iloveyou", "dragon", "monkey",
    "football", "sunshine", "master", "shadow", "superman"
}


def check_password(password: str) -> dict:
    """Return a strength report for the given password."""
    score = 0
    feedback = []

    # 1. Length
    length = len(password)
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    else:
        feedback.append("Use at least 8 characters (12+ is recommended).")

    # 2. Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    # 3. Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    # 4. Digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add digits (0-9).")

    # 5. Special characters
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\",.<>/?`~|\\]", password):
        score += 2
    else:
        feedback.append("Add special characters (!@#$% etc.).")

    # 6. Common / weak password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback = ["This is a well-known weak password. Choose something unique."]
    elif re.search(r"(.)\1{2,}", password):  # e.g. "aaa", "1111"
        score -= 1
        feedback.append("Avoid repeating the same character (e.g. 'aaa', '111').")

    # Clamp score between 0 and 8
    score = max(0, min(score, 8))

    # Strength label
    if score <= 2:
        strength = "VERY WEAK"
    elif score <= 4:
        strength = "WEAK"
    elif score <= 6:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    return {
        "score": score,
        "max_score": 8,
        "strength": strength,
        "feedback": feedback,
    }


def print_report(password: str) -> None:
    report = check_password(password)
    print("=" * 45)
    print(f"Password : {'*' * len(password)}")
    print(f"Score    : {report['score']}/{report['max_score']}")
    print(f"Strength : {report['strength']}")
    if report["feedback"]:
        print("Tips to improve:")
        for tip in report["feedback"]:
            print(f"   - {tip}")
    else:
        print("Great job! This is a strong password.")
    print("=" * 45)


if __name__ == "__main__":
    print("Password Strength Checker")
    print("Type 'q' to quit.\n")
    while True:
        pwd = input("Enter a password to check: ")
        if pwd.lower() == "q":
            break
        print_report(pwd)
