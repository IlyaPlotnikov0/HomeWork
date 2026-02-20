import numpy as np

def sr(x):
    return sum(x)/len(x)

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    k = (sr(x*y)-sr(x)*sr(y)) / (sr(x*x)-sr(x)**2)
    b = sr(y) - k*sr(x)
    return k, b

x, y = list(map(int, input().split())), list(map(int, input().split()))
print(mnk(x, y))                                           
