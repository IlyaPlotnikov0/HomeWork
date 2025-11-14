m = list(map(int, input().split()))
res = [-1] * len(m)
stack = []

for i in range(len(m)):
    while stack and m[stack[-1]] < heights[i]:
        stack.pop()
    if stack:
        res[i] = stack[-1]
    else:
        res[i] = -1
    stack.append(i)
print(res)