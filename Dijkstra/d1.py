import heapq

def dijkstra(V, edges, source):
    # Step 1: Create adjacency list
    graph = [[] for _ in range(V)]
    for u, v, w in edges:
        graph[u].append((v, w))

    # Step 2: Initialize distance array
    distance = [float('inf')] * V
    distance[source] = 0

    # Step 3: Min-heap (priority queue)
    pq = [(0, source)]  # (distance, node)

    while pq:
        dist, node = heapq.heappop(pq)

        # If we already found a shorter path before, skip
        if dist > distance[node]:
            continue

        # Step 4: Relax edges
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    # Step 5: Print results
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
dijkstra(V, edges, source)
