from metabolic_network import MetabolicNetwork

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
            if(graph_list[i][0] == 'R'):
                reac.append(graph_list[i])
            elif(graph_list[i][0] == 'M'):
                meta.append(graph_list[i])
        return len(reac), len(meta)

    def perg_3(graph):
        g = graph.all_degrees()
        sort = sorted(g.items(), key=lambda x:x[1], reverse=True)
        return sort[:10]

    def perg_4(graph):
        print(graph.all_degrees(deg_type="inout"))
    
    def perg_5(graph):


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

            escolha=input('Escolha a pergunta a executar: ') 
            if escolha=='1': 
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                graph.print_graph()
            elif escolha=='2':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                print("Numero reações: ", perg_2(graph)[0])
                print("Numero metabolitos: ", perg_2(graph)[1])
            elif escolha=='3':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                print(perg_3(graph))
            elif escolha=='4':
                graph = perg_1('ijr904-metab.txt', 'ijr904-reac.txt', 'ijr904-matrix.txt')
                perg_4(graph)
            elif escolha=='0':
                print('\n Adeus!') 