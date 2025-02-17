# creating email validation program using string function 
import re
def validate_email(email):
    # Check minimum length
    if len(email) < 6:
        return "Invalid Email"

    # Check first character (should be a letter)
    if not email[0].isalpha():
        return "Invalid Email,first character should be a letter"

    # Check if exactly one '@' is present
    if email.count("@") != 1:
        return "Invalid Email, only one @ is allowed"

    # Check if domain ends with '.com' or '.in' or similar (.edu, .org, etc.)
    if not (email.endswith(".com") or email.endswith(".in") or email.endswith(".org") or email.endswith(".edu")):
        return "Invalid Email, domain should be end with (.com , .in, .org) "

    # Check for invalid characters
    for char in email:
        if char.isspace():  # No spaces allowed
            return "Invalid Email,No spaces allowed"
        if char.isupper():  # No uppercase letters allowed
            return "Invalid Email,No uppercase letters allowed"
        if char not in "abcdefghijklmnopqrstuvwxyz0123456789@._":
            return "Invalid Email"

    return "Valid Email"

# Taking input
email = input("Enter your email: ")
print(validate_email(email))
