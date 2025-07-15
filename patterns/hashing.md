# 🧩 Hashing / HashMap Patterns 

Hashing is a technique used to **store and retrieve data in constant time** (average case). It’s implemented using data structures like **HashMaps** and **HashSets**, and is especially useful when dealing with **frequency counts**, **duplicates**, and **pair matching**.

---

## 📌 When to Use

Use hashing when:

- You need to **check for duplicates** quickly.
- You want to **count the frequency** of elements.
- You need to **track presence** of elements (e.g. Two Sum).
- You need to **group** or **bucket** data by common traits.
- You want to **compare unordered collections** (like anagrams).

---

## 🔧 Core Techniques

### 🔍 Lookup / Membership Test

- Use `set()` to check if an element exists in O(1) time.

### 🔁 Frequency Counting

- Use `collections.Counter` or a `defaultdict(int)`.

### 🔄 Prefix Sum Tracking

- Store cumulative sums in a hash map to avoid nested loops.

### 🧠 Value to Index Mapping

- Store value:index pairs when solving pair problems.

---

## 🧠 Key Insight

- Hashing **avoids brute-force** by storing partial results for reuse.
- When scanning an array once, store what you’ve seen so far.
- Combine with other patterns (Two Pointers, Sliding Window) for more complex problems.

---

## ⏱️ Time & Space Complexity

### Time Complexity:

- Lookup / Insert in hash maps: **O(1)** average
- Sorting + hash map: **O(n log n)**
- Nested map operations (rare): **O(n²)**

### Space Complexity:

- HashMap/Set stores: **O(n)**
- Some problems may use additional arrays or nested maps.

---

## 🧪 Common Use Cases

| Use Case                      | Example Problem            |
| ----------------------------- | -------------------------- |
| Duplicate detection           | Contains Duplicate         |
| Pair sum lookup               | Two Sum                    |
| Frequency counter             | Valid Anagram, Ransom Note |
| Subarray prefix sums          | Subarray Sum Equals K      |
| Grouping                      | Group Anagrams             |
| Sliding Window with frequency | Permutation in String      |

---

## 🧰 Python Tools

```python
from collections import defaultdict, Counter

# Basic dictionary usage
d = {}
d[key] = value

# Default dictionary for frequency
freq = defaultdict(int)
freq[char] += 1

# Counter for direct frequency counting
c = Counter(some_list_or_string)

# Set for membership
seen = set()
if val in seen:
    ...
```

## ⏱️ Time & Space Complexity

### ⌛ Time Complexity

- **O(1)** average case for insert, delete, and lookup in a hash map or hash set
- **O(n)** when iterating over an array once and using hashing to track elements
- **O(n log n)** if the problem involves sorting before or after hashing
- **O(n²)** in rare cases with nested hash operations or collision-heavy data

### 🗃️ Space Complexity

- **O(n)** in most problems — to store all elements or counts in a map/set
- **O(1)** if no extra data structures are used (less common in hashing problems)

## 🔍 Recognizing Hashing Pattern Problems

Look for keywords or requirements like:

- "Find pair / subarray / indices that sum to X"
- "Check if there are duplicates"
- "Group items with similar structure"
- "Find longest/shortest subarray with a property"
- "Track frequency / number of times something appears"

## ⚠️ Common Pitfalls with Hashing

- **Hash collisions:** Rare in Python, but know that `O(1)` can degrade to `O(n)` in worst-case.
- **Mutable keys:** Lists and dictionaries cannot be keys in a hash map.
- **Order isn't guaranteed** (use `OrderedDict` if needed).
- **Set vs Dictionary:** Use `set()` when values don’t matter, just presence.
