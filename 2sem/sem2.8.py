N = int(input())
s = list(map(int, input().split()))
k = 0
for i in range(0,len(s)):
    for j in range(0,len(s)):
        if s[i] > s[j]:
            k += 1

    if k == (N-1)/2:
        print(s[i])
        k = 0
    else:
        k = 0
