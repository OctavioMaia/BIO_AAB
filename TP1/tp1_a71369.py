from metabolic_network import MetabolicNetwork
import matplotlib.pyplot as plot

class TP1:
    def perg_1(file_meta, file_reac, file_mat):
        mn = MetabolicNetwork('metabolite-reaction', {})
        mn.load_from_files(file_reac, file_meta, file_mat)
        return mn

    def perg_2(graph):
        reac=[]
        meta=[]
        graph_list = list(graph.g)
        for i in range(0, len(graph_list)):
            if(graph_list[i].startswith('R_')):
                reac.append(graph_list[i])
            elif(graph_list[i].startswith('M_')):
                meta.append(graph_list[i])
        return len(reac), len(meta)

    def perg_3(graph):
        meta={}
        graph_list = dict(graph.all_degrees())
        for k,v in graph_list.items():
            if(k.startswith('M_')):
                meta[k[2:]] = v
        sort = sorted(meta.items(), key=lambda x:x[1], reverse=True)
        return sort[:10]

    def perg_4(graph):
        d = {}
        graph_list = list(graph.g)
        for i in range(0, len(graph_list)):
            if(graph_list[i].startswith('R_')):
                degree = graph.degree(graph_list[i])
                if degree in d:
                    d[degree] = d[degree] + 1
                else:
                    d[degree] = 1
        plot.bar(range(len(d)), d.values(), align='center')
        plot.xticks(range(len(d)), d.keys())
        plot.show()

    def perg_5(graph):
        dead_ends = []
        graph_list = list(graph.g)
        for i in range(0, len(graph_list)):
            if(graph_list[i].startswith('M_')):
                if(graph.out_degree(graph_list[i])==0):
                    dead_ends.append(graph_list[i][2:])
        return dead_ends

    def perg_6(graph,uptake):
        suc= []
        uptake = input("Insira os valores pretendidos semparados por ';' (ex: M_2dhguln_c;M_maltttr_c) \n>")
        uptake =  uptake.split(";")
        metain = list(set(uptake))
        reacin = list(set([]))
        for i in range (0, len(metain)):
            reacin = graph.get_successors([metain[i]])
            for j in range (0, len (reacin)):
                if (graph.get_predecessors(reacin[j]) in metain):
                    metain = graph.get_successors(reacin[j])

    def perg_7(graph,meta):
        reac=[]
        graph_list = list(graph.g)
        for i in range(0, len(graph_list)):
            if(graph_list[i].startswith('R_')):
                if(meta in graph.get_successors(graph_list[i])):
                    reac.append(graph_list[i][2:])
        return reac

    def perg_8(graph):
        reac=set()
        graph_list = list(graph.g)
        for i in range(0, len(graph_list)):
            if(graph_list[i].startswith('R_')):
                for meta in graph.get_successors(graph_list[i]):
                    if(graph_list[i] in graph.get_successors(meta)):
                        reac.add(graph_list[i][2:])
        return reac

    def perg_9 (graph, orig, dest):
        paths = []
        past_elems = []
        orig = 'M_' + orig
        dest = 'M_' + dest
        if(orig != dest):
            if(graph.distance(orig,dest)>0):
                l = [(orig, [])]
                while(l):
                    cur, path = l.pop(0)
                    for elem in graph.g[cur]:
                        if(elem == dest):
                            paths.append([orig[2:]] + path + [elem[2:]])
                        elif(elem not in past_elems):
                            l.append((elem, path + [elem[2:]]))
                            past_elems.append(elem)
                return paths
            else: #nao existe caminho ate la
                return None
        else: #origem = destino
            return None

    def perg_10 (graph):
        ciclos = set()
        graph_list = list(graph.g)
        for i in range(0, len(graph_list)):
            if(graph.node_has_cycle(graph_list[i])):
                ciclos.add(graph_list[i][2:])
        return ciclos

    if __name__ == '__main__':
        while True:
            print()
            print('1. Cria um grafo com base na rede metabólica presente nos 3 ficheiros.')
            print('2. Qual o número de reações e metabolitos.')
            print('3. Identifica os 10 metabolitos que participam num maior número de reações.')
            print('4. Cria um gráfico com a distribuição do número de reações por cada um dos possíveis graus do tipo inout.')
            print('5. Identifica os metabolitos que são dead ends.')
            print('6. Considerando uma lista de metabolitos como uptake dado pelo utilizador, implementa uma função que retorna quais os produtos excretados pelo modelo.')
            print('7. Cria uma função que dado um metabolito dado pelo utilizador devolve a lista de reações que produzem esse metabolito.')
            print('8. Valida que no modelo não existem reações que contenham o mesmo metabolito como reagente e produto.')
            print('9. Implementa uma função que dado o metabolito origem e metabolito destino retorne todos os caminhos possíveis entre estes dois nós.')
            print('10. Implementa uma função que retorne a lista de ciclos existentes na rede.')
            print('0. Sair')
            escolha=input('Escolha a pergunta a executar: ') 
            if escolha=='1': 
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                graph.print_graph()
            elif escolha=='2':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                print('Numero reações: ', perg_2(graph)[0])
                print('Numero metabolitos: ', perg_2(graph)[1])
            elif escolha=='3':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                print(perg_3(graph))
            elif escolha=='4':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                perg_4(graph)
            elif escolha=='5':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                print('Detetados ' , len(perg_5(graph)), ' deadends: ', perg_5(graph) )
            elif escolha=='6':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                perg_6(graph,'')
            elif escolha=='7':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                meta = input('Metabolito a pesquisar: ')
                print('Reações produtoras do metabolito: ' , perg_7(graph,meta))
            elif escolha=='8':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                print('Existem ', len(perg_8(graph)), ' reações que contem os mesmos metabolitos como reagente e produto:' , perg_8(graph))
            elif escolha=='9':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                meta_orig = input('Metabolito de origem: ')
                meta_dest = input('Metabolito de destino: ')
                paths = perg_9(graph,meta_orig,meta_dest)
                for i in range(len(paths)):
                    print("Caminho", end='')
                    for j in range(len(paths[i])):
                        print(' -> ' + paths[i][j], end='')
                    print()
            elif escolha=='10':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                ciclos = perg_10(graph)
                print('Existem ' , len(ciclos) , ' ciclos na rede: ', ciclos)
            elif escolha=='0':
                print('\n Adeus!') 
                exit()