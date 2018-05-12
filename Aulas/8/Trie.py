class Trie:   
    def __init__(self):
        self.nodes = { 0: {} } # root node
        self.num = 0
    
    def print_tree(self):
        for k in self.nodes.keys():
            print (k, "->" , self.nodes[k]) 
    
    def addNode(self, origin, symbol):
        self.num += 1
        self.nodes[origin][symbol] = self.num
        self.nodes[self.num] = {}
    
    def addPattern(self, p):
        pos=0
        node=0
        while pos<(len(p)):
            if p[pos] not in self.nodes[node].keys():
                self.addNode(node, p[pos])
            node = self.nodes[node][p[pos]]
            pos+=1
                    
                
    def trieFromPatterns(self, pats):
        for p in pats:
            self.addPattern(p)
    
    def prefixTrieMatch(self, text):
        pos= 0
        match = ""
        node = 0
        while pos< len(text):
            if text[pos] in self.nodes[node].keys() :
                node = self.nodes[node][text[pos]]
                match += text[pos]
                if self.nodes[node] == {}:
                    return match
                else: 
                    pos+= 1
            else: 
                return None
        return None
        
    def trieMatches(self, text):
        res = []
        for i in range(len(text)):
            m = self.prefixTrieMatch(text[i:])
            if m != None: res.append((i,m))
        return res
   
def test():
    patterns = ["ATAGA", "ATC", "GAT"]
    t = Trie()
    t.trieFromPatterns(patterns)
    t.print_tree()
    print (t.prefixTrieMatch("ATAGACATC"))
    print (t.trieMatches("CCATAGACATCAAGATCGG"))
    
test()