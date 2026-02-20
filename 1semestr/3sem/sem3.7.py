import numpy as np

N, M = int(input()), int(input())
A = np.zeros([N,N])
Z = np.zeros([N,1])
for i in range(0, N):
    s = list(map(int, input().split()))
    A[i] = np.array(s[:-1])
    Z[i] = np.array(s[-1])
A_copy = A.copy()

detA = np.linalg.det(A)

m = []
for j in range(0, N):
    A_copy[:, j] = Z.T
    det = np.linalg.det(A_copy)
    m.append(det)
    A_copy[:, j] = A[:, j]
    
solve = np.array(m)/detA
for i in range(0, N):
    print (f"x{i+1} = {solve[i]}")

