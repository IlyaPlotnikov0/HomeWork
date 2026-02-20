a = input()
slovo = list(a)

def pol(s):
    if s == s[::-1]:
        return 1
    else:
        return 0

def z(s):
    s_ = s
    c = 0
    mimo = ['4', '6', '7', '9', 'Q', 'R', 'P', 'D', 'F', 'G', 'K', 'C', 'B', 'N']
    zerc = ['E', 'J', 'S', 'Z', '3', 'L', '2', '5']
    zerc_ = zerc[4:8] + zerc[0:4]
    for i in s:
        if i in mimo == True:
            c += 1
    if c > 0:
        return 0

    else:
        for i in range(0, 3):
            for j in range (0, 8):
                if s[i] == zerc[j]:
                    s_[i] = zerc_[j]
        if s_[::-1] == s:
            return 1
        else:
            return 0

p = pol(slovo)
z = z(slovo)

if p == 0 and z == 0:
    print(a, "is not a palindrome")
if p == 1 and z == 0:
    print(a, "is a regular palindrome")
if p == 0 and z == 1:
    print(a, "is a mirrored string")
if p == 1 and z == 1:
    print(a, "is a mirrored palindrome")    
    
        
