"""
Topic:
Linked List Coding Problems

Importance:
Linked lists teach node-link references and sequential pointer manipulation.
Mastering operations like reversals, cycle checks, and splicing builds pointer manipulation skills.

This file covers:
- Singly Linked List Node representation
- Problem 1: Reverse a Singly Linked List
- Problem 2: Linked List Cycle Detection (Floyd's Algorithm)
- Problem 3: Merge Two Sorted Linked Lists
"""

# =====================================================================
# NODE DEFINITION
# =====================================================================

class ListNode:
    """A standard node in a singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # Helper string representation to inspect list print output
        res = []
        curr = self
        visited = set()  # prevent infinite loop in cycles
        while curr:
            if curr in visited:
                res.append(f"Cycle detected at node({curr.val})")
                break
            res.append(str(curr.val))
            visited.add(curr)
            curr = curr.next
        return " -> ".join(res)


# =====================================================================
# PROBLEM 1: Reverse a Singly Linked List
# =====================================================================
# Problem Statement:
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Approach:
# Three-Pointer Iterative:
# We maintain three pointers:
# - 'prev' (initially None)
# - 'curr' (initially head)
# - 'next_node' (temporary holder)
# Loop while curr is not None:
# - Store the next node: next_node = curr.next.
# - Reverse current node's link: curr.next = prev.
# - Move 'prev' pointer forward: prev = curr.
# - Move 'curr' pointer forward: curr = next_node.
# Return 'prev' as the new head.
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(1) - in-place reversal
#
# Common Interview Variations:
# 1. Reverse Linked List II (reverse a subsegment from index left to right).
# 2. Reverse Nodes in K-Group (Hard).

def reverse_list(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next  # save next node
        curr.next = prev       # reverse link direction
        prev = curr            # shift prev forward
        curr = next_node       # shift curr forward
        
    return prev


# =====================================================================
# PROBLEM 2: Linked List Cycle Detection
# =====================================================================
# Problem Statement:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer.
#
# Approach:
# Floyd's Cycle-Finding Algorithm (Tortoise and Hare):
# Initialize two pointers, 'slow' and 'fast', at the head.
# - 'slow' moves one step at a time: slow = slow.next.
# - 'fast' moves two steps at a time: fast = fast.next.next.
# If fast reaches None (or fast.next reaches None), there is no cycle (return False).
# If slow and fast meet at any node, a cycle exists (return True).
#
# Time Complexity: O(N) - fast pointer catches slow pointer in linear steps
# Space Complexity: O(1) - only two pointers tracked
#
# Common Interview Variations:
# 1. Find the starting node of the cycle (once met, reset slow to head, move both 1 step at a time until they meet again).
# 2. Find length of cycle.

def has_cycle(head):
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If pointers meet, there is a cycle
        if slow == fast:
            return True
            
    return False


# =====================================================================
# PROBLEM 3: Merge Two Sorted Linked Lists
# =====================================================================
# Problem Statement:
# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Approach:
# Dummy Head Pointer:
# Create a dummy node ('dummy') to anchor the merged list, and a pointer 'curr' to track the tail.
# Loop while both list1 and list2 are not None:
# - Compare their head values. Link 'curr.next' to the smaller node.
# - Shift that list's pointer forward.
# - Move 'curr' forward.
# Attach remaining non-empty list segment (curr.next = list1 or list2).
# Return dummy.next.
#
# Time Complexity: O(M + N) - where M and N are lengths of list1 and list2
# Space Complexity: O(1) - nodes are spliced in-place without duplicating structures
#
# Common Interview Variations:
# 1. Merge K Sorted Lists (solved using Min-Heap / Priority Queue).
# 2. Sort a Linked List (solved in O(N log N) time and O(log N) space using Merge Sort).

def merge_two_lists(list1, list2):
    dummy = ListNode(-1)
    curr = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
        
    # Append the remaining nodes of whichever list is not empty
    curr.next = list1 if list1 else list2
    
    return dummy.next


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Helper to construct linked list from standard list
    def make_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        curr = head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    # Test Problem 1: Reverse List
    list_1 = make_list([1, 2, 3, 4, 5])
    print("=======================================")
    print("Problem 1: Reverse a Singly Linked List")
    print(f"Input: {list_1}")
    print(f"Output (Reversed): {reverse_list(list_1)}")
    
    # Test Problem 2: Cycle Detection
    list_2 = make_list([3, 2, 0, -4])
    # Create cycle manually: link node(-4) -> node(2)
    node_minus_four = list_2.next.next.next
    node_two = list_2.next
    node_minus_four.next = node_two  # creates cycle
    print("\n=======================================")
    print("Problem 2: Linked List Cycle Detection")
    # print(list_2) would print representation showing cycle loop
    print(f"Cycle detected status: {has_cycle(list_2)}")
    
    # Test Problem 3: Merge Sorted Lists
    list_3_a = make_list([1, 2, 4])
    list_3_b = make_list([1, 3, 4])
    print("\n=======================================")
    print("Problem 3: Merge Two Sorted Linked Lists")
    print(f"Input A: {list_3_a} | Input B: {list_3_b}")
    print(f"Output (Merged): {merge_two_lists(list_3_a, list_3_b)}")
    print("=======================================")

"""
Key Takeaways:
- Linked lists do not support index offsetting, requiring sequential traversal (O(N) search).
- Reversals occur in-place by maintaining a temp `next_node` holder variable to prevent breaking link sequences.
- Floyd's cycle detection checks loop intersections in constant space.

Interview Relevance:
- Always check for null boundaries (empty head, single nodes).
- Practice drawing node connections to verify pointer assignments.

AI/ML Relevance:
- Graph Architectures: Nodes in neural graphs (DAGs) link to successor layers using neighbor pointer lists.
- Memory Pointers: Dynamic C/C++ backend engines (like PyTorch tensor memory allocations) route blocks using linked list trackers.
"""
