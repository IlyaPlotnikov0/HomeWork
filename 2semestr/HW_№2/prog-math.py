n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
graph = {}
graph['M'] = {}
graph['P'] = {}

for i in range(n):
    graph[str(i)] = {}
    graph['M'][str(i)], graph[str(i)]['M'] = b[i], 0
    graph[str(i)]['P'], graph['P'][str(i)] = a[i], 0
m = int(input())
for i in range(m): 
    u, v, w = input().split()
    graph[u][v], graph[v][u] = int(w), int(w)

def dfs(G,start,finish,visited,f_min):
    if start == finish:
        return f_min
    visited.add(start)
    for v in G[start]:
        if (v not in visited and G[start][v] > 0):
            flow = dfs(G,v,finish,visited,min(f_min,G[start][v]))
            if flow > 0:
                G[start][v] -= flow
                G[v][start] += flow
                return flow
    return 0
        
def ford_fulkerson(G,start,finish):
    visited = set()
    res = 0
    while (flow:=dfs(G,start,finish,visited,float('inf'))) != 0:
        res += flow
        visited = set()
    return res

ans = ford_fulkerson(graph, 'M', 'P')
print(ans)

def razrez(G, start):
    visit = set()
    stuck = [start]
    while stuck:
        u = stuck.pop()
        for v in G[u]:
            if v not in visit and G[u][v] > 0:
                visit.add(v)
                stuck.append(v)
    return visit

for i in range(n):
    if str(i) in razrez(graph, 'M'):
        print(i, "mathematic")
    else:
        print(i, "proger")





    
































"""n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

G = {}

def add_edge(G, u, v, w):
    if u not in G:
        G[u] = {}
    if v not in G:
        G[v] = {}
    G[u][v] = w
    if v not in G or u not in G[v]:
        if v not in G:
            G[v] = {}
        G[v][u] = 0

for i in range(n):
    add_edge(G, 'S', str(i), a[i])  
    add_edge(G, str(i), 'T', b[i])  

m = int(input())
for _ in range(m):
    i, j, c = map(int, input().split())
    i, j = str(i), str(j)
    add_edge(G, i, j, c)
    add_edge(G, j, i, c)

def dfs(G, start, finish, visited, f_min):
    if start == finish:
        return f_min
    visited.add(start)
    for v in list(G[start].keys()):
        if v not in visited and G[start][v] > 0:
            flow = dfs(G, v, finish, visited, min(f_min, G[start][v]))
            if flow > 0:
                G[start][v] -= flow
                if v not in G:
                    G[v] = {}
                if start not in G[v]:
                    G[v][start] = 0
                G[v][start] += flow
                return flow
    return 0

def ford_fulkerson(G, start, finish):
    res = 0
    while True:
        visited = set()
        flow = dfs(G, start, finish, visited, float('inf'))
        if flow == 0:
            break
        res += flow
    return res

ans = ford_fulkerson(G, 'S', 'T')
print(ans)

def find_reachable(G, start):
    visited = set()
    stack = [start]
    while stack:
        u = stack.pop()
        for v in G[u]:
            if v not in visited and G[u][v] > 0:
                visited.add(v)
                stack.append(v)
    return visited

reachable = find_reachable(G, 'S')

for i in range(n):
    if str(i) in reachable:
        print(i, "programmer")
    else:
        print(i, "mathematician")"""