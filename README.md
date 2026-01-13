# Data_Structure_and_Algorithms_2_Practise
```markdown
# DSA2 Topics README

This README organizes key Data Structures and Algorithms (DSA) topics at level 2, including shortest path algorithms, sorting techniques, graph problems, string matching, and recursive paradigms. Each section covers core concepts, time complexity, and high-level pseudocode for quick reference and implementation.

## Bellman-Ford Algorithm
Bellman-Ford computes shortest paths from a source vertex in graphs with negative weights, relaxing all edges V-1 times and detecting negative cycles.Time complexity is O(V * E) in worst case, where V is vertices and E is edges, due to full relaxations even in best cases.Pseudocode: Initialize distances to infinity except source (0); for i=1 to V-1, for each edge (u,v,w), relax dist[v] = min(dist[v], dist[u] + w); check for negative cycles with one more pass.

## Dijkstra's Algorithm
Dijkstra finds shortest paths in graphs with non-negative weights using a priority queue to select the minimum distance vertex.[web:6] Time complexity is O((V + E) log V) with binary heap, or O(V^2) without, outperforming Bellman-Ford for non-negative edges. Pseudocode: Initialize distances to infinity except source (0), use priority queue; while queue not empty, extract min u, for each neighbor v of u, relax dist[v] = min(dist[v], dist[u] + w).[web:6]

## Divide and Conquer
Divide and Conquer solves problems by dividing into subproblems, conquering recursively, and combining results, analyzed via Master Theorem T(n) = aT(n/b) + f(n).[web:7] Common in sorting and searching, it achieves balanced efficiency across levels. Example: Merge Sort divides array into halves, sorts subarrays, merges in O(n).
## Merge Sort
Merge Sort, a stable Divide and Conquer sort, divides array into halves, sorts recursively, and merges sorted halves. Time complexity is O(n log n) worst/average/best due to log n levels each costing O(n) merges. Pseudocode: If size >1, mid = n/2, recursively sort left[0..mid] and right[mid+1..n], then merge by comparing and copying smallest elements.

## Minimum Spanning Tree (MST)
MST connects all vertices with minimum total edge weight without cycles; Kruskal sorts edges and adds non-cycle forming ones using Union-Find (O(E log E)), Prim grows from vertex using priority queue (O(E log V)).Both suit dense/sparse graphs differently.Pseudocode for Kruskal: Sort edges by weight; initialize Union-Find; for each edge, if not same set, union and add to MST until V-1 edges.

## Recursion
Recursion solves problems by calling itself on smaller inputs with base case to terminate, analyzed via recursion trees summing costs per level.Time complexity varies, e.g., factorial T(n) = T(n-1) + O(1) is O(n).Common in tree traversals, Divide and Conquer; tail recursion optimizes to iteration.

## Rabin-Karp Algorithm
Rabin-Karp uses rolling hash for string matching, computing pattern hash and sliding text window hashes for quick comparisons.[web:11] Average time O(n + m), worst O(nm) due to collisions requiring verification. Pseudocode: Compute pattern hash h; compute text window hash, slide by removing first char hash and adding next (modulo prime); if hashes match, check characters.
```
