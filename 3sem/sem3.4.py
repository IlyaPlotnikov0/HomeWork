def triangle (size, symb):
    for i in range(1, (size+1)//2):
        print(symb*i)
    for i in range((size+1)//2, 0, -1):
        print(symb*i)
s = input().split()
triangle(int(s[0]), s[1])















 
    
