# Problem Solving: Control Flow (Module 02)

This directory focuses on intermediate logic problems involving conditional logic and loops. These are fundamental interview questions.

---

## Questions

### 1. Prime Number Check
* **Description**: Write a program to determine if a given positive integer $N$ is a prime number.
* **Logic**: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself. Optimize the loop to check for factors up to $\sqrt{N}$.
* **Focus Area**: Efficient loops (`break`), handling edge cases (like 1, 2, and negative integers).

### 2. Fibonacci Sequence Generation
* **Description**: Write a program that prints the first $N$ terms of the Fibonacci sequence.
* **Sequence**: $0, 1, 1, 2, 3, 5, 8, 13, 21, \dots$
* **Focus Area**: Variable updates, initialization, tracking counts with loops.

### 3. Palindrome Check
* **Description**: Determine whether a given integer or string is a palindrome. (A palindrome reads the same backwards as forwards, e.g., `121` or `radar`).
* **Logic**: Implement the check without using advanced slicing `[::-1]` to show your core logic flow (reversing numbers mathematically using loops).
* **Focus Area**: Modulo arithmetic, division, loops.

### 4. Leap Year Verification
* **Description**: Write a program to check if a user-input year is a leap year.
* **Rules**: A year is a leap year if:
  1. It is divisible by 4, AND
  2. If it is divisible by 100, it must also be divisible by 400.
* **Focus Area**: Logical operators (`and`, `or`), operator precedence, and nested conditional structures.

### 5. Armstrong Number Validation
* **Description**: Check if a given number is an Armstrong number (Narcissistic number) of order $D$ (where $D$ is the number of digits).
* **Example**: $153$ is an Armstrong number because $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$.
* **Focus Area**: Multi-digit extraction using loops, mathematical formulas, and type conversion.

---

## How to Run the Solutions
The solutions are coded in [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/02_Control_Flow/problem_solving/solutions.py).

Run the solutions script via:
```bash
python solutions.py
```
