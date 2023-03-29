import secrets
import string

def createPass(passlength = 12):
    letters = string.ascii_letters 
    digits = string.digits 
    specialchars = string.punctuation
    setText = letters + digits + specialchars
    password = ""
    isStrong = False 

    while not isStrong:
        password = ""

        for i in range(passlength):
             password += "".join(secret.choice(setText))
        
        if(any(char in specialChars for char in password) and 
           sum (char in digits for char in password) >= 2):
            isStrong = True

    return password 


if_name_=="_main_":
    print(createPass())