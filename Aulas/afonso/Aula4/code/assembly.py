from graphs import MyGraph

class DeBruijnGraph(MyGraph):
    def __init__(self, fragments):
        super().__init__({})
        self.create_DeBruijn_graph(fragments)


    # override method
    def add_edge(self, orig, dest):
       pass

    def create_DeBruijn_graph(self, fragments):
        pass

    # override method
    def in_degree(self, v):
		pass

class OverlapGraph(MyGraph):
    def __init__(self, fragments, reps=True):
		pass
    
    def create_overlap_graph(self,fragments):
		pass
    
    def create_overlap_graph_reps(self, fragments):
		pass
    
    # get the instances (ATG_1, ATG_2,ATG_3) of a seq (ATG)
    def get_instances(self, seq):
		pass

    def getSeq(self, node):
		pass

    def seq_from_path(self, p):
		pass

# get the prefix and sufix of a string
def suffix (seq):
    return seq[1:]

def prefix (seq):
    return seq[:-1]

#composição de k-mers
def composition(k,seq):
	pass

