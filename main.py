# main.py
# Secure Software Design and Development - Team Project
# Author: Sadat Ali (FA23-BCT-034)

import hashlib


def greet():
    print("Welcome to the Secure Software Design Team Project!")


def secure_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


if __name__ == "__main__":
    greet()
    print("SHA-256 of 'secure':", secure_hash("secure"))