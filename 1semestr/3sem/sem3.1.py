def factor(n, c = {0:0, 1:1}):
    if n in c:
        return (c[n])
    else:
        c[n] = n*factor(n-1)
        return c[n]
    
a = int(input())
print(factor(a))



