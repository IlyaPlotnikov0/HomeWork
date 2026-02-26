
def dijkstra(G, start):
    distances = {i: float('inf') for i in G}
    distances[start] = 0
    visited = set()
    while len(visited) < len(G): 
        cur = min((v for v in distances if v not in visited), key=distances.get)
        visited.add(cur)
        for node in G[cur]:
            if node not in visited:
                if distances[node] > distances[cur] + G[cur][node]:
                    distances[node] = distances[cur] + G[cur][node]
    return distances


def bellman_ford(G, start):
    d  = {i: float('inf') for i in G}
    d[start] = 0
    for i in range(len(G)-1):
        for node1 in d:
            for node2 in G[node1]:
                if d[node2] > d[node1] + G[node1][node2]:
                    d[node2] = d[node1] + G[node1][node2]
    return d 


def johnson(G):
    nodes = list(G.keys())
    s = bellman_ford(G, nodes[0])  
    G_new = {v: {} for v in nodes}
    for v in nodes:
        for u in G[v]:
            G_new[v][u] = G[v][u] + s[v] - s[u]
    
    res = {}
    for start in nodes:
        dist = dijkstra(G_new, start)
        dist_new = {u: dist[u] - s[start] +s[u] for u in nodes}
        res[start] = dist_new  
    return res