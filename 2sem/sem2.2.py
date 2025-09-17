G, s = input().split()
G = int(G)
g_len = len(s)//G
res = ''
for i in range (0, len(s),g_len):
    res += s[i:i+g_len][::-1]
print(res)
