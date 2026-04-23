from collections import deque

alphabet = 'abc'

class Node:
    def __init__(self):
        self.children = {}
        self.to = {}
        self.sufflink = None
        self.compressed_sufflink = None
        self.output = None

class AhoCorasick:
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

    def built_trie(self, words):
        for word in words:
            self.add(word)
        self.built_links()

    def built_links(self):
        queue = deque()
        self.root.sufflink = self.root
        self.root.compressed_sufflink = self.root
        for char in alphabet:
            if char in self.root.children:
                self.root.to[char] = self.root.children[char]
            else:
                self.root.to[char] = self.root
        for i in self.root.children:
            cur = self.root.children[i]
            cur.sufflink = self.root
            cur.compressed_sufflink = self.root
            queue.append(cur)

        while queue:
            current = queue.popleft()
            for char in alphabet:
                if char in current.children:
                    current.to[char] = current.children[char]
                else:
                    current.to[char] = current.sufflink.to[char]
            for i in current.children:
                current_child = current.children[i]
                current_child.sufflink = current.sufflink.to[i]
                queue.append(current_child)
                if current_child.sufflink.output is not None:
                    current_child.compressed_sufflink = current_child.sufflink
                else:
                    current_child.compressed_sufflink = current_child.sufflink.compressed_sufflink

    
    def find_short_str(self, words):
        self.root = Node()
        for word in words:
            self.add(word)
        self.built_links()

        n = len(words)
        node_num = {w: i for i, w in enumerate(words)}
        node_mask = {}

        def get_mask(node):
            if node in node_mask:
                return node_mask[node]         
            mask = 0
            cur = node
            while cur != self.root:
                if cur.output is not None:
                    mask = mask | (1 << node_num[cur.output])
                cur = cur.compressed_sufflink
            node_mask[node] = mask
            return mask

        queue, visited = deque(), set()
        queue.append((self.root, 0, ""))
        visited.add((id(self.root), 0))
        final_mask = (1 << n) - 1

        while queue:
            node, mask, string = queue.popleft()
            if mask == final_mask:
                return string

            for c in alphabet:
                next_node = node.to[c]
                new_mask = mask | get_mask(next_node)
                state = (id(next_node), new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((next_node, new_mask, string + c))

        return None
    

aho = AhoCorasick()
paterns = ('ab', 'bacccc','ccccaaba')
print(aho.find_short_str(paterns))