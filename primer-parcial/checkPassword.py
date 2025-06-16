def checkPassword(password):
    if len(password) >= 7 and password[0] == password[-1] and "*" in password:
        return True
    else:
        return False

print(checkPassword("neu*quen"))