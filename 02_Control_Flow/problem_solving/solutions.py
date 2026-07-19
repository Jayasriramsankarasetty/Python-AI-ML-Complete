"""
Topic:
Control Flow Practice Solutions

Importance:
Developing logical problem-solving structures using conditionals and loops is
highly valued in coding interviews and when writing custom logic inside ML architectures.

This file covers:
- Solution 1: Prime Number Check (Optimized to O(sqrt(N)))
- Solution 2: Fibonacci Sequence Generation
- Solution 3: Palindrome Check (using mathematical reversal)
- Solution 4: Leap Year Verification
- Solution 5: Armstrong Number Validation
"""

# =====================================================================
# Solution 1: Prime Number Check
# =====================================================================
print("==================================================")
print("SOLUTION 1: Prime Number Check")
print("==================================================")

n = 29  # Number to test
is_prime = True

if n <= 1:
    is_prime = False
else:
    # Optimization: Only check up to square root of n (i * i <= n)
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

print(f"Is the number {n} prime? {is_prime}")

# Check with non-prime number
non_prime = 15
is_non_prime_prime = True
if non_prime <= 1:
    is_non_prime_prime = False
else:
    i = 2
    while i * i <= non_prime:
        if non_prime % i == 0:
            is_non_prime_prime = False
            break
        i += 1
print(f"Is the number {non_prime} prime? {is_non_prime_prime}")
print()


# =====================================================================
# Solution 2: Fibonacci Sequence Generation
# =====================================================================
print("==================================================")
print("SOLUTION 2: Fibonacci Sequence Generation")
print("==================================================")

terms = 10  # Number of terms to generate
first = 0
second = 1

print(f"Fibonacci sequence up to {terms} terms:")
if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print(first)
else:
    print(first, second, end=" ")
    for count in range(2, terms):
        nxt = first + second
        print(nxt, end=" ")
        first = second
        second = nxt
print("\n")


# =====================================================================
# Solution 3: Palindrome Check (Mathematical Reversal)
# =====================================================================
print("==================================================")
print("SOLUTION 3: Palindrome Check (Mathematical)")
print("==================================================")

# A palindrome reads the same backwards.
# E.g., 12321. We reverse mathematically.
original_num = 12321
temp = original_num
reversed_num = 0

while temp > 0:
    last_digit = temp % 10
    reversed_num = (reversed_num * 10) + last_digit
    temp = temp // 10  # Floor division to remove last digit

is_palindrome = (original_num == reversed_num)
print(f"Original number: {original_num} | Reversed number: {reversed_num}")
print(f"Is {original_num} a palindrome? {is_palindrome}")
print()


# =====================================================================
# Solution 4: Leap Year Verification
# =====================================================================
print("==================================================")
print("SOLUTION 4: Leap Year Verification")
print("==================================================")

year = 2024
is_leap = False

# Rules: Divisible by 4, and if divisible by 100, must be divisible by 400.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap = True

print(f"Year {year} is a leap year? {is_leap}")
print(f"Year 1900 is a leap year? {(1900 % 4 == 0 and 1900 % 100 != 0) or (1900 % 400 == 0)}")
print()


# =====================================================================
# Solution 5: Armstrong Number Validation
# =====================================================================
print("==================================================")
print("SOLUTION 5: Armstrong Number Validation")
print("==================================================")

# 153 is Armstrong of order 3: 1^3 + 5^3 + 3^3 = 153
armstrong_candidate = 153
num_str = str(armstrong_candidate)
num_digits = len(num_str)
sum_of_powers = 0

temp_val = armstrong_candidate
while temp_val > 0:
    digit = temp_val % 10
    sum_of_powers += digit ** num_digits
    temp_val //= 10

is_armstrong = (armstrong_candidate == sum_of_powers)
print(f"Candidate: {armstrong_candidate} | Calculated Sum: {sum_of_powers}")
print(f"Is {armstrong_candidate} an Armstrong number? {is_armstrong}")
print()


"""
Key Takeaways:
- Modulo `% 10` extracts the last digit of an integer, while floor division `// 10` removes the last digit.
- Prime checking only needs to run until `i * i <= N` (i.e. sqrt(N)), reducing time complexity from O(N) to O(sqrt(N)).
- Operator precedence: Logical 'and' has higher priority than 'or'. Use parentheses to avoid logical bugs.

Interview Relevance:
- Prime check, Fibonacci, and Palindrome checks are highly common in initial coding rounds.
- Reversing a string or number is a gateway pattern to list/array reversal questions.
- Practice explaining the math behind the O(sqrt(N)) optimization for primes.

AI/ML Relevance:
- Series calculations (like Fibonacci) relate conceptually to sequential algorithms (RNNs/LSTMs) where the next value depends on previous states.
- Mathematical parsing: Manipulating digits helps in feature extraction from structural ID strings or formatting custom datasets.
"""
