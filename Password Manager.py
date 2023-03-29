import bcrypt
import json
import getpass

# Load existing passwords from JSON file
try:
    with open("passwords.json", "r") as f:
        passwords = json.load(f)
except (json.JSONDecodeError, FileNotFoundError):
    passwords = {}

# Prompt user for a new password
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

# Store new password in the dictionary
passwords[username] = password

# Save the updated password dictionary to JSON file
with open("passwords.json", "w") as f:
    json.dump(passwords, f)

# Prompt user to retrieve a password
username = input("Enter username to retrieve password: ")

# Retrieve password from the dictionary
if username in passwords:
    password = passwords[username]
    print("Password for {} is {}".format(username, password))
else:
    print("Password not found for {}".format(username))


def load_user_data():
    try:
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary
        user_data = {}
    return user_data


username = input("Enter a username: ")
password = input("Enter a password: ")
hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
user_dict = {username: hashed_password}
user_data = load_user_data()
user_data.update(user_dict)
with open("user_data.json", "w") as f:
    json.dump(user_data, f)
