import re
import time

flags = []

welcome_message = f"""Greetings! Please choose a password for your account, ensure your password is within our guidelines
to allow for a secure account! To see our guidelines, please input "!Help" 
"""

print(welcome_message)

def help_message():
    print("""
    Your password should not be empty
    Too short (below 8 characters)
    No spaces
    Requires special characters such as *
    Requires digits
    
    Example Password: Pa$$word123*_%2
    """)
    time.sleep(2)

while True:
    user_password = input("Please pick a password: ")  # Input by user.

    if user_password == "!Help":
        help_message()
    else:

    # Setting variables to allow for string checks.
        chara_count = len(user_password)
        has_star = "*" in user_password
        has_underscore = "_" in user_password

        # Boolean variables.
        has_spaces = ' ' in user_password   #Checks for spaces
        is_empty = (chara_count == 0)       #Checks length of input
        is_too_short = (chara_count < 8)    #^^
        has_s_or_u = has_star or has_underscore
        has_digit = bool(re.search(r'\d', user_password))  ##Checks for digits

        checks = {
            "Your password should not be empty!": is_empty,
            "Your password is too short! It needs at least 8 Characters": is_too_short,
            "Your password should not have spaces!": has_spaces,
            "Your password should have a * or _ !": not has_s_or_u,
            "Your password should have digits!": not has_digit
        }

        for check, condition in checks.items():
            if condition:
                flags.append(check)

        if not flags:
            print("Your password has been accepted! Welcome to the Family!")
        else:
            for flag in flags:
                print(flag)
            flags.clear()
