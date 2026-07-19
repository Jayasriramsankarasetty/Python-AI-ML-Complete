# Practice Questions: Python Basics (Module 01)

This directory contains practice problems designed to reinforce your understanding of variables, datatypes, operators, I/O, and typecasting.

Each question focuses on logic building, clean implementation, and concepts frequently evaluated in technical interviews and applied data roles.

---

## Questions

### 1. Temperature Converter
* **Description**: Write a program that prompts the user to enter a temperature in Celsius, converts it to Fahrenheit, and displays the result formatted to 2 decimal places.
* **Formula**: $F = (C \times 9/5) + 32$
* **Focus Area**: User input, arithmetic operators, explicit typecasting (string to float), and output formatting.

### 2. Swapping Variables Without a Temp Variable
* **Description**: Given two variables `a` and `b`, swap their values without using any third (temporary) variable. Print the values of `a` and `b` before and after the swap.
* **Focus Area**: Assignment operators, arithmetic swap logic, or Python-specific tuple unpacking swap logic.
* **Interview Context**: A classic puzzle frequently used in screening rounds to check Pythonic syntax knowledge.

### 3. BMI (Body Mass Index) Calculator
* **Description**: Write a program that reads a person's weight (in kilograms) and height (in meters). Calculate their Body Mass Index (BMI) and output the value rounded to 1 decimal place.
* **Formula**: $BMI = \frac{\text{weight}}{\text{height}^2}$
* **Focus Area**: Operator precedence, exponentiation (`**`), and formatted print statements.

### 4. Simple and Compound Interest Calculator
* **Description**: Create a script that takes the principal amount ($P$), rate of interest ($R$), and time period ($T$ in years) as inputs. Calculate and display:
  1. Simple Interest (SI)
  2. Compound Interest (CI) compounded annually.
* **Formulas**:
  * $SI = \frac{P \times R \times T}{100}$
  * $CI = P \times \left(1 + \frac{R}{100}\right)^T - P$
* **Focus Area**: Complex arithmetic operations, exponentiation, and typecasting.

### 5. Odd-Even Check Using Bitwise Operators
* **Description**: Write a program to check whether a given integer is odd or even using the bitwise AND (`&`) operator instead of the arithmetic modulus (`%`) operator.
* **Focus Area**: Bitwise operations, conditional Boolean mapping.
* **Interview Context**: Helps test the candidate's understanding of low-level binary data representation and optimization.

---

## How to Run the Solutions
The solutions are coded in the adjacent file [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/01_Python_Basics/practice_questions/solutions.py).

Run the solutions script via:
```bash
python solutions.py
```
