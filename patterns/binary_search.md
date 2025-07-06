# 🔍 Binary Search Pattern

Binary Search is a fundamental algorithm used to efficiently search sorted arrays. It's the foundation for many optimized solutions involving ordered data or monotonic behaviors.

---

## 💡 When to Use

Use binary search when:

- The input data is **sorted** (ascending/descending).
- You need to **search for an element** or determine its **position**.
- You're solving problems with **monotonic functions** or range-based decisions.

---

## 🧠 Key Insight

Binary Search repeatedly divides the search space in half, reducing the time complexity from O(n) to **O(log n)**.

You maintain two pointers: `left` and `right`, and narrow the range based on comparisons with a calculated midpoint.

---

## 🔧 Template

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # or return True

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    
    return -1  # or False if not found
```

## ⏱️ Time & Space Complexity

| Algorithm Variant            | Time Complexity | Space Complexity | Notes                                |
|-----------------------------|------------------|------------------|--------------------------------------|
| Standard Binary Search      | O(log n)         | O(1)             | Iterative approach                   |
| Recursive Binary Search     | O(log n)         | O(log n)         | Due to recursive call stack          |
| First/Last Occurrence       | O(log n)         | O(1)             | Binary search with boundary tracking |
| Peak Element in Mountain    | O(log n)         | O(1)             | Monotonic array structure            |
| Binary Search on Answer     | O(log(max−min))  | O(1)             | Often used in optimization problems  |

### 📌 Why O(log n)?

In each step of the binary search:

- The search space is divided by 2
- So the number of steps required is roughly log₂(n)
- Example: for a list of 1,000,000 elements, binary search finds the answer in about 20 steps
