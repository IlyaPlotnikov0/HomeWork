f = open('input.txt','r')
s = f.readline().split()
d = f.readline().strip()
c = int(f.readline().strip())
m = []
res = ''

for i in range(0, len(s)):
    j_10 = 0
    for j in range(0, len(s[i])):
      j_10 += int(s[i][-j-1])*(c**j)
    m.append(j_10)           

if d == '+':
    res_10 = 0
    for x in m:
        res_10 += x
elif d == '-':
    res_10 = 0
    for x in m:
        res_10 -= x        
elif d == '*':
    res_10 = 1
    for x in m:
        res_10 *= x    
f.close()

while(res_10):
    res += str(res_10%c)
    res_10 = res_10//c

f = open('output.txt','w')
f.write(res[::-1])
f.close()
