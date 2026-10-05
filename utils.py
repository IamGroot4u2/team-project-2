# utils.py
import secrets
import string


def generate_secure_token(length: int = 32) -> str:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print("Secure Token:", generate_secure_token())