# main.py
# Secure Software Design and Development - Team Project
# Author: Sadat Ali (FA23-BCT-034)

import hashlib

import re


def check_password_strength(password: str) -> str:
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search(r"[A-Z]", password):
        return "Weak: Missing uppercase"
    if not re.search(r"[a-z]", password):
        return "Weak: Missing lowercase"
    if not re.search(r"[0-9]", password):
        return "Weak: Missing digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Missing special char"
    return "Strong password"

def greet():
    print("Welcome to the Secure Software Design Team Project!")


def secure_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


if __name__ == "__main__":
    greet()
    print("SHA-256 of 'secure':", secure_hash("secure"))