# 🧠 Greedy Algorithms

Greedy algorithms are a category of algorithms that make the **locally optimal choice at each step** with the hope of finding a global optimum.

---

## 📌 When to Use Greedy Algorithms
- When the problem has **optimal substructure** (an optimal solution can be constructed from optimal solutions of its subproblems).
- When **local choices** lead to a **global optimum**.
- When **no need to revisit decisions**.
- When **overlapping subproblems or dynamic state** tracking is not needed (unlike DP).

---

## 🔧 Characteristics of Greedy Algorithms
- **Greedy Choice Property**: A global optimum can be arrived at by choosing a local optimum.
- **Optimal Substructure**: A problem has an optimal solution that can be constructed efficiently from optimal solutions to its subproblems.

---

## 🔁 Greedy Algorithm Template
```python
# Pseudocode
sort(data or prioritize by condition)
result = []
for item in data:
    if item meets condition:
        take item (greedy choice)
```

## 🧠 Key Insight

- Greedy is simple and fast.
- Often easier to implement than Dynamic Programming.
- Doesn’t always guarantee the optimal solution unless the problem has specific properties (like **Greedy Choice** and **Optimal Substructure**).

---

## ⏱️ Time & Space Complexity

### Time Complexity:
- **O(n log n)** – if sorting is involved
- **O(n)** – if scanning only without sorting

### Space Complexity:
- **O(1)** – if only constant extra space is used
- **O(n)** – if using additional data structures (e.g., for tracking results)

---

## 🔍 Examples in Theory

- **Activity Selection Problem**
- **Huffman Coding**
- **Interval Scheduling**
- **Fractional Knapsack Problem**
- **Minimum Number of Coins** (in specific coin systems)
