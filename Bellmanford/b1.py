INF = float('inf')

def bellman_ford(V, edges, source):
    # Step 1: Initialize distances
    distance = [INF] * V
    distance[source] = 0

    # Step 2: Relax all edges (V-1) times
    for _ in range(V - 1):
        for u, v, w in edges:
            if distance[u] != INF and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Step 3: Check for negative weight cycles
    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w < distance[v]:
            print("Negative Cycle Detected!")
            return

    # Step 4: Print result
    print("Vertex\tDistance from Source")
    for i in range(V):
        print(f"{i}\t{distance[i]}")

# ---- Main Code ----
V, E = map(int, input("Enter number of vertices and edges: ").split())
edges = []

print("Enter edges (u v w):")
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex: "))
bellman_ford(V, edges, source)
