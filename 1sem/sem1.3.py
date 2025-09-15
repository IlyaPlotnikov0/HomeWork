a = list(map(int,input().split(' ')))
p = 1
for i in range(0,len(a)):
  p = p*a[i]
print(p**(1/len(a)))
