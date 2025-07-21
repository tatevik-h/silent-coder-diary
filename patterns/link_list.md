# Linked List — Explanation and Overview

## What is a Linked List?
A **Linked List** is a linear data structure where each element (called a **node**) contains two parts:

- **Data**: The actual value stored.
- **Next**: A reference (or pointer) to the next node in the sequence.

Unlike arrays, linked lists store elements in non-contiguous memory locations and use pointers to link nodes.

---

## Types of Linked Lists

### Singly Linked List
Each node points only to the next node. Traversal is one-way.

### Doubly Linked List
Each node contains two pointers: one to the next node and one to the previous node. Allows bi-directional traversal.

### Circular Linked List
The last node points back to the head node, forming a circle. Can be singly or doubly linked.

---

## Basic Operations

### 1. Traversal
- **Description**: Start from the head node and follow the `next` pointers until reaching `null` (end).
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### 2. Insertion
- **At the beginning**: 
  - **Time**: O(1)  
  - **Space**: O(1)  
- **At the end**: 
  - **Time**: O(n) (need to traverse to the end)  
  - **Space**: O(1)  
- **At a position**: 
  - **Time**: O(n)  
  - **Space**: O(1)

### 3. Deletion
- **At the beginning**: 
  - **Time**: O(1)  
  - **Space**: O(1)
- **At the end**: 
  - **Time**: O(n)  
  - **Space**: O(1)
- **At a position**: 
  - **Time**: O(n)  
  - **Space**: O(1)

---

## Advantages
- Dynamic size (can grow or shrink at runtime)
- Ease of insertion/deletion (no need to shift elements as in arrays)
- Efficient for operations at the head or tail (with a tail pointer)

---

## Disadvantages
- No random access (must traverse nodes sequentially)
- Extra memory required for storing pointers
- Poor cache locality compared to arrays

---

## Common Patterns & Techniques

### 🔁 Two Pointers (Fast and Slow)
Used for:
- Detecting cycles (Floyd’s Cycle-Finding Algorithm)
- Finding the middle node of a linked list
- Checking if a linked list is a palindrome

### 🧷 Dummy Node Technique
- Used to simplify edge cases during insertion/deletion, especially at the head.

### 🔄 Recursion
- Useful for:
  - Reversing a linked list
  - Printing nodes in reverse order
- Watch for stack overflow on large inputs.

---

## Summary Table of Time Complexity

| Operation         | Singly Linked List | Doubly Linked List | Circular Linked List |
|------------------|--------------------|---------------------|-----------------------|
| Access (index)   | O(n)               | O(n)                | O(n)                  |
| Search (by value)| O(n)               | O(n)                | O(n)                  |
| Insert at Head   | O(1)               | O(1)                | O(1)                  |
| Insert at Tail   | O(n) or O(1)\*     | O(n) or O(1)\*      | O(1)\*                |
| Delete at Head   | O(1)               | O(1)                | O(1)                  |
| Delete at Tail   | O(n)               | O(1)                | O(n)\*                |

> \* If tail pointer is maintained

---

Let me know if you'd like me to add:
- Python code templates (e.g., `ListNode` class)
- Common LeetCode linked list problems
- Visual illustrations (ASCII or image-based)
