# Data Structures & Algorithms: Strings (Module 08)

Strings in Python are immutable sequences of characters. Since strings cannot be changed in-place, string manipulation operations usually require creating new strings, meaning space complexity must be carefully monitored.

---

## Python String Operations Time & Space Complexity

| Operation | Time Complexity | Space Complexity | Reason |
| :--- | :--- | :--- | :--- |
| **Indexing (`s[i]`)** | $O(1)$ | $O(1)$ | Direct character lookup. |
| **Slicing (`s[i:j]`)** | $O(J - I)$ | $O(J - I)$ | Copies slice segment to a new string object. |
| **Splitting (`s.split()`)** | $O(N)$ | $O(N)$ | Scans entire string and creates list of word tokens. |
| **Joining (`"".join(list)`)** | $O(N)$ | $O(N)$ | Iterates list and consolidates memory blocks. |
| **Concatenation (`s1 + s2`)** | $O(M + N)$ | $O(M + N)$ | Instantiates a new string storing both arrays. |

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/strings/solutions.py), we implement the following three classic string interview problems:

1. **Valid Anagram**:
   * Determine if one string is a permutation of another using character frequency counts.
2. **Reverse Words in a String**:
   * Reverse the order of words in a sentence, cleaning up redundant internal spaces.
3. **Longest Palindromic Substring**:
   * Find the longest contiguous substring that reads the same forwards and backwards.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
