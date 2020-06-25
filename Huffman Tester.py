print("Enter String to Compress:")

string = input()

class Tree(object):
    
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
    
    def child(self):
        return(self.left, self.right)
    
    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)
    
def Huffman_Compression(node, left = True, binString = ""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.child()
    dict()
    dict.update(Huffman_Compression(l, True, binString + "0"))
    dict.update(Huffman_Compression(r, False, binString + "1"))
    return dict()

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
        
freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = Tree(key1, key2)
    nodes.append((node, c1 + c2))
    
    nodes = sorted(nodes, key = lambda x: x[1], reverse = True)
    
huffmancoding = Huffman_Compression(nodes[0][0])

print(" Characters | Huffman Code ")
print("----------------------------")

for (char, frequency) in freq:
    print(" %-4r |%12s" % (char, huffmancoding[char]))