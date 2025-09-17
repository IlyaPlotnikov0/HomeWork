s = input().split()
m = 0
for i in range(0,len(s)):
    if s.count(s[i]) > m:
        m = s.count(s[i])
        j = i
print(s[j])        
