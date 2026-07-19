"""
Topic:
Dynamic Programming (DP) Basics

Importance:
Dynamic Programming optimizes recursive overlaps by caching solved sub-states.
Converting exponential O(2^N) recursions to polynomial/linear checks is highly
demanded in placements to solve pathing and optimization challenges.

This file covers:
- Problem 1: Climbing Stairs (1D DP - Space Optimized)
- Problem 2: Coin Change (1D DP Tabulation)
- Problem 3: 0/1 Knapsack Problem (2D DP Tabulation)
"""

# =====================================================================
# PROBLEM 1: Climbing Stairs
# =====================================================================
# Problem Statement:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Approach:
# Fibonacci recurrence relation: dp[i] = dp[i-1] + dp[i-2].
# Base cases: dp[1] = 1, dp[2] = 2.
# Instead of storing an entire DP array of size n, we optimize space by maintaining
# only two variables tracking the last two steps.
#
# Time Complexity: O(N) - single iteration up to n
# Space Complexity: O(1) - only two variables tracked
#
# Common Interview Variations:
# 1. Min Cost Climbing Stairs (each step has a cost, minimize sum).
# 2. Decode Ways (LeetCode 91).

def climb_stairs(n):
    if n <= 2:
        return n
        
    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2
    
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
        
    return prev1


# =====================================================================
# PROBLEM 2: Coin Change
# =====================================================================
# Problem Statement:
# Given an integer array coins representing coins of different denominations and an
# integer amount representing a total amount of money, return the fewest number of
# coins that you need to make up that amount.
# If that amount cannot be made up by any combination of the coins, return -1.
#
# Approach:
# Bottom-Up 1D DP Tabulation:
# 1. Initialize `dp` array of size `amount + 1` filled with float('inf') representing unreachable states.
# 2. Base case: `dp[0] = 0` (0 coins to make amount 0).
# 3. For target value `i` from 1 to amount:
#    - For each coin in coins:
#      - If i - coin >= 0:
#        - dp[i] = min(dp[i], 1 + dp[i - coin])
# 4. Return dp[amount] if not float('inf') else -1.
#
# Time Complexity: O(Amount * C) - where C is the number of coins denominations
# Space Complexity: O(Amount) - to store the DP tabulation array
#
# Common Interview Variations:
# 1. Coin Change II (return total combinations to make sum).
# 2. Combination Sum IV (LeetCode 377).

def coin_change(coins, amount):
    # Initialize table with infinity representing unreachable amount
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
                
    return dp[amount] if dp[amount] != float("inf") else -1


# =====================================================================
# PROBLEM 3: 0/1 Knapsack Problem
# =====================================================================
# Problem Statement:
# Given weights and values of N items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack.
# You cannot break items (either take whole item or leave it).
#
# Approach:
# Bottom-Up 2D DP Tabulation:
# Create matrix `dp` of size `(N + 1) x (W + 1)`:
# - dp[i][w] represents maximum value obtainable from first 'i' items with capacity limit 'w'.
# For item index i from 1 to N, and capacity w from 1 to W:
# - If wt[i-1] <= w (item fits):
#   - dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]) (take item vs skip item)
# - Else (item does not fit):
#   - dp[i][w] = dp[i-1][w]
# Return dp[N][W].
#
# Time Complexity: O(N * W) - nested iteration of items and capacities
# Space Complexity: O(N * W) - 2D matrix storage (can be optimized to O(W) using 1D row array)
#
# Common Interview Variations:
# 1. Partition Equal Subset Sum (split list into equal sum partitions, subset sum variation).
# 2. Target Sum (assign +/- signs to reach target).

def knapsack(wt, val, W):
    n = len(val)
    # Create 2D DP table initialized to 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            item_weight = wt[i - 1]
            item_value = val[i - 1]
            
            if item_weight <= w:
                # Max of including the item vs excluding the item
                dp[i][w] = max(item_value + dp[i - 1][w - item_weight], dp[i - 1][w])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][W]


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Climbing Stairs
    steps = 5
    print("=======================================")
    print("Problem 1: Climbing Stairs")
    print(f"Number of stairs: {steps}")
    print(f"Unique ways to climb: {climb_stairs(steps)}")  # Expected 8
    
    # Test Problem 2: Coin Change
    coins_list = [1, 2, 5]
    target_amount = 11
    print("\n=======================================")
    print("Problem 2: Coin Change (Min coins)")
    print(f"Coins: {coins_list} | Target Amount: {target_amount}")
    print(f"Fewest coins needed: {coin_change(coins_list, target_amount)}")  # Expected 3 (5 + 5 + 1)
    
    # Test Problem 3: 0/1 Knapsack
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    print("\n=======================================")
    print("Problem 3: 0/1 Knapsack Problem")
    print(f"Values: {values} | Weights: {weights} | Capacity limit: {capacity}")
    print(f"Maximum value obtainable: {knapsack(weights, values, capacity)}")  # Expected 220 (weights 20 + 30)
    print("=======================================")

"""
Key Takeaways:
- Dynamic Programming caches overlapping results to optimize runtimes from O(2^N) to polynomial speeds.
- Space optimizations from O(N) to O(1) are achieved by keeping only active dependent variables.
- Tabulation checks base cases first, preventing recursive call stack memory overheads.

Interview Relevance:
- Always check if the recursion state repeats overlapping branches before writing DP solutions.
- Be comfortable explaining Top-Down (Memoization) vs Bottom-Up (Tabulation).

AI/ML Relevance:
- Reinforcement Learning: Value iteration (Bellman equations) updates state-value mappings using dynamic programming tabulation.
- Viterbi Decoding: Hidden Markov Models (HMMs) find the most likely sequence of hidden states using DP path metrics calculations.
"""
