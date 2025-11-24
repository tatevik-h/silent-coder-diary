# Breadth-First Search (BFS)

## 1. What is BFS?

**Breadth-First Search (BFS)** is a graph traversal algorithm that explores nodes **level by level**.  
Starting from a given source node, it first visits all nodes at distance 1, then distance 2, and so on.

BFS is especially useful because:

- It finds the **shortest path** in **unweighted graphs**  
- It guarantees **minimum number of edges** from source to each reachable node  
- It avoids infinite loops with the help of a **visited** set  

---

## 2. How BFS Works (Algorithm)

### Pseudocode

```python
def bfs(graph, start):
    queue = [start]
    visited = {start}

    while queue:
        node = queue.pop(0)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
              queue.append(neighbor)
```
## Key Components

- **Queue (FIFO):** ensures processing order is by distance (levels)  
- **Visited Set:** prevents revisiting nodes and avoids cycles  
- **Adjacency List/Matrix:** graph representation  

### Why BFS Uses a Queue
Because BFS must process nodes in the exact order they are discovered → **first discovered = first processed**.

---

## 3. Time Complexity of BFS

### Time Complexity

| Graph Representation | BFS Time Complexity |
|----------------------|--------------------|
| **Adjacency List**   | **O(V + E)**       |
| **Adjacency Matrix** | **O(V²)**          |

Where:

- **V = number of vertices**  
- **E = number of edges**

BFS touches every vertex once and every edge once → **O(V + E)**.

---

## 4. Space Complexity of BFS

BFS requires memory for:

- **Queue** → up to **O(V)** in the worst case  
- **Visited Set** → **O(V)**  
- Optional: **distance**, **parent**, or **level** arrays → **O(V)**  

**Total Space Complexity: O(V)**

---

## 5. BFS Use Cases

### ✔ 5.1. Shortest Path in Unweighted Graphs
BFS guarantees the shortest path based on number of edges.

Examples:
- Word Ladder  
- Maze shortest path  
- Knight minimum moves in chess  
- Social network distance (degrees of separation)

---

### ✔ 5.2. Level Order Traversal of Trees
Binary Tree level order traversal is BFS applied to a tree.

Use cases:
- Right side view  
- Left side view  
- Zigzag traversal  

---

### ✔ 5.3. Connected Components in Graphs
BFS explores all nodes reachable from a given node.

Used for:
- Counting islands (grid problems)  
- Detecting clusters  
- Finding communication groups  

---

### ✔ 5.4. Cycle Detection (Undirected Graph)
If BFS finds a visited node that is **not the parent** → a cycle exists.

---

### ✔ 5.5. Checking Bipartite Graphs
Color the graph using two colors during BFS.  
If a conflict occurs → graph is **not bipartite**.

---

### ✔ 5.6. Nodes at Distance K / Level Finding
Because BFS is level-based, it's perfect for:
- Nodes at distance K  
- Minimum steps to reach a target  

---

### ✔ 5.7. Web Crawlers / Network Crawlers
Explore URLs or nodes in expanding layers → BFS behavior.

---

### ✔ 5.8. Pathfinding in Games / Grids
Used in:
- 2D grid shortest path  
- Maze solving  
- BFS flood-fill  
- Shortest path in puzzles  

---

## 6. BFS vs DFS (Quick Comparison)

| Feature         | BFS                      | DFS                     |
|-----------------|--------------------------|--------------------------|
| Shortest path   | ✔ Yes (unweighted)       | ✘ No                    |
| Memory usage    | Higher                   | Lower                   |
| Traversal style | Level by level           | Depth-first             |
| Good for        | Shortest path, layers    | Recursion, backtracking |

---

## 7. BFS Variations

- BFS with **parent tracking** → reconstruct shortest path  
- BFS returning **all shortest paths**  
- **Multi-source BFS** (initialize queue with many start nodes)  
- **Bidirectional BFS** (fastest for shortest path search)  

---
