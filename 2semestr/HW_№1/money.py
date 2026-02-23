N = int(input())
graph_valuts = {}
all_valuts = set()

for i in range(N):
   s = input("Введите в формате: валюта1 валюта2 коэффициент").split()
   all_valuts.add(s[0])
   all_valuts.add(s[1])
   if s[0] not in graph_valuts:
      graph_valuts[s[0]] = [(s[1], float(s[2]))]
   else:
      graph_valuts[s[0]].append((s[1], float(s[2])))


def cycle_inf(G, valuts, valuta):
   if valuta in valuts:
      color = {i:0 for i in valuts}
      curs = {i:1.0 for i in valuts}

      def dfs(start, k=1.0):
         color[start] = 1
         curs[start] = k
         for point in G[start]:
            new_k = k*point[1]
            if color[point[0]] == 0 and dfs(point[0], new_k):
               return True
            if color[point[0]] == 1:
               cycle_k = new_k/curs[point[0]]
               if cycle_k > 1.0:
                  return True
         color[start] = 2
         return False
      
      return dfs(valuta)
   else:
      return False


if cycle_inf(graph_valuts, all_valuts, 'руб'):
   print("Можно бесконечно обогатиться")
else:
   print("Нельзя")




             
