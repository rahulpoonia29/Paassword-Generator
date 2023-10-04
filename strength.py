import re


def strength_calculator(password):
    uppercase = re.findall(r"[A-Z]", password)
    lowercase = re.findall(r"[a-z]", password)
    digit = re.findall(r"[0-9]", password)
    punctuation = re.findall(r"[!@#$%&()+{}\[\]:;<>,.?\\/-]", password)

    password_strength = 0
    a = [uppercase, lowercase, digit, punctuation]

    # Adjusted weights based on perceived importance
    weights = [0.3, 0.3, 0.2, 0.4]

    for x, y in zip(a, weights):
        password_strength += len(x) * y

    # Bonus points for length
    length_bonus = min(max(len(password) / 12, 1.0), 2.0)
    password_strength *= length_bonus

    return min(max(password_strength, 0), 6.0)  # Scale to a range of 0 to 4
