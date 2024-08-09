from validator_collection import validators, checkers, errors

def main():
    email = input("Please enter your email address: ").strip()
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

def validate_email(email):
    try:
        validators.email(email)
        return True
    except errors.InvalidEmailError:
        return False

if __name__ == "__main__":
    main()
