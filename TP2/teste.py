# -*- coding: utf-8 -*-
"""
@author: PedroQ
"""

#We'll use the file multiple times so it's just better to read it and save it once.
def readfile(file):
    res=[]
    fh=open(file,"r")
    line=fh.readline()
    iniSave=0 #when this becomes 1, we'll start saving lines
    while line:
        if iniSave==1:
            line= line.split()
            pos,ref,alt=line[1],line[3].upper(),line[4].upper() #we are saving the position "just because", we only really need the ref and alt
            if "," in alt:
                altSep=alt.split(",")
                for alternativa in altSep: res.append([pos,ref,alternativa])
            else: res.append([pos,ref,alt])
        if line[0:6]=="#CHROM":
            iniSave=1
        line=fh.readline()
    fh.close()
    return res

def efficientFun(matrix):
    #since we'd be accessing the same matrix over and over in each exercise, it's more efficient
    # to go through it once, even if it costs us in the readability of the function
    uniquevar={}
    variantCounter={"SNP":0,"In":0, "Del":0}    #Counter of SNP, insertions and deletions
    numberOfTransitions={}  #SNP transition counter
    res=[0,{},[]]   #res[0] will count the number of different mutations
                    #res[1] will be the number of SNP,insertions and deletions
                    #res[2] will be the matrix of SNP transitions
    for i in matrix:
        if i[1] != i[2]:
            ##########################################Exercise 1
            if (i[1],i[2]) not in uniquevar: uniquevar[(i[1],i[2])]=1
            ##########################################Exercise 2
            if len(i[2])-len(i[1])==0:  variantCounter["SNP"]+=1
            elif len(i[2])-len(i[1])>0: variantCounter["In"]+=1
            elif len(i[2])-len(i[1])<0: variantCounter["Del"]+=1
            ##########################################Exercise 3
            if len(i[2])-len(i[1])==0:
                if (i[1],i[2]) not in numberOfTransitions: numberOfTransitions[(i[1],i[2])]=1
                else:                                      numberOfTransitions[(i[1],i[2])]+=1
    res[0]=len(uniquevar)
    res[1]=variantCounter
    res[2]=numberOfTransitions
    return res

def matrixCreator(code):    #creation of a standard matrix
    matrix= [[str(0) for lin in range(5)] for col in range(5)]
    for lin in range(5):
        if lin==0:
            matrix[lin]=[" "]+ code
        for col in range(5):
            if lin>0 and col==0:
                matrix[lin][col]=code[lin-1]
    return matrix

def matrixValuesAtt(res,code):   #we now give the matrix the values of each SNP
    codeLetters = list(code)
    matrix=matrixCreator(codeLetters)
    for k in res[2]:
        for i in range(1,5):
            for j in range(i):
                if matrix[0][j]==k[1] and matrix[i][0]==k[0]: matrix[i][j]=str(res[2][k])
                if matrix[i][0]==k[1] and matrix[0][j]==k[0]: matrix[j][i]=str(res[2][k])
    return matrix

def printResolution(res,code):
    print("1.Calculate the number of unique type of variants:", res[0],"\n")
    print("2. Calculate the number of SNPs, Insertions and Deletions:", res[1],"\n")
    print("3.Considering all the SNP variants, calculate a matrix with the number of "
          "transitions between every nucleotide:")
    codeLetters=list(code)
    matrix4x4=matrixValuesAtt(res,codeLetters)
    for i in matrix4x4:print(i)
    print("\nHow to read this? \n"
          "Basically, the left column is the reference, while the first row is the alternative. "
          "\nFor example, if in the line 2 we have a C and in the row 1 an A, it means "
          "that the reference had a C and the \nalternative an A, therefore the number",matrix4x4[2][1],"is the "
          "the number of SNPs where a C was exchanged for an A.")

def saveIntoFile(info):
    f=open("ex3info.csv","w")
    for i in info:
        line=i[0]+i[1]+","+str(info[i])+"\n"
        f.write(line)
    f.close()

def saveAsMatrix(matrix):
    matToFile=[]
    for i in range(len(matrix)):
        if i>0:
            matToFile.append(matrix[i])
    matToFile=[ row[1:] for row in matToFile ]
    f=open("ex3matrix.csv","w")
    for i in matToFile:
        f.write(",".join(i)+"\n")
    f.close()

def test():
    file="HG00154.chr21.raw.vcf"
    mat=readfile(file)
    res=efficientFun(mat)
    code="ACTG"
    printResolution(res,code)
    saveIntoFile(res[2])
    mat=matrixValuesAtt(res,code)
    saveAsMatrix(mat)

test()