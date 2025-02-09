# 2025-ITELEC2-LAB002
Laboratory Activity # 02 - Working with Variables, Arithmetic and Assignment Operators

---

### **Step 1: Accept the Assignment**

1. Click on the assignment link provided by your instructor.
2. GitHub Classroom will create a **private repository** under your GitHub account.
3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 2: Clone the Repository to Your Local Machine**

1. On your repository page, click the green **"Code"** button.
2. Copy the repository URL (choose HTTPS for simplicity).
3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:

```bash
git clone <your_git_repo_url>
```

4. Navigate into the cloned folder:

```bash
cd <your_local_repo_folder>
```

### **Step 3: Complete the Assignment**
**Overview**
This problem set consists of two Python programming tasks designed to build basic skills in coding and user interaction. The first task creates a simple calculator that performs arithmetic operations on two user-provided numbers, while the second computes the square of a single number.

# **Problem Set 01 – Problem 01: Simple Calculator Program**

**Objectives**
- Programming Fundamentals: Learn how to write a Python script that takes user input, performs arithmetic operations, and displays results.
- User Interaction: Practice obtaining input from users and formatting the output.
- Code Organization: Understand the importance of clear code structure and comments for readability.

**Folder Structure and Naming Conventions**
- File Name: problem_01.py
- Location: Place the file in the root folder of your repository.
- File Header: Include your name, course code (e.g., ITELEC2), and a brief description as shown in the starter template.

**Desired Output**
When the program runs, it should display:
- The title:
```txt
Simple Calculator Program
```
- Prompts for two numbers.
- The sum, difference, product, and quotient of the two numbers (formatted to two decimal places for the quotient).
*Example (with sample numbers):*
```txt
Simple Calculator Program
Enter 1st number: 8
Enter 2nd number: 2
The sum is 10
The difference is 6
The product is 16
The quotient is 4.00
```

**Notable Observations**
- Input Conversion: Ensure user inputs are converted to integers for proper arithmetic operations.
- Division Consideration: Note the quotient is formatted to two decimal places using :.2f, which is a format specifier that controls numerical precision.
- F-string Arithmetic: Python f-strings allow you to perform arithmetic operations directly within the expression brackets (e.g., {num1 + num2}), streamlining your code.
- Code Comments: Use header comments for documentation and update them with your actual details.
- Consistent File Structure: Maintain the file in the repository's root directory and adhere to naming conventions to support automatic grading.

**Step-by-Step Instructions**
1. Initialize the File:
- Open problem_01.py in your text editor or IDE.
- Start with the following template:
```python
# YOUR NAME
# ITELEC2
# Problem Set 01 - Problem 01
# Simple Calculator Program

def main():
    pass  # replace this line with all of your code

if __name__ == "__main__":
    main()
```

2. Introduce the Program:
- Replace the pass statement with a print statement to introduce the program:
```python
print("Simple Calculator Program")
```

3. Obtain User Input:
- Prompt the user for two numbers and convert the inputs to integers:
```python
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
```

4. Perform Arithmetic Operations:
- Sum:
```python
print(f"The sum is {num1 + num2}")
```
- Difference:
```python
print(f"The difference is {num1 - num2}")
```
- Product:
```python
print(f"The product is {num1 * num2}")
```
- Quotient:
```python
print(f"The quotient is {(num1 / num2):.2f}")
```

5. Run and Verify:
- Save the file and verify its output by running the command in your terminal
```bash
python problem_01.py
```

**Conclusion**
Completing the Simple Calculator Program reinforces essential programming concepts such as input handling, arithmetic operations, and output formatting. It also introduces the power of f-string expressions and format specifiers, all of which are crucial for writing clean and efficient code.

# **Problem Set 01 – Problem 02: Square the Number Program**

**Objectives**
- Basic Computation: Compute and display the square of a number using Python.
- User Interaction: Practice obtaining and processing user input.
- Program Structure: Transform a template into a functional program.

**Folder Structure and Naming Conventions**
- File Name: problem_02.py
- Location: Save the file in the root folder of your repository.
- File Header: Include your name, course code (e.g., ITELEC2), and a brief description per the provided starter template.

**Desired Output**
When the program runs, it should display:
- The title:
```txt
Square the Number Program
```
- Prompts for two numbers.
- The sum, difference, product, and quotient of the two numbers (formatted to two decimal places for the quotient).
*Example (with sample numbers):*
```txt
Square the Number Program
Enter a number: 5
The square of 5 is 25.00
```

**Notable Observations**
- Input Handling: Ensure that the input is correctly converted to an integer for computation.
- F-string Arithmetic: The square is computed directly inside the f-string (i.e., {number * number}), demonstrating the convenience of embedding arithmetic within a print statement.
- Format Specifier: The use of :.2f ensures that the output is formatted to two decimal places, providing consistency and precision in numerical output.
- Simplicity and Clarity: The program exemplifies how a concise code structure can be both readable and functional.

**Step-by-Step Instructions**
1. Initialize the File:
- Open problem_02.py in your text editor or IDE.
- Start with the following template:
```python
# YOUR NAME
# ITELEC2
# Problem Set 01 - Problem 01
# Simple Calculator Program

def main():
    pass  # replace this line with all of your code

if __name__ == "__main__":
    main()
```

2. Introduce the Program:
- Replace the pass statement with a print statement to introduce the program:
```python
print("Square the Number Program")
```

3. Obtain User Input:
- Prompt the user for a number:
```python
number = int(input("Enter a number: "))
```

4. Compute the Square:
- Calculate and display the square (formatted to two decimal places):
```python
print(f"The square of {number} is {(number * number):.2f}")
```

5. Run and Verify:
- Save the file and verify its output by running the command in your terminal
```bash
python problem_02.py
```

**Conclusion**
The Square the Number Program strengthens your skills in handling user input and performing basic computations. By embedding arithmetic operations within f-strings and utilizing format specifiers, you learn techniques that help create clean, efficient, and well-formatted output. Both problems together lay a solid foundation for further programming challenges.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
Open the terminal and run:

```bash
git status
```
This command shows any modified or new files.

2. Stage the changes:
Add all modified files to staging:

```bash
git add .
```

3. Commit your changes:
Write a meaningful commit message:

```bash
git commit -m "Submitting Python Session 03 - Exercise 01"
```

4. Push your changes to GitHub:
Upload your changes to your remote repository:

```bash
git push origin main
```

### **Step 5: Submit Your Repository Link**
Once your changes have been pushed:
1. Visit your GitHub repository online.
2. Copy the repository URL from your browser (e.g., https://github.com/PLMUN-CITCS/itelec2-s03-e01-[your username] ).
3. Submit the repository link to your instructor via the classroom portal or as instructed.

