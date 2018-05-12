class MyGraph:

    def __init__(self, g={}):
        self.g = g


    def print_graph(self):
        [print (node, " --> " ,self.g[node]) for node in self.g.keys()]

    def get_nodes(self):
        return list(self.g.keys())

    def get_edges(self):
        return [(o, d) for o, nodes_dest in self.g.items() for d in nodes_dest]

    def add_node(self, node):
        if node not in self.g.keys():
            self.g[node]=[]

    def add_edge(self, orig, dest):
        if orig not in self.g.keys():
            self.add_node(orig)
        if dest not in self.g.keys():
            self.add_node(dest)
        if dest not in self.g[orig]:
            self.g[orig].append(dest)

    def get_successors(self, node):
        return list(self.g[node])

    def get_predecessors(self, node):
        return [node_orig for node_orig, nodes_dest in self.g.items() if node in nodes_dest]

    def get_adjacents(self, node):
        s = self.get_successors(node)
        p = self.get_predecessors(node)
        return list(set(s+p))

    def out_degree(self, node):
        return len(self.g[node])

    def in_degree(self, node):
        return len(self.get_predecessors(node))

    def degree(self, node):
        return len(self.get_adjacents(node))

    def reachableBFS (self, node):
        to_visit = [node]
        res=[]
        while to_visit:
            actual_node = to_visit.pop(0) #index required to remove the first element of the list
            if node!= actual_node : res.append(actual_node)
            to_visit.extend([elem for elem in self.g[actual_node] if elem not in res and elem not in to_visit])
        return res

    def reachableDFS (self, node):
        to_visit = [node]
        res = []
        while to_visit:
            actual_node = to_visit.pop(0)
            if node!= actual_node : res.append(actual_node)
            aux = [elem for elem in self.g[actual_node] if elem not in res and elem not in to_visit]
            to_visit = aux + to_visit
        return res


    def distance(self, orig, dest):
        if orig == dest: return 0
        l = [(orig, 0)]
        visited = [orig]
        while l:
            actual_node, dist = l.pop(0)
            for elem in self.g[actual_node]:
                if elem == dest:
                    return dist + 1
                elif elem not in visited:
                    l.append((elem, dist + 1))
                    visited.append(elem)
        return float("inf")


    def shortest_path(self, orig, dest):
        if orig == dest: return []
        l = [(orig, [])]
        visited = []
        while l:
            actual_node, path = l.pop(0)
            for elem in self.g[actual_node]:
                if elem == dest:
                    return [orig] + path + [elem]
                elif elem not in visited:
                    l.append((elem, path + [elem]))
                    visited.append(elem)
        return None


    def reachable_with_dist(self, node):
        res = []
        l = [(node, 0)]
        while len(l) > 0:
            actual_node, dist = l.pop(0)
            if actual_node != node: res.append((actual_node, dist))
            for elem in self.g[actual_node]:
                if elem not in [x[0] for x in l + res]:
                    l.append((elem, dist + 1))
        return res

    def node_has_cycle (self, node):
        l = [node]
        res = False
        visited = [node]
        while l:
            actual_node = l.pop()
            for elem in self.g[actual_node]:
                if elem == node: return True
                elif elem not in visited:
                    l.append(elem)
                    visited.append(elem)
        return res

    def has_cycle(self):
        for v in self.g.keys():
            if self.node_has_cycle(v): return True
        return False

    #aula 3
    #########################################
    def all_degrees(self, deg_type = "inout"):
        degs = {v: len(self.g[v]) if (deg_type == "out" or deg_type == "inout") else 0 for v in self.g.keys()}

        if deg_type == "in" or deg_type == "inout":
            for v in self.g.keys():
                for d in self.g[v]:
                    if deg_type == "in" or v not in self.g[d]:
                        degs[d] += 1
        return degs

    def mean_degree (self, deg_type = "inout"):
        degrees = self.all_degrees(deg_type)
        return sum(degrees.values()) / float(len(degrees))

    def prob_degree (self, deg_type = "inout"):
        degrees = self.all_degrees(deg_type)
        res={}
        for node in degrees:
            k = degrees[node]
            res[k] = 1 if k not in res.keys() else res[k]+1
        return {k: val/len(degrees) for k,val in res.items()}


    def mean_distances(self):
        tot = 0
        num_reachable = 0
        for k in self.g.keys():
            distsk = self.reachable_with_dist(k)
            for _, dist in distsk:
                tot += dist
            num_reachable += len(distsk)
        meandist = float(tot) / num_reachable
        n = len(self.get_nodes())
        return meandist, float(num_reachable) / ((n - 1) * n)

    def clustering_coef(self, v):
        adjs = self.get_adjacents(v)
        if len(adjs) == 0: return 0
        if len(adjs) == 1: return 1.0
        ligs = 0
        for i in range(0, len(adjs)):
            for j in range(i+1, len(adjs)):
                n1 = adjs[i]
                n2 = adjs[j]
                if n1 in self.g[n2] or n2 in self.g[n1]:
                    ligs += 1
        return float(ligs) / ((len(adjs) * (len(adjs) - 1))/2)

    def all_clustering_coefs(self):
        return {k:self.clustering_coef(k) for k in self.g.keys()}


    def meanClusteringCoef(self):
        ccs = self.all_clustering_coefs()
        return sum(ccs.values()) / float(len(ccs))

    def mean_clustering_per_deg(self, deg_type="inout"):
        degs = self.all_degrees(deg_type)
        ccs = self.all_clustering_coefs()
        print(degs)
        print(ccs)
        degs_node = {}
        for n in degs.keys():
            if degs[n] in degs_node.keys():
                degs_node[degs[n]].append(n)
            else:
                degs_node[degs[n]] = [n]
        print(degs_node)
        ck = {}
        for d in degs_node.keys():
            tot = sum([ccs[node] for node in degs_node[d]])
            ck[d] = float(tot) / len(degs_node[d])
        return ck

    # AULA 4
    #
    def check_balanced_node(self, node):
        pass
		
    def check_balanced_graph(self):
        pass

    #ciclo euleriano

    def eulerian_cycle(self):
        pass

    def check_nearly_balanced_graph(self):
        pass
		
    def eulerian_path(self):
        pass

    # caminhos Hamiltonianos
    def check_is_valid_path(self, path):
        pass

    def check_is_hamiltonian_path(self, path):
        pass

    def search_hamiltonian_path_from_node(self, node):
        pass
		
    def search_hamiltonian_path(self):
        pass

