from graphs import MyGraph

class MetabolicNetwork(MyGraph):
    def __init__(self, networktype = "metabolite-reaction", graph = {}):
        super().__init__(graph)
        self.net_type = networktype

    def load_from_files(self, reac_file, meta_file, matrix_file):
        meta_ids = read_file_rm(meta_file)[0]
        reac_ids, reac_attrs = read_file_rm(reac_file)
        matrix = read_file_matrix(matrix_file)
        aux_graph = get_meta_reac_graph(meta_ids, reac_ids,reac_attrs,  matrix)

        if self.net_type == "metabolite-reaction":
            self.g = aux_graph

        elif self.net_type == "reaction":
            for node in reac_ids:
                self.add_node(node)
            for r in reac_ids:
                metas = aux_graph[r]
                reacs_dest =[]
                for m in metas:
                    reacs_dest.extend([r_d for r_d in aux_graph[m] if r_d !=r])
                for new_r in reacs_dest:
                    self.add_edge(r,new_r)

        elif self.net_type =="metabolite":
            for node in meta_ids:
                self.add_node(node)
            for m in meta_ids:
                reacs = aux_graph[m]
                meta_dest=[]
                for r in reacs:
                    meta_dest.extend([m_d for m_d in aux_graph[r] if m_d!=m])
                for new_m in meta_dest:
                    self.add_edge(m,new_m)
        else:
            print("What are you doing ???")


    #auxiliar functions
def get_meta_reac_graph(meta_ids, reac_ids,reac_attrs, matrix):
    graph = MyGraph()

    for node in meta_ids + reac_ids:
        graph.add_node(node)
    for tuple in matrix:
        meta = meta_ids[int(tuple[0])]
        reac = reac_ids[int(tuple[1])]
        direction = int(tuple[2])
        lower_bound = int(reac_attrs[reac][0])
        if direction < 0 or lower_bound < 0: graph.add_edge(meta, reac)
        if direction > 0 or lower_bound < 0: graph.add_edge(reac, meta)
    return graph.g

def read_file_rm(file, sep=","):
    ids =[]
    dict={}
    with open (file) as f:
        for line in f:
            tokens= line.strip().split(sep)
            id = tokens[0]
            ids.append(id)
            dict[id]= tokens[1:]   # list from index 1 until the end
    return (ids, dict)


def read_file_matrix(file, sep="\t"):
    result =[]
    with open (file) as f:
        for line in f:
            tokens = line.strip().split(sep)
            result.append((tokens[0],tokens[1],tokens[2]))
    return result