from MyGraph import MyGraph

class MetabolicNetwork(MyGraph):
    def __init__(self, networktype = 'metabolite-reaction', graph = {}):
        MyGraph.__init__(self, graph)
        self.net_type = networktype

    def loadFromFiles(self, reactions_file, metabs_file, matrix_file):
        reaction_ids, reactions = read_file_rm(reactions_file)
        metab_ids, _ = read_file_rm(metabs_file)
        matrix = read_file_mat(matrix_file)
        gmr = MyGraph()

        for metab in metab_ids:
            gmr.add_node(metab)

        for reaction in reaction_ids:
            gmr.add_node(reaction)

        for index_metabolite, index_reaction, coeficient_value in matrix:
            metab_id = metab_ids[index_metabolite]
            reaction_id = reaction_ids[index_reaction]
            reaction_rev = reactions[reaction_id][0]

            if coeficient_value > 0 or reaction_rev < 0:
                gmr.add_edge(reaction_id, metab_id)
            if coeficient_value < 0 or reaction_rev < 0:
                gmr.add_edge(metab_id, reaction_id)

        if self.net_type == 'metabolite-reaction':
            self.g = gmr.g
        else:
            self.g = {}

def read_file_rm(filename, sep=','):
    identifiers = []
    attributes = {}

    with open(filename, 'r') as f:
        for line in f:
            identifier, *bounds = line.strip().split(sep)

            if len(bounds) >= 2:
                attributes[identifier] = (int(bounds[0]), int(bounds[1]))

            identifiers.append(identifier)

    return (identifiers, attributes)

def read_file_mat(filename, sep='\t'):
    res = []

    with open(filename, 'r') as f:
        for line in f:
            columns = line.strip().split(sep)
            res.append((int(columns[0]), int(columns[1]), int(columns[2])))

    return res

if __name__ == '__main__':
    mrn = MetabolicNetwork('metabolite-reaction', {})
    mrn.loadFromFiles('data/exemplo-reac.txt', 'data/exemplo-metab.txt', 'data/exemplo-mat.txt')
    print ('Metabolite-reaction network:')
    mrn.print_graph()
