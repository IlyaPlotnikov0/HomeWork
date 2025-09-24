f = open('input.txt','r')
s = list(map(int, f.readline().split()))
d = f.readline().strip()
print(d)
if d == '+':
    res = 0
    for x in s:
        res += x
elif d == '-':
    res = 0
    for x in s:
        res -= x        
elif d == '*' : 
    res = 1
    for x in s:
        res *= x

f.close()

f = open('output.txt','w')
f.write(str(res))
f.close()
