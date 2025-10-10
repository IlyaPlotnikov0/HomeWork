X = list(map(int, input().split()))
Y = list(map(int, input().split()))
A = set(X)
B = set(Y)

print('Уникальные элементы х:', A - B)
print('Уникальные элементы y:', B - A)
print('Уникальные элементы объединения:', A^B)        
print('Содержатся в обоих списках:', A & B)



