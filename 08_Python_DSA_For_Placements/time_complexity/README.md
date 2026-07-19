# Complexity Analysis: Time & Space Complexity

Complexity analysis is the framework used to estimate the resources (time and memory) an algorithm consumes relative to the size of its input ($N$). It is the single most critical concept in technical interviews.

---

## 1. Asymptotic Notations

Asymptotic notations describe the behavior of algorithms as the input size approaches infinity ($N \to \infty$).

1. **Big-O ($O$) - Upper Bound**:
   * Represents the **worst-case scenario**.
   * It guarantees that the execution time will not exceed this limit.
   * *Example*: Linear search takes $O(N)$ time.
2. **Big-Omega ($\Omega$) - Lower Bound**:
   * Represents the **best-case scenario**.
   * It guarantees that the execution will take at least this much time.
   * *Example*: Linear search takes $\Omega(1)$ time (if the target is at the first index).
3. **Big-Theta ($\Theta$) - Tight Bound**:
   * Represents the **average-case scenario** (when upper and lower bounds match).
   * Describes exact behavior.
   * *Example*: Accessing array element by index takes $\Theta(1)$ time.

---

## 2. Common Time Complexities

| Notation | Name | Description / Example |
| :--- | :--- | :--- |
| **$O(1)$** | Constant Time | Operation execution does not depend on input size. E.g. Hash Map lookup, index array access. |
| **$O(\log N)$** | Logarithmic Time | Search space is divided by half in every step. E.g. Binary Search. |
| **$O(N)$** | Linear Time | Every element is visited exactly once. E.g. Iterating a list, finding min/max. |
| **$O(N \log N)$** | Linearithmic Time | Divide-and-conquer sorting algorithms. E.g. Merge Sort, Quick Sort (average), Timsort. |
| **$O(N^2)$** | Quadratic Time | Nested loops iterating over the same dataset. E.g. Bubble Sort, checking all pairs. |
| **$O(2^N)$** | Exponential Time | Recursive algorithms splitting calls into branches. E.g. Naive recursive Fibonacci. |
| **$O(N!)$** | Factorial Time | Generating all permutations of a set. E.g. Traveling Salesperson brute-force. |

---

## 3. Rules for Complexity Calculation

When analyzing a block of code, follow these three rules:

1. **Drop Constants**:
   * $O(2N + 5) \to O(N)$
   * $O(500) \to O(1)$
2. **Drop Non-Dominant Terms**:
   * $O(N^2 + N) \to O(N^2)$
   * $O(N \log N + N^2) \to O(N^2)$
3. **Sequence vs Nesting**:
   * **Sequence**: Add complexities ($O(A) + O(B) = O(A + B)$).
   * **Nesting**: Multiply complexities ($O(A) \times O(B) = O(A \times B)$).

---

## 4. Space Complexity

Space complexity measures the total memory space required by the algorithm relative to the input size, including:
1. **Auxiliary Space**: Extra space created by the algorithm (e.g. temporary lists).
2. **Input Space**: Space occupied by inputs.
3. **Recursion Stack Space**: Memory consumed by call frames on stack during recursion.

---

## 5. Typical Placement Interview Questions

### Q1. What is the Time & Space Complexity of a recursive function?
* **Time Complexity**: Proportional to the number of recursive calls made. E.g. Fibonacci call tree height.
* **Space Complexity**: Proportional to the maximum height of the recursion call stack (active stack frames in memory).

### Q2. How does Python's `list.sort()` manage complexity?
* Python uses **Timsort** (a hybrid of Merge Sort and Insertion Sort).
* **Time Complexity**: Worst-case is $O(N \log N)$, Best-case is $O(N)$ (if array is already sorted).
* **Space Complexity**: $O(N)$ auxiliary memory.
