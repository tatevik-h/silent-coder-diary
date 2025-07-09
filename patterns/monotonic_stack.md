# 🧱 Monotonic Stack Pattern

Monotonic Stack is a specialized stack that maintains elements in **monotonically increasing or decreasing order**. It is a powerful pattern for solving problems related to **next greater/smaller elements**, **stock span**, and **histogram-based** algorithms.

---

## 📌 When to Use

- Finding the next/previous greater or smaller element
- Calculating ranges (e.g., span of elements)
- Handling problems that require maintaining a stack of increasing or decreasing values
- Most often applied to **arrays** or **strings**

---

## 🔧 How It Works

- **Monotonic Increasing Stack**: Maintains elements such that the top is always the smallest (e.g. stack[-1] < current)
- **Monotonic Decreasing Stack**: Maintains elements such that the top is always the largest (e.g. stack[-1] > current)

---

## 🔄 Template (Increasing Stack)

```python
stack = []
for i in range(len(arr)):
    while stack and arr[stack[-1]] > arr[i]:
        stack.pop()
    stack.append(i)
```

## 🧠 Key Insight

- Avoids brute-force by maintaining helpful order in the stack  
- Each element is pushed and popped **at most once**  
- Allows solving **O(n²)** problems in **O(n)**

---

## ⏱️ Time & Space Complexity

- **Time**: O(n) — Every element is processed at most twice (once when pushed, once when popped)  
- **Space**: O(n) — Stack may hold all indices in the worst case
