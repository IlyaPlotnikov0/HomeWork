def alg(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, d = alg(b, a%b)
        return y, x - y*(a//b), d

s = input().split()
a = int(s[0])
b = int(s[1])

print(alg(a, b))

    
