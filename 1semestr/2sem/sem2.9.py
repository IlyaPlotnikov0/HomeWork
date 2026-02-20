with open('input_2.9.txt', 'r') as f:
    text = f.read()
f.close()    

m = ['.', '!', '?']
c = 0
    
for i in range(len(text)-1,0,-1):
    if text[i] in m:
        if text[i-1] in m:
            c = c
        else:
            c += 1
    
print(c)



 
