N = int(input())
graph = {i: set() for i in range(N)}
for i in range(N):
    graph[i] = list(map(int, input().split()))


visited_edges = []
path = []

def check(graph):
    v_nech = []   
    for v in graph:
        if len(graph[v]) % 2 == 1:
            v_nech.append(v)
    if len(v_nech) < 3:
        return v_nech
    else:
        print('В графе кол-во вершин с нечетн степенью > 2')
        exit()
    
if check(graph):
    start = check(graph)[0]
else:
    start = list(graph.keys())[0]

def dfs(start):
    for v in graph[start]:
        if v > start:
            edge = [start, v]
        else:
            edge = [v, start]
        if edge not in visited_edges:
            visited_edges.append(edge)
            dfs(v)
    path.append(start) 

dfs(start)

graph_edges = sum(len(graph[i]) for i in range(N)) // 2
if len(visited_edges) != graph_edges:
    print("В графе несколько компонент связанности. Эйлерова пути нет")

else:
    print(path[::-1])





          










    


