from metabolic_network import *
#import numpy as np
#import matplotlib.pyplot as plt


class TestesTP:

    def __init__(self, g={}):
        self.g = g






if __name__ == "__main__":
    print("CLASSE PARA TESTE DO TP1")
    g = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D'], 'D': ['B', 'C']}


    # V1 = Vertice de inicio
    # V2 = Vertice Final

    dicVertices = g.getVertices()
    for v in dicVertices:
        if v != v1:
            if v1 in dicVertices.get(v):
                dicVertices.get(v).remove(v1)
    matriz=[]
    lista=[]
    for v in dicVertices.get(v1):
        while v != v2:
            percorrer(v,v2,dicVertices)
            lista.append(v)
        matriz.append(lista)

    print(matrizes) 











    #print("-----------------------------------------------RESPOSTA 7 ------------------------------------------------")


    #mrn = MetabolicNetwork("metabolite-reaction", {})
    #mrn.load_from_files("C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-reac.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-mat.txt")
    #print ("--------------------METABOLITE - REACTION NETWORK--------------------")
    ##print("O tamanho é de:")
    ##print(mrn.size())
    ##mrn.print_graph()


    #with open("C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/reacoes_que_geraram_metabolitos.txt", "r") as arq:
    #    for f in arq.readlines():
    #        #input_pesquisaMetabolito = input ("Introduza o metabolico na qual pretende saber quais as reacoes que o geraram \n")
    #        if(f.find("M_gln_DASH_L_c")>-1):
    #            print (f)
    









    #print("-----------------------------------------------RESPOSTA 5 ------------------------------------------------")
    #arq_matri = 'C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-mat.txt'
    #ref_arquivo = open(arq_matri,"r") 

    #arq_metabolito = 'C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt'
    #ref_arquivo_metabolito = open(arq_metabolito,"r") 
   
    #linha = ref_arquivo.readline()    
    #count__find=0

    #count = 0
    #for linha in ref_arquivo:
    #    count = count + 1
    #    caracter = "-1.0"
    #    if linha.count(caracter) == 1:
    #        texto = ref_arquivo_metabolito.readline(count)

    #        print("O ID da linha do ficheiro MATRIX que contem os metabolitos que são produzidos e não há reações que os consumam: ID = ", count, "Metabolito = ", texto)