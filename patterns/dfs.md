# Depth-First Search (DFS)

## 1. What is DFS?
**Depth-First Search (DFS)** is a traversal algorithm used on **trees** and **graphs**.  
It explores nodes by going **as deep as possible** along a path before backtracking.

DFS = *Explore → Go Deep → Backtrack*

---

## 2. Key Characteristics
- **Recursive or Stack-based** (explicit stack)
- Explores **depth** before **breadth**
- Can be used on:
  - Trees
  - Directed graphs
  - Undirected graphs
  - Cyclic or acyclic structures
- Requires **visited set** (in graphs) to avoid infinite loops

---

## 3. DFS Variants (Tree Traversals)
DFS has natural forms inside binary trees:

### 3.1 Preorder Traversal  
`Root → Left → Right`  
Used when you want to **copy** or **serialize** a tree.

### 3.2 Inorder Traversal  
`Left → Root → Right`  
- Only meaningful for **Binary Search Trees (BSTs)**
- Returns **sorted order**

### 3.3 Postorder Traversal  
`Left → Right → Root`  
Used for tasks like **evaluating expressions**, **deleting trees**, etc.

---

## 4. DFS Implementation (Graph)

### Recursive version
```python
def dfs(node, visited=set()):
    if node in visited:
        return
    visited.add(node)
    for nei in graph[node]:
        dfs(nei, visited)
