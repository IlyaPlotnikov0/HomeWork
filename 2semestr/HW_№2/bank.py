from collections import deque

n = int(input())
graph = {'p':{}, 'b':{}}
sum_credit = 0

for i in range(n):
    graph['p'][str(i)] = 0
    graph[str(i)] = {'p': 0}
for i in range(n, 2*n):
    graph['b'][str(i)] = 0
    graph[str(i)] = {'b': 0}

for i in range(n):
    s1 = input('№_pr credit bank_i ...').split()
    credit = int(s1[1])
    sum_credit += credit
    graph['p'][s1[0]] = credit
    for v in s1[2::]:
        graph[s1[0]][v] = credit
        graph[v][s1[0]] = 0
for i in range(n, 2*n):
    s2 = input('№_banca sum').split()
    sum = int(s2[1])
    graph[s2[0]]['b'] = sum

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

if edmonds_karp(graph, 'p', 'b') == sum_credit:
    print('YES')
else:
    print('NO')