def password_required(func):
    def wrapper():
        password = input("Enter password: ")
        if password == "mysecretpassword":
            func()
        else:
            print("Incorrect password!")
    return wrapper


@password_required
def bank_credentials():
    print("Bank card: 0000-1111-2222-3333-4444")
    print("Bank password: 1234")
    print("Amount: 100,000,000$")


@password_required
def instagram_credentials():
    print("Username: snowden")
    print("Password: cia")

bank_credentials()
instagram_credentials()