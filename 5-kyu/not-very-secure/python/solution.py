def alphanumeric(password):
    if not len(password) == 0:
        if password.isalnum():
            return True
    return False 