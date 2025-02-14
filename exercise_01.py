# Russell Togno
# ITELEC2
# Laboratory #03 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

# Variable declarations with numeric literals
count = 10                   # 'count' is assigned 10 (integer literal)
Count = 15                   # 'Count' (different from 'count') is assigned 15
decimal_value = 3.14         # 'decimal_value' is assigned 3.14 (float literal)

total_count = 20             # Another integer literal assignment

# String literal
greeting = "Hello, Python!"

# Boolean literal
is_active = True

# None literal
result = None

# Displaying values
print("Integer (count):", count)
print("Integer (Count):", Count)
print("Integer (total_count):", total_count)
print("Decimal:", decimal_value)
print("Text:", greeting)
print("Boolean:", is_active)
print("None Value:", result)

# Inline arithmetic using f-string
num1 = 5
num2 = 3
print(f"Sum: {num1 + num2:.2f}")  # The result (8.00) is formatted to 2 decimal places
