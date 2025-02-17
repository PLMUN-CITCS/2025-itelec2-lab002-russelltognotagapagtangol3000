try:
    # Get user input and convert it to an integer
    number = int(input("Enter a number: "))

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"The number {number} is Even.")
    else:
        print(f"The number {number} is Odd.")

except ValueError:
    print("Invalid input. Please enter an integer.")
