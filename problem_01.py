# Russell Togno
# ITELEC2
# Problem Set 01 - Problem 01
# Simple Calculator Program

def main():
    # Introduce the program
    print("Simple Calculator Program")
    
    # Obtain user input
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    # Perform arithmetic operations and display results
    print(f"The sum is {num1 + num2}")
    print(f"The difference is {num1 - num2}")
    print(f"The product is {num1 * num2}")
    print(f"The quotient is {num1 / num2:.2f}")

if __name__ == "__main__":
    main()
