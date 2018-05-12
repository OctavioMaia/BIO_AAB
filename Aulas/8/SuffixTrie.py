class SuffixTrie:
    
    def __init__(self):
        self.nodes = { 0:(-1,{}) } # root node
        self.num = 0
    
    def print_tree(self):
        for k in self.nodes.keys():
            if self.nodes[k][0] < 0:
                print (k, "->", self.nodes[k][1]) 
            else:
                print (k, ":", self.nodes[k][0])
                
    def addNode(self, origin, symbol, leafnum = -1):
        self.num += 1
        self.nodes[origin][1][symbol] = self.num
        self.nodes[self.num] = (leafnum,{})
        
    def addSuffix(self, p, sufnum):
        pos = 0
        node = 0
        while pos < len(p):
            if p[pos] not in self.nodes[node][1].keys():
                if pos == len(p)-1:
                    self.addNode(node, p[pos], sufnum)
                else:
                    self.addNode(node, p[pos])     
            node = self.nodes[node][1][p[pos]]
            pos += 1
    
    def suffixTrieFromSeq(self, text):
        t = text+"$"
        for i in range(len(t)):
            self.addSuffix(t[i:], i)
            
    def findPattern(self, pattern):
        pos = 0
        node = 0
        for pos in range(len(pattern)):
            if pattern[pos] in self.nodes[node][1].keys():
                node = self.nodes[node][1][pattern[pos]]
                pos += 1
            else: return None
        return self.getLeafesBelow(node)
        

    def getLeafesBelow(self, node):
        res = []
        if self.nodes[node][0] >=0: 
            res.append(self.nodes[node][0])            
        else:
            for k in self.nodes[node][1].keys():
                newnode = self.nodes[node][1][k]
                leafes = self.getLeafesBelow(newnode)
                res.extend(leafes)
        return res
    
    def compact (self):
        dic = {0:(-1,{})}
        lista=[]
        visited=[]
        prev=""
        pattern=""
        next=0
        for i in range(0, len(self.nodes)):
            if len(self.nodes[i][1])>1:
                lista.append(i)
        for i in range(0, len(lista)):
            for l in self.nodes[lista[i]][1]:
                root=lista[i]
                next=self.nodes[lista[i]][1][l]
                prev=l
                pattern=""
                if prev=="$":
                    if lista[i] not in dic:
                        dic[lista[i]]=(-1,{})
                    if prev not in dic[lista[i]][1].keys():
                        dic[lista[i]][1][prev]=next
                    visited.append(next)
                    dic[next]=(self.nodes[next][0],{})
                
                if next not in visited:
                    while self.nodes[next][1]!={}:
                        if len(self.nodes[next][1])==1:
                            for letter in self.nodes[next][1]:
                                visited.append(next)
                                pattern=pattern+prev+letter
                                prev=""
                                next=self.nodes[next][1][letter]
                        elif len(self.nodes[next][1])>1:
                            for letter in self.nodes[next][1]:
                                if self.nodes[next][1][letter]==next+1:
                                    visited.append(next)
                                    if root not in dic: 
                                        dic[root]=(-1,{})                                         
                                    if pattern=="":
                                        if prev not in dic[root][1].keys(): 
                                            dic[root][1][prev]=next
                                    else:
                                        if pattern not in dic[root][1].keys(): 
                                            dic[root][1][pattern]=next
                                    root=next
                                    next=self.nodes[next][1][letter]
                                    prev=letter
                                    pattern=""
                                    break
                        if self.nodes[next][1]=={}:
                            visited.append(next)
                            if root not in dic:
                                dic[root]=(-1,{})
                            if pattern not in dic[root][1].keys():
                                dic[root][1][pattern]=next
                            dic[next]=(self.nodes[next][0],{})
        self.nodes=dic


    def findPattern2(self, pattern):
        node = 0
        counter=0
        while len(pattern)!=0 and counter<len(self.nodes[node][1]):
            for n in self.nodes[node][1]:
                if n[0] in pattern[0]:
                    i=0
                    j=0
                    while i<len(n) and j<len(pattern):
                        if n[i]==pattern[j]:
                            i+=1
                            j+=1
                        else:
                            return None
                    pattern=pattern[len(n)::]
                    node=self.nodes[node][1][n]
                    counter=0
                    break
                else:
                    counter+=1
        if pattern!="":
            return None 
        return self.getLeafesBelow(node)
    
    
    def repeats(self,k,ocs):
        node=0
        seq=""
        dic={}
        lista=[]
        while self.nodes[node][1]!={}:
            for l in self.nodes[node][1]:
                if self.nodes[node][1][l]==node+len(l):
                    seq+=l
                    node=self.nodes[node][1][l]
                    break
        seq=seq[:-1]
        for i in range(0, len(seq)-k+1):
            if seq[i:i+k] in dic:
                dic[seq[i:i+k]]+=1
            else:
                dic[seq[i:i+k]]=1
        for d in dic:
            if dic[d]>=ocs:
                lista.append(d)
        return lista
        
def test1():
    seq = "aaabbbc"
    st = SuffixTrie()
    st.suffixTrieFromSeq(seq)
    #print (st.findPattern(""))
    #st.print_tree()
    #print(st.getLeafesBelow(10))
    st.compact()
    st.print_tree()
    print (st.findPattern2("bbc"))
    print(st.repeats(2,2))
    
    
def test2():
    seq = "aaabbbc"
    st = SuffixTrie()
    st.suffixTrieFromSeq(seq)
    #st.print_tree()
    #print (st.findPattern("TA"))
    st.compact()
    st.print_tree()
    #print (st.findPattern2("T"))
    #print (st.findPattern2("TA"))
    #print(st.repeats(3,2))

test1()
#test2()