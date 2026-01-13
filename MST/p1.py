import sys

def primMST(graph, root):
    V = len(graph)
    key = [sys.maxsize] * V
    parent = [-1] * V
    inMST = [False] * V

    key[root] = 0

    for _ in range(V):
        u = -1
        for v in range(V):
            if not inMST[v] and (u == -1 or key[v] < key[u]):
                u = v

        if u == -1 or key[u] == sys.maxsize:
            break

        inMST[u] = True

        for v, weight in graph[u]:
            if not inMST[v] and weight < key[v]:
                parent[v] = u
                key[v] = weight

    print("Minimum Spanning Tree:")
    for i in range(V):
        if parent[i] != -1:
            print(f"{parent[i]} {i}")


# Main Function
if __name__ == "__main__":
    # ---------- Sample Input ----------
    V = int(input("Vertex = "))
    E = int(input("Edge = "))

    graph = [[] for _ in range(V)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))  # Undirected graph

    root = 0  # Start from vertex 0 (you can change if needed)

    primMST(graph, root)
