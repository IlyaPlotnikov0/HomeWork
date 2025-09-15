N, b, c = input(), int(input()), int(input())
N10 = 0
for i in range(0, len(N)):
    N10 += int(N[-i-1])*(b**i)
res = ''
while(N10):
    res += str(N10%c)
    N10 = N10//c
print(res[::-1])    
    
