def display_menu() -> None:
    """
    Displays the program's menu options to the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user() -> None:
    """
    Prints a greeting message.
    """
    print("Hello! Welcome!")

def check_even_odd(number: int) -> str:
    """
    Determines whether the given number is even or odd.
    
    :param number: The integer to check.
    :return: A string indicating if the number is even or odd.
    """
    return "even" if number % 2 == 0 else "odd"

def even_odd_checker_action() -> None:
    """
    Handles the logic for the even/odd check, including getting user input.
    """
    try:
        number = int(input("Enter an integer: "))
        result = check_even_odd(number)
        print(f"{number} is an {result} number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def handle_menu_choice(choice: int) -> bool:
    """
    Executes the corresponding action based on the user's menu choice.
    
    :param choice: The menu option selected by the user.
    :return: True if the program should exit, False otherwise.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice! Please select a valid option.")
    return False

def main():
    """
    Main function to run the menu-driven program.
    """
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
