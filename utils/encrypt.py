from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)


def encrypt_string(string: str) -> bytes:
    return f.encrypt(bytes(string, 'utf-8'))
