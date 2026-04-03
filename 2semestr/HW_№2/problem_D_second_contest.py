def Prima(G):
    MST = []
    dist = {i: float('inf') for i in G}
    start = list(G.keys())[0]
    dist[start] = 0
    sum = 0
    prev = {i: None for i in G}
    visited = set()
    while len(visited) != len(G):
        candidates = {k: v for k, v in dist.items() if k not in visited}
        if not candidates:
            break
        v = min(candidates, key=candidates.get)
        if dist[v] == float('inf'):
            return None, 0
        visited.add(v)
        if prev[v] is not None:
            MST.append([prev[v], v])
            sum += dist[v]
        for u in G[v]:
            if u not in visited and dist[u] > G[v][u]:
                dist[u] = G[v][u]
                prev[u] = v
        dist[v] = float('inf')
    return MST, sum


n, m, p = list(map(int, input().split()))
unsafe = list(map(int, input().split()))
unsafe_set = set(unsafe)

G = {i: {} for i in range(1,n+1)}
for i in range(m):
    u, v, w = list(map(int, input().split()))
    G[u][v], G[v][u] = w, w

for val in unsafe:
    min_w, min_v = float('inf'), None
    for v in G[val]:
        if v not in unsafe_set and G[val][v] < min_w:
            min_w, min_v = G[val][v], v
    if min_v is None:
        print("impossible")
        exit()
    G[min_v][val], G[val][min_v] = min_w, min_w

safe_G = {}
for u in G:
    if u not in unsafe_set:
        safe_G[u] = {}
        for v in G[u]:
            if v not in unsafe_set:
                safe_G[u][v] = G[u][v] 

if not safe_G:
    print("impossible")
    exit()
MST, mst_w = Prima(safe_G)
total_w = 0
if MST is None:
    print("impossible")
    exit()
else:
    for val in unsafe:
        w = list(G[val].values())[0]
        total_w += w
print(mst_w + total_w)