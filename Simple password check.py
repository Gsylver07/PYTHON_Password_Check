# import regular expressions module to check specifications.
import re


# Create a function to check if the password is valid.
def passwordCheck(password):
    # Check length of password.
    if len(password) < 8:
        return False

    # Check for a minimum of one lowercase character.
    lowerCaseRegex = re.compile(r'[a-z]')
    if not lowerCaseRegex.search(password):
        return False

    # Check for a minimum of one uppercase character.
    upperCaseRegex = re.compile(r'[A-Z]')
    if not upperCaseRegex.search(password):
        return False

    # Check for a minimum of one numerical or special character input.
    numberRegex = re.compile(r'/d')
    if numberRegex.search(password):
        return False

    return True


print('''Please enter a password. Your password must contain:
Atleast one capital letter
Atleast one small letter
Atleast one digit or special character
Must be a minimum of 8 characters long\n''')

password = input('Please enter your password: ')

# Output if password doesn't have all attributes required.
while not passwordCheck(password):
    password = input('Your password is weak. Please enter another password: ')

# Output if password meets all attributes required.
print('\nYour password is strong.')
