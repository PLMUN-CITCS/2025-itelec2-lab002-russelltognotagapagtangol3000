# tagapagtangol3000
# ITELEC2
# Problem Set 01 - Problem 01
# Simple Calculator Program

def main():
    # Print the program header
    print("Simple Calculator Program")

    # Get two numbers from the user
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    # Return the sum of the two numbers
    print(f"The sum is {num1 + num2}")

    # Return the difference of the two numbers
    print(f"The difference is {num1 - num2}")

    # Return the product of the two numbers
    print(f"The product is {num1 * num2}")

    # Return the quotient of the two numbers
    print(f"The quotient is {(num1 / num2):.2f}")

if __name__ == "__main__":
    main()
