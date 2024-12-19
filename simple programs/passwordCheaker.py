passw = input("Enter password:\n")

is_upper = False
is_special = False
is_lower = False
is_digit = False


for char in passw:
    if char.isupper():
        is_upper = True
    elif char.islower():
        is_lower = True
    elif char.isdigit():
        is_digit = True
    elif char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/":
        is_special = True

length = len(passw)


if length >= 8 and is_upper and is_lower and is_digit and is_special:
    print("Strong password")
elif length >= 6 and (is_upper or is_lower) and (is_digit or is_special):
    print("Medium password")
else:
    print("Weak password")
