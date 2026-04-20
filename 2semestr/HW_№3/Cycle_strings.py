def prefix(s):
    p =[0]*len(s)
    for i in range(1, len(s)):
        k = p[i-1]
        while (k>0 and s[k] != s[i]):
            k = p[k-1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

text, p = input(), input()
p_set = set()
p2 = p + p
for i in range(len(p)):
    p_set.add(p2[i:i+len(p)])
p_cycle = list(p_set)

res = 0
for i in range(len(p)):
    for k in prefix(p_cycle[i]+'#'+text):
        if k == len(p):
            res += 1

print(res)
    
