import sys

password = input("Please enter secret password: ")
attempt_count = 1
while password != "opensea":
    if attempt_count > 3:
        sys.exit("Too man invalid password attempts")
    password = input("Invalid password! True again: ")
    attempt_count += 1
print("Welcome to Opensea")
