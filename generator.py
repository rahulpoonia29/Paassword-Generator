import random
import string


def generate_password(
    password_length,
    upper_case_choice,
    lower_case_choice,
    digit_choice,
    punctuation_choice,
):
    password = ""
    all_characters = []

    # if type(int(password_length)) == int:
    #     password_length = int(password_length)
    # elif type(password_length) != int:
    #     raise TypeError("Please enter a valid number")

    if int(password_length) > 30:
        raise ValueError("Value too large")

    if upper_case_choice == 1:
        all_characters += string.ascii_uppercase
    if lower_case_choice == 1:
        all_characters += string.ascii_lowercase
    if digit_choice == 1:
        all_characters += string.digits
    if punctuation_choice == 1:
        all_characters += string.punctuation

    for i in range(0, password_length):
        letter_chosen = random.choice(all_characters)
        password = password + letter_chosen

    return password
