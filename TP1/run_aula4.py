from assembly import *
#from OverlapGraph import *


def test1():
    seq = "CAATCATGATG"
    k = 3
    print(composition(k, seq))


def test2():
    frags = ["AAT", "ATG", "GTT", "TAA", "TGT"]
    dbgr = DeBruijnGraph(frags)
    dbgr.print_graph()


def test3():
    frags = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT",
             "TAA", "TGC", "TGG", "TGT"]
    dbgr = DeBruijnGraph(frags)
    dbgr.print_graph()


def test4():
    gr = MyGraph({1: [2], 2: [3, 1], 3: [4], 4: [2, 5], 5: [6], 6: [4]})
    gr.print_graph()
    print(gr.check_balanced_graph())
    print(gr.eulerian_cycle())


def test5():
    gr = MyGraph({1: [2], 2: [3, 1], 3: [4], 4: [2, 5], 5: [6], 6: []})
    gr.print_graph()
    print(gr.check_balanced_graph())
    print(gr.check_nearly_balanced_graph())
    print(gr.eulerian_path())


def test6():
    frags = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    dbgr = DeBruijnGraph(frags)
    dbgr.print_graph()
    print(dbgr.check_nearly_balanced_graph())
    print(dbgr.eulerian_path())


def test7():
    orig_sequence = "ATGCAATGGTCTG"
    frags = composition(3, orig_sequence)
    dbgr = DeBruijnGraph(frags)
    dbgr.print_graph()
    print(dbgr.check_nearly_balanced_graph())
    p = dbgr.eulerian_path()
    print(p)


def test8():
    frags = ["AAT", "ATG", "GTT", "TAA", "TGT"]
    ovgr = OverlapGraph(frags)
    ovgr.print_graph()


def test9():
    frags = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    ovgr = OverlapGraph(frags)
    ovgr.print_graph()


def test10():
    frags = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    ovgr = OverlapGraph(frags, True)
    ovgr.print_graph()


def test11():
    frags = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    ovgr = OverlapGraph(frags, True)
    path = ["AAT-1", "ATG-4", "TGC-13"]
    print(ovgr.check_is_valid_path(path))
    print(ovgr.check_is_hamiltonian_path(path))
    path2 = ["TAA-12", "AAT-1", "ATG-2", "TGC-13", "GCC-8", "CCA-6", "CAT-5", "ATG-3", "TGG-14", "GGG-10", "GGA-9",
             "GAT-7", "ATG-4", "TGT-15", "GTT-11"]
    print(ovgr.check_is_valid_path(path2))
    print(ovgr.check_is_hamiltonian_path(path2))


def test12():
    frags = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    ovgr = OverlapGraph(frags, True)
    path2 = ["TAA-12", "AAT-1", "ATG-2", "TGC-13", "GCC-8", "CCA-6", "CAT-5", "ATG-3", "TGG-14", "GGG-10", "GGA-9",
             "GAT-7", "ATG-4", "TGT-15", "GTT-11"]
    print(ovgr.check_is_hamiltonian_path(path2))
    print(ovgr.seq_from_path(path2))


def test13():
    frags = ["AAT", "ATG", "GTT", "TAA", "TGT"]
    ovgr = OverlapGraph(frags, False)
    ovgr.print_graph()
    print(ovgr.seq_from_path(["TAA", "AAT", "ATG", "TGT", "GTT"]))
    print(ovgr.seq_from_path(["TAA", "TGT", "ATG", "TGT", "GTT"]))


def test14():
    frags = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    ovgr = OverlapGraph(frags, True)
    print(ovgr.search_hamiltonian_path_from_node("AAT-1"))
    print(ovgr.search_hamiltonian_path_from_node("TAA-12"))
    path = ovgr.search_hamiltonian_path()
    print(ovgr.check_is_hamiltonian_path(path))
    print(ovgr.seq_from_path(path))


def test15():
    orig_sequence = "CAATCATGATGATGATC"
    frags = composition(3, orig_sequence)
    ovgr = OverlapGraph(frags, True)
    path = ovgr.search_hamiltonian_path()
    print(path)
    print(ovgr.seq_from_path(path))


if __name__ == '__main__':
    print("###   test 1   ###")
    #test1()
    print("###   test 2   ###")
    #test2()
    print("###   test 3   ###")
    #test3()
    print("###   test 4   ###")
    #test4()
    print("###   test 5   ###")
    #test5()
    print("###   test 6   ###")
    #test6()
    print("###   test 7   ###")
    #test7()
    print("###   test 8   ###")
    #test8()
    print("###   test 9   ###")
    #test9()
    print("###   test 10   ###")
    #test10()
    print("###   test 11   ###")
    #test11()
    print("###   test 12   ###")
    #test12()
    print("###   test 13   ###")
    #test13()
    print("###   test 14   ###")
    #test14()
    print("###   test 15   ###")
    #test15()