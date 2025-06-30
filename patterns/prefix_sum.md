# 📊 Prefix Sum Pattern

The **Prefix Sum** (also known as **Cumulative Sum**) is a powerful technique used to efficiently compute the sum of elements within a range of an array. It's especially useful in problems involving subarray sums, range queries, or frequency counts.

---

## 🧠 What Is Prefix Sum?

Prefix Sum helps avoid recomputing sums over and over again.  
We precompute a `prefix` array where:

```prefix[i] = arr[0] + arr[1] + ... + arr[i]```


Then, the sum of a subarray from index `i` to `j` can be computed as:

```range_sum(i, j) = prefix[j] - prefix[i - 1]```


Special case:
- If `i = 0`, then `range_sum(0, j) = prefix[j]`

---

## 🔧 Basic Implementation

```python
def build_prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix
```

## 💡 When to Use

Use **Prefix Sum** when:

- You need to calculate the **sum of elements in multiple subarrays**
- You're dealing with **sliding sums** or **range-based queries**
- You're solving problems like:
  - ✅ Count subarrays with a specific sum
  - ✅ Range sum queries
  - ✅ Frequency of patterns based on counts

 
## ⏱️ Time & Space Complexity

| Operation                                 | Time Complexity | Space Complexity |
|-------------------------------------------|------------------|-------------------|
| Building the prefix sum array             | O(n)             | O(n)              |
| Querying sum in a range (i to j)          | O(1)             | —                 |
| Subarray sum with hash map (e.g. LeetCode 560) | O(n)         | O(n)              |

🧠 Note:
- Prefix arrays allow constant-time sum queries after O(n) preprocessing.
- When using hash maps for prefix tracking, extra space is needed for storing prefix sums and frequencies.



