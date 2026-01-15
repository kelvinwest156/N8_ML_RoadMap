def pswd_strong(password):
    if len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(
            c.isdigit() for c in password):
        return True
    else:
        return False


print("A STRONG PASSWORD MUST CONTAIN AT LEAST ONE UPPERCASE, LOWERCASE AND A NUMBER")

password = input("Enter your password: ")
if pswd_strong(password):
    print("Your password is strong")
else:
    print("Password is weak")
