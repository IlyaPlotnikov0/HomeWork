class Node:
    def __init__(self):
        self.children = {}
        self.output = None

class Bor:
    def __init__(self):
        self.root = Node()

    def add(self, s):
        v = self.root
        for c in s:
            if c in v.children:
                v = v.children[c]
            else:
                new_v = Node()
                v.children[c] = new_v
                v = new_v
        v.output = s

    def find(self, s):
        v = self.root
        for c in s:
            if c in v.children:
                v = v.children[c]
            else:
                return False
        if v.output:
            return v
        else:
            return False
    
    def delete(self, s):
        v = self.find(s)
        if not v:
            return False
        v.output = None

        cur = self.root
        path= [cur]
        for c in s:
            if c in cur.children:
                cur = cur.children[c]
                path.append(cur)
        
        for i in range(len(path)-1, 0, -1):
            cur = path[i]
            parent = path[i-1]
            if cur.children or cur.output:
                break
            else:
                for c, v in parent.children.items():
                    if v == cur:
                        del parent.children[c]
                        break



            

