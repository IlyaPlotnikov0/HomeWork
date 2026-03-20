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
