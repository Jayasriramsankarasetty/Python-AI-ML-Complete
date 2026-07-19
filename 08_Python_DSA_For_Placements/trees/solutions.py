"""
Topic:
Binary Tree and Binary Search Tree (BST) Coding Problems

Importance:
Trees form hierarchical graphs. Tree traversals (Inorder, Preorder, Postorder) and DFS heights calculations
are classic interview requirements, which form the base for Decision Trees and random forest paths.

This file covers:
- TreeNode class representation
- Problem 1: Tree Traversals (Inorder, Preorder, Postorder)
- Problem 2: Maximum Depth of Binary Tree
- Problem 3: Validate Binary Search Tree (BST)
"""

# =====================================================================
# TREENODE DEFINITION
# =====================================================================

class TreeNode:
    """A standard node in a binary tree"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =====================================================================
# PROBLEM 1: Binary Tree Traversals
# =====================================================================
# Problem Statement:
# Implement inorder, preorder, and postorder depth-first traversals on a binary tree recursively.
#
# Approach:
# Recursive DFS Traversals:
# - Inorder: Traverse left, visit root, traverse right.
# - Preorder: Visit root, traverse left, traverse right.
# - Postorder: Traverse left, traverse right, visit root.
#
# Time Complexity: O(N) - visits each of the N nodes exactly once
# Space Complexity: O(N) - recursion stack memory (worst case O(N) if tree is skewed, average O(log N) if balanced)
#
# Common Interview Variations:
# 1. Level Order Traversal (Breadth First Search BFS, solved using a Queue).
# 2. Zigzag Level Order Traversal.

def inorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result

def preorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.val)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)
    return result

def postorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.val)
    return result


# =====================================================================
# PROBLEM 2: Maximum Depth of Binary Tree
# =====================================================================
# Problem Statement:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
# Approach:
# Recursive DFS (Height Calculation):
# - Base Case: If root is None, return depth of 0.
# - Recursive step: Calculate maximum depth of left sub-tree and right sub-tree.
# - Return 1 + max(left_depth, right_depth).
#
# Time Complexity: O(N) - visits each node once
# Space Complexity: O(N) - recursion stack frame space
#
# Common Interview Variations:
# 1. Minimum Depth of Binary Tree (stops at first leaf node encountered).
# 2. Balanced Binary Tree check (checks if left and right heights differ by at most 1 at every node).

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# =====================================================================
# PROBLEM 3: Validate Binary Search Tree (BST)
# =====================================================================
# Problem Statement:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# 1. The left subtree of a node contains only nodes with keys less than the node's key.
# 2. The right subtree of a node contains only nodes with keys greater than the node's key.
# 3. Both the left and right subtrees must also be binary search trees.
#
# Approach:
# Recursive Range Bounds:
# A node's value must lie strictly between a 'low' and 'high' bound.
# - Initialize validation with low = float('-inf'), high = float('inf').
# - Base Case: If root is None, return True.
# - If root.val <= low or root.val >= high, return False (violates BST property).
# - Recursively validate left subtree: range becomes [low, root.val].
# - Recursively validate right subtree: range becomes [root.val, high].
# Both subtrees must return True.
#
# Time Complexity: O(N) - visits each node once
# Space Complexity: O(N) - recursion stack
#
# Common Interview Variations:
# 1. Find the K-th smallest element in a BST (solved by keeping track of count during inorder traversal).
# 2. Lowest Common Ancestor (LCA) in a BST.

def validate_bst_helper(node, low, high):
    if not node:
        return True
        
    # Check value bounds
    if node.val <= low or node.val >= high:
        return False
        
    # Recurse:
    # - Left child must be in range [low, node.val]
    # - Right child must be in range [node.val, high]
    return (validate_bst_helper(node.left, low, node.val) and 
            validate_bst_helper(node.right, node.val, high))

def is_valid_bst(root):
    return validate_bst_helper(root, float('-inf'), float('inf'))


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Constructing a sample binary search tree:
    #        4
    #       / \
    #      2   5
    #     / \
    #    1   3
    tree_root = TreeNode(4)
    tree_root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    tree_root.right = TreeNode(5)
    
    # Test Problem 1: Traversals
    print("=======================================")
    print("Problem 1: Binary Tree DFS Traversals")
    print(f"Inorder Traversal:   {inorder_traversal(tree_root)}")
    print(f"Preorder Traversal:  {preorder_traversal(tree_root)}")
    print(f"Postorder Traversal: {postorder_traversal(tree_root)}")
    
    # Test Problem 2: Maximum Depth
    print("\n=======================================")
    print("Problem 2: Maximum Depth of Binary Tree")
    print(f"Output Max Depth: {max_depth(tree_root)}")  # expected 3 (4 -> 2 -> 1)
    
    # Test Problem 3: Validate BST
    print("\n=======================================")
    print("Problem 3: Validate Binary Search Tree (BST)")
    print(f"Tree is valid BST? {is_valid_bst(tree_root)}")  # expected True
    
    # Modify to make it invalid BST: set left child of 2 to value 10
    tree_root.left.left.val = 10
    print(f"After modifying leaf value to 10...")
    print(f"Tree is valid BST? {is_valid_bst(tree_root)}")  # expected False
    print("=======================================")

"""
Key Takeaways:
- Traversing a BST inorder yields elements in sorted ascending order.
- To validate a BST, it is not enough to check `left.val < node.val < right.val` locally. The node must satisfy inheritance bounds defined by ancestral decisions.
- Recursive height checks scale with depth heights.

Interview Relevance:
- Always clarify if tree values can be duplicate or negative.
- Explain recursive vs iterative stack space usage (iterative traversals use an explicit stack list to avoid call stack limits).

AI/ML Relevance:
- Decision Tree Classifiers: Tree traversal algorithms determine split conditions sequentially along left and right branches (e.g. `feature_value <= threshold`) during inference.
- Graph Neural Networks (GNN): Nodes propagate information to parent layers along child networks similarly to recursive DFS traversals.
"""
