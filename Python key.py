import secrets
import bcrypt

# Generate a strong, random password
password = secrets.token_hex(16)

# Hash the password with bcrypt
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

# Print the password and hashed password
print("Password:", password)
print("Hashed password:", hashed_password.decode("utf-8"))
