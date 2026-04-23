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

def prefix_counter(s):
    pr = prefix(s)
    res = {i: 0 for i in range(0, n+1)}
    for i in pr:
        res[i] += 1
    for i in range(n, 0, -1):
        res[pr[i-1]] += res[i]
    for i in range(n+1):
        res[i] += 1
    return res

s = 'abcabbbbabcab'
n = len(s)
for i in range(1, n+1):
    print(s[:i], prefix_counter(s)[i])