import sys
import re
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
    mutacoes = {}
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

if __name__ == "__main__":
    filename = str(sys.argv[1])
    print('Total de mutações únicas: ' + perg_a(filename))
    perg_b(filename)
    print('Total de SNP, deleções e inserções : ' + perg_c(filename))