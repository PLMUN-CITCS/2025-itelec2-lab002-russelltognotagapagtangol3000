# Your Name
# ITELEC2
# Laboratory #04 – Guided Coding Exercise:
# Input, Output, and Text Formatting in Python

# Get integer input from the user and convert it to an integer
user_integer = int(input("Enter an integer: "))

# Get decimal (float) input from the user and convert it to a float
user_decimal = float(input("Enter a decimal number: "))

# Get string input from the user (no conversion needed)
user_text = input("Enter a string: ")

# Display formatted output using old-style formatting
print("\nFormatted Output using old-style formatting:")
print("Integer: %d" % user_integer)
print("Decimal: %.2f" % user_decimal)  # Format to 2 decimal places
print("String: %s" % user_text)

# Display formatted output using f-strings
print("\nFormatted Output using f-strings:")
print(f"Integer: {user_integer}")
print(f"Decimal: {user_decimal:.2f}")  # Format to 2 decimal places
print(f"String: {user_text}")