try:
   
    age = int(input("Enter your age: "))
    membership = input("Are you a member? (Yes/No): ").strip().lower()

   
    if age >= 18:
        if membership == "yes":
            print("Access granted.")
        else:
            print("Membership required for access.")
    else:
        print("Access denied. Must be at least 18 years old.")

except ValueError:
    print("Invalid age input. Please enter an integer.")
