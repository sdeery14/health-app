import secrets

secret_key = secrets.token_hex(32)  # Generates a 64-character string (256 bits)
print(secret_key)