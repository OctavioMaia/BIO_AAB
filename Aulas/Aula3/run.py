from metabolic_network import *

if __name__ == "__main__":

    mrn = MetabolicNetwork("metabolite-reaction", {})
    mrn.load_from_files("../data/exemplo-reac.txt", "../data/exemplo-metab.txt", "../data/exemplo-mat.txt")
    print ("Metabolite-reaction network:")
    mrn.print_graph()

    mrn2 = MetabolicNetwork("metabolite", {})
    mrn2.load_from_files("../data/exemplo-reac.txt", "../data/exemplo-metab.txt", "../data/exemplo-mat.txt")
    print ("Metabolite network:")
    mrn2.print_graph()

    mrn3 = MetabolicNetwork("reaction", {})
    mrn3.load_from_files("../data/exemplo-reac.txt", "../data/exemplo-metab.txt", "../data/exemplo-mat.txt")
    print ("Reaction network:")
    mrn3.print_graph()

    print("degrees")
    print(mrn2.all_degrees(deg_type="in"))
    print(mrn2.all_degrees(deg_type="out"))
    print(mrn2.all_degrees(deg_type="inout"))

    print("distances")
    for k in mrn2.g.keys():
        print("Node: ", k)
        print(mrn2.reachable_with_dist(k))
    print(mrn2.mean_distances())

    print("clustering")
    gr = MyGraph({1: [2], 2: [3], 3: [2, 4], 4: [2]})
    print("clustering_coef for M1: ",gr.clustering_coef(1))
    print("clustering_coef for M2: ",gr.clustering_coef(2))

    gr = MyGraph({"n1": ["n2"], "n2": ["n3"], "n3": ["n2", "n4"], "n4": ["n2"]})
    print(gr.mean_clustering_per_deg())

