"""
Topic:
Recursion and Backtracking Problems

Importance:
Recursion and Backtracking allow systematic exploration of decision tree spaces.
These concepts are core to path-finding algorithms, permutations, and combinatorial optimizations.

This file covers:
- Problem 1: Generate Parentheses
- Problem 2: Permutations (Distinct Integers)
- Problem 3: N-Queens Chessboard Placement
"""

# =====================================================================
# PROBLEM 1: Generate Parentheses
# =====================================================================
# Problem Statement:
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
# Approach:
# Constraint-Guided Backtracking:
# We maintain a recursive helper `backtrack(current_string, open_count, close_count)`:
# - Base Case: If len(current_string) == 2 * n, we have placed all brackets. Append current_string to results and return.
# - Branch 1 (Open): If open_count < n, we can always add an opening bracket '(':
#   `backtrack(current_string + '(', open_count + 1, close_count)`
# - Branch 2 (Close): If close_count < open_count, we can add a closing bracket ')' to match:
#   `backtrack(current_string + ')', open_count, close_count + 1)`
#
# Time Complexity: O(4^N / (N * sqrt(N))) - bounded by the N-th Catalan Number
# Space Complexity: O(N) - maximum height of recursion stack frame is 2N
#
# Common Interview Variations:
# 1. Generate all valid subsets (Power Set).
# 2. Letter Combinations of a Phone Number (LeetCode 17).

def generate_parentheses(n):
    res = []
    
    def backtrack(curr_str, open_c, close_c):
        # Base case
        if len(curr_str) == 2 * n:
            res.append(curr_str)
            return
            
        # Recursive step with constraint checking
        if open_c < n:
            backtrack(curr_str + "(", open_c + 1, close_c)
            
        if close_c < open_c:
            backtrack(curr_str + ")", open_c, close_c + 1)
            
    backtrack("", 0, 0)
    return res


# =====================================================================
# PROBLEM 2: Permutations
# =====================================================================
# Problem Statement:
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
#
# Approach:
# Swapping Backtracking:
# Define helper `backtrack(start_index)`:
# - Base Case: If start_index == len(nums), we have arranged all positions. Append a copy of nums to results.
# - Recursive step: Loop index 'i' from start_index to len(nums)-1:
#   - Swap nums[start_index] and nums[i] (decide which element goes to current position).
#   - Recursively solve next positions: `backtrack(start_index + 1)`.
#   - Swap back (backtrack/revert state swap) to restore original array order for subsequent loops.
#
# Time Complexity: O(N * N!) - N! permutations, each taking O(N) to copy/process
# Space Complexity: O(N) - recursion stack depth matches array length N
#
# Common Interview Variations:
# 1. Permutations II (input array contains duplicate values, requires skipping duplicate swaps).
# 2. Combinations (generate all subsets of size K).

def permute(nums):
    res = []
    
    def backtrack(start):
        # Base case
        if start == len(nums):
            res.append(nums[:])  # Append a shallow copy of current permutation
            return
            
        for i in range(start, len(nums)):
            # 1. State change: swap elements
            nums[start], nums[i] = nums[i], nums[start]
            
            # 2. Recurse next index
            backtrack(start + 1)
            
            # 3. Backtrack: restore original swap state
            nums[start], nums[i] = nums[i], nums[start]
            
    backtrack(0)
    return res


# =====================================================================
# PROBLEM 3: N-Queens
# =====================================================================
# Problem Statement:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other. Given an integer n, return all
# distinct solutions to the n-queens puzzle.
#
# Approach:
# Backtracking row-by-row with diagonal constraints:
# We maintain sets to track occupied columns, positive diagonals (row + col), and negative diagonals (row - col) in constant O(1) checks.
# Helper `backtrack(row, board)`:
# - Base Case: If row == n, we successfully placed queens on all rows. Format board and append to results.
# - Loop column 'col' from 0 to n-1:
#   - If column 'col' or diagonals are occupied, skip.
#   - State change: Place Queen at (row, col) (set board[row][col] = 'Q'), add col/diagonals to occupied sets.
#   - Recurse: `backtrack(row + 1, board)`.
#   - Backtrack: Remove Queen (set board[row][col] = '.'), remove col/diagonals from sets.
#
# Time Complexity: O(N!) - placing queens reduces search choices row-by-row
# Space Complexity: O(N^2) - board state matrix
#
# Common Interview Variations:
# 1. N-Queens II (returns total solution counts instead of layouts).
# 2. Sudoku Solver (backtracks cells 1 to 9).

def solve_n_queens(n):
    res = []
    board = [["."] * n for _ in range(n)]
    
    # Tracking sets to ensure no queen attacks another
    cols = set()
    pos_diag = set()  # row + col is constant
    neg_diag = set()  # row - col is constant
    
    def backtrack(r):
        # Base case
        if r == n:
            # Format rows of board to string lists
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
            
        for c in range(n):
            # Check constraints
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
                
            # 1. State change: Place Queen
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"
            
            # 2. Recurse next row
            backtrack(r + 1)
            
            # 3. Backtrack: Revert placement
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."
            
    backtrack(0)
    return res


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Generate Parentheses
    pairs = 3
    print("=======================================")
    print("Problem 1: Generate Parentheses")
    print(f"Input N: {pairs}")
    print(f"Output combinations: {generate_parentheses(pairs)}")
    
    # Test Problem 2: Permutations
    nums_list = [1, 2, 3]
    print("\n=======================================")
    print("Problem 2: Permutations")
    print(f"Input list: {nums_list}")
    print(f"Output Permutations:\n  {permute(nums_list)}")
    
    # Test Problem 3: N-Queens
    n_size = 4
    print("\n=======================================")
    print("Problem 3: N-Queens Puzzle")
    print(f"Board size N: {n_size}")
    solutions = solve_n_queens(n_size)
    print(f"Total solutions found: {len(solutions)}")
    if solutions:
        print("First solution layout:")
        for row_str in solutions[0]:
            print(f"  {row_str}")
    print("=======================================")

"""
Key Takeaways:
- Base cases prevent infinite recursion stack overflow crashes.
- Backtracking is characterized by: State change -> Recursive exploration -> Revert/Restore state.
- Set lookup hashing optimizes column and diagonal constraints checks to O(1) efficiency.

Interview Relevance:
- Always draw a decision state tree to trace the branching factor.
- Verify recursion limit boundaries for extreme scale inputs.

AI/ML Relevance:
- Game Theory Decision Trees: Backtracking forms the foundation of minimax search engines (like alpha-beta pruning in chess models).
- Neural Architecture Search (NAS): Algorithms explore structural choices recursively (selecting layer blocks/channels) and prune low-accuracy configurations.
"""
