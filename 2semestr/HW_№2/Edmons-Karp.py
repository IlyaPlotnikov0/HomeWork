from collections import deque

M = int(input())
G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = int(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    if v2 in G:
        G[v2][v1] = 0
    else:
        G[v2] = {v1:0}

def bfs(G, start, finish):
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        for v in G[current]:
            if v not in visited and G[current][v]>0:
                new_path = path + [v]
                queue.append((v, new_path))
                visited.add(v)
                if v == finish:
                   return new_path
    return False
                   
def edmonds_karp(G,start,finish):
    res = 0
    while True:
        line = bfs(G, start, finish)
        if not line:
            break
        flow = float('inf')
        for i in range(len(line)-1):
            u, v = line[i], line[i+1]
            flow = min(flow, G[u][v])
        for i in range(len(line)-1):
            u, v = line[i], line[i+1]
            G[u][v] -= flow
            G[v][u] += flow 
        res += flow
    return res

print(edmonds_karp(G, '0', '3'))
        


    


