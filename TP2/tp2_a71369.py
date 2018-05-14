import sys
import matplotlib.pyplot as plt

#leitura pares
def readPairs(filename):
	pairs = []
	file  = open(filename, "r")
	flag  =  0

	print ("Parsing...")
	for line in file:
		#chrom line
		if flag == 0:
			if "#CHROM" in line:
				flag = 1
		#data lines
		else:
			ref = line.split('\t')[3]
			alt = line.split('\t')[4]
			if ',' in alt:
				pairs.append('(' + str(ref) + '>' + str(alt.split(',')[0])+')')
				pairs.append('(' + str(ref) + '>' + str(alt.split(',')[1])+')')
			else:
				pairs.append('(' + str(ref) + '>' + str(alt)+')')
	return pairs

#total de mutações unicas
def perg_a(filename):
	pairs = readPairs(filename)
	count = len(set(pairs))

	return str(count)

#grafico de barras
def perg_b(fileName):
	pairs = readPairs(filename)
	mutacoes = dict()
	x = []
	y = []

	for pair in pairs:
		values = pair.split('>')
		if(len(values[0]) == len(values[1])):
			if(pair in mutacoes):
				mutacoes[pair]+=1
			else:
				mutacoes[pair]=1
	
	for m in mutacoes:
		x.append(str(m))
		y.append(mutacoes[m])

	#desenho
	plt.bar(x,y)
	plt.show()

#snp, delete, insert
def perg_c(fileName):
	pairs = readPairs(filename)
	snp = deleted = inserted = 0

	for pair in pairs:
		values = pair.split('>')
		if(len(values[0]) == len(values[1])):
			snp+=1
		elif(len(values[0]) > len(values[1])):
			deleted += 1
		else:
			inserted += 1

	return str((snp,deleted,inserted))

#SUFFIX_TRIE
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
			
	def findPattern(self, p):
		node = 0
		counter = 0
		while len(p)!=0:
			if counter<len(self.nodes[node][1]):
				for n in self.nodes[node][1]:
					if n[0] in p[0]:
						i=0
						j=0
						while i<len(n) and j<len(p):
							if n[i]==p[j]:
								i = i+1
								j = j+1
							else:
								return None
						p=p[len(n)::]
						node=self.nodes[node][1][n]
						counter=0
						break
					else:
						counter+=1
		if p!="":
			return None
		return self.getLeafesBelow(node)

	def getLeafesBelow(self, node):
		res = []
		if self.nodes[node][0]>=0: 
			res.append(self.nodes[node][0])            
		else:
			for k in self.nodes[node][1].keys():
				new_node = self.nodes[node][1][k]
				below = self.getLeafesBelow(new_node)
				res.extend(below)
		return res

	def resolve_path(self,node):
		c = []
		p = ''
		if self.nodes[node][0] < 0:
			for k in self.nodes[node][1].keys():
				c.append(self.nodes[node][1][k])
				p = p + k
				path,compact = self.resolve_path(self.nodes[node][1][k])
				p = p + path
				c.extend(compact)
		return p,c

	def update(self,new):
		#atualização dos campos
		for index in new:
			for key,value in new[index]:
				self.nodes[index][1][key]=value
			self.nodes[index] = (self.nodes[index][0],self.nodes[index][1])	
	
	def remove(self,deletions):
		#remoção dos campos
		for index in deletions:
			for key,values in deletions[index]:
				del(self.nodes[index][1][key])
				for value in values:
					del(self.nodes[value])

	#Compact Tree
	def compact(self):
		path = ''
		previous = []
		new = dict()
		deletions = dict()
		if(self.nodes.keys()!=None):
			for key in self.nodes.keys():
				if self.nodes[key][0] < 0:
					for node in self.nodes[key][1]:
						l = len(self.getLeafesBelow(self.nodes[key][1][node]))
						if l == 1:
							if self.nodes[key][1][node] not in previous:
								if node != "$":
									path = node
									path = path + self.resolve_path(self.nodes[key][1][node])[0]
									previous.append(self.nodes[key][1][node])
									previous.extend(self.resolve_path(self.nodes[key][1][node])[1])
									c = self.resolve_path(self.nodes[key][1][node])[1]
									if key in new:
										new[key].append((path,c[len(c)-1]))
									else:
										new[key] = [(path,c[len(c)-1])]
									if key in deletions:
										list_del = [self.nodes[key][1][node]] + c[0:len(c)-1]
										deletions[key].append([(node, list_del)])
									else:
										list_del = [self.nodes[key][1][node]] + c[0:len(c)-1]
										deletions[key] = [(node, list_del)]
			self.update(new)
			self.remove(deletions)

	def repeats(self,k,ocs):
		x=0
		seq=''
		#check if current dictionary value isnt empty
		while self.nodes[x][1]!={}:
			n_nodes = self.nodes[x][1]
			for n in n_nodes:
				n_node = n_nodes[n]
				if n_node==x+len(n):
					seq=seq+n
					x=n_node
					break
		seq=seq[0:len(seq)-1]
		#add to dictionary
		d=dict()
		for i in range(0, len(seq)-k+1):
			if seq[i:i+k] not in d:
				d[seq[i:i+k]]=1
			else:
				d[seq[i:i+k]]+=1
		#return
		l=[]
		for elem in d:
			if d[elem] > ocs or d[elem] == ocs:
				l.append(elem)
		return sorted(l)

if __name__ == "__main__":
	#py .\tp2_a71369.py .\HG00154.chr21.raw.vcf
	if(len(sys.argv)>1):
		filename = str(sys.argv[1])
		print('----------Pergunta 1a----------')
		print('Total de mutações únicas: ' + perg_a(filename))
		perg_b(filename)
		print('----------Pergunta 1c----------')
		print('Total de SNP, deleções e inserções : ' + perg_c(filename))
		print('-------------------------------')
	#py .\tp2_a71369.py  
	else:
		seq = 'TACTA'
		st = SuffixTrie()
		st.suffixTrieFromSeq(seq)
		st.compact()
		print('----------Pergunta 2a----------')
		st.print_tree()
		print('----------Pergunta 2b----------')
		pattern = 'CTA'
		print('Found pattern ' + pattern + ' on index ' + str(st.findPattern(pattern)))
		print('----------Pergunta 2c----------')
		repeats = st.repeats(3,1)
		print('Found the following repeated values ' + str(repeats))
		print('-------------------------------')