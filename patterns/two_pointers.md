# Two Pointers Pattern

---

## 📌 Core Idea

The Two Pointers technique involves using **two indices (pointers)** to traverse an array or string—often moving from opposite ends or in the same direction—to achieve optimal time and space efficiency when solving various problems.

---

## 🧠 When to Use

- **Sorted Data**: The input array or string is sorted or has some inherent order.  
- **Pair/Subarray Problems**: You need to find pairs, triplets, or subarrays that satisfy a condition (sum, difference, etc.).  
- **In-Place Operations**: You want to modify or inspect the data without extra memory overhead.  
- **Linear Traverse**: You can decide pointer movement based on comparisons (e.g., sum < target → move left pointer).

---

## ⚙️ General Approach

1. **Initialize** two pointers:  
   ```python
   left, right = 0, len(arr) - 1


2. Loop while `left < right`:  
   - Compute `current = arr[left] + arr[right]` (or other condition)  
   - If `current` meets the target condition → return or record result  
   - If `current < target` → `left += 1`  
  - Else → `right -= 1`

3. End when pointers cross or result found.
