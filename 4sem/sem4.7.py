f = open('C:/Users/User/Desktop/qwerty.txt')
s = f.read()

l = {}
k = 0

sign = '.,!?-'
for i in sign:
  s = s.replace(i, ' ')
s1 = set(s.lower().split())

for i in s.lower().split():
  if i in l:
    l[i] += 1
  else:
    l[i] = 1
while k < 10:
  print(max(l, key = l.get), l[max(l, key = l.get)])
  del a[max(l, key = l.get)]
  k += 1
