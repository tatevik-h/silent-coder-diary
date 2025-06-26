# Sliding Window Pattern

The **Sliding Window** technique is used to efficiently solve problems that involve arrays or strings and require checking **contiguous subarrays or substrings**.

---

## 🔍 When to Use

Use Sliding Window when:

- You need to **inspect subarrays/substrings** (contiguous elements)
- Brute-force is O(n²) or worse
- You can use a moving range (or window) and adjust its size while iterating

---

## 🧱 Two Types of Windows

### 1. Fixed-size Window

Used when the window size is known in advance.

Example: Find max sum of subarray of size `k`

```python
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)
```

### 2. Dynamic-Size Sliding Window

This type of window **grows and shrinks dynamically** based on a constraint, such as avoiding duplicate characters, matching a target sum, or meeting frequency conditions.

---

## 📌 Use It When:

- The **window size is not fixed**
- You need to **shrink or expand** the window based on a specific **condition**
- You want to **optimize** brute-force approaches with **sets or hash maps** to track state

---

## 🔧 Template

```python
left = 0
for right in range(len(arr)):
    # Expand the window
    update_window(arr[right])

    while condition_is_invalid():
        # Shrink the window
        remove_from_window(arr[left])
        left += 1

    # Update result if needed
    update_result(right, left)
```

## 🧠 Key Insight

- Efficiency comes from **avoiding reprocessing overlapping elements**.
- Each element is **examined at most twice** — once when it's **added** to the window, and once when it's **removed**.
- Many brute-force `O(n²)` problems can be reduced to a linear time solution using this technique — **`O(n)`**.

---

## ⏱️ Time & Space Complexity

### Time: `O(n)`
- Each element is **processed a limited number of times**:
  - Once when the window expands (`right` pointer)
  - Once when the window shrinks (`left` pointer)

### Space: `O(k)`
- `k` is the number of **unique elements** inside the current window.
- Most implementations use a **`set`** or a **`dictionary`** to track the state of the window.

