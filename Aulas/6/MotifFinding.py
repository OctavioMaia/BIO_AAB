# -*- coding: utf-8 -*-
from MySeq import MySeq
from MyMotifs import MyMotifs
from random import randint
from random import random

class MotifFinding:    
    def __init__(self, size = 8, seqs = None):
        self.motifSize = size
        if (seqs != None):
            self.seqs = seqs
            self.alphabet = seqs[0].alfabeto()
        else:
            self.seqs = []
                    
    def __len__ (self):
        return len(self.seqs)
    
    def __getitem__(self, n):
        return self.seqs[n]
    
    def seqSize (self, i):
        return len(self.seqs[i])
    
    def readFile(self, fic, t):
        for s in open(fic, "r"):
            self.seqs.append(MySeq(s.strip().upper(),t))
        self.alphabet = self.seqs[0].alfabeto()
        
        
    def createMotifFromIndexes(self, indexes):
        pseqs = []
        for i,ind in enumerate(indexes):
            pseqs.append( MySeq(self.seqs[i][ind:(ind+self.motifSize)], self.seqs[i].tipo) )
        return MyMotifs(pseqs)
        
        
    # SCORES
    def score(self, s):
        score = 0
        motif = self.createMotifFromIndexes(s)
        motif.doCounts()
        mat = motif.counts
        for j in range(len(mat[0])):
            maxcol = mat[0][j]
            for  i in range(1, len(mat)):
                if mat[i][j] > maxcol: 
                    maxcol = mat[i][j]
            score += maxcol
        return score
   
    def scoreMult(self, s):
        score = 1.0
        motif = self.createMotifFromIndexes(s)
        motif.createPWM()
        mat = motif.pwm
        for j in range(len(mat[0])):
            maxcol = mat[0][j]
            for  i in range(1, len(mat)):
                if mat[i][j] > maxcol: 
                    maxcol = mat[i][j]
            score *= maxcol
        return score     
       
    # EXHAUSTIVE SEARCH
    def nextSol (self, s):
        nextS = [0]*len(s)
        pos = len(s) - 1     
        while pos >=0 and s[pos] == self.seqSize(pos) - self.motifSize:
            pos -= 1
        if (pos < 0): 
            nextS = None
        else:
            for i in range(pos): 
                nextS[i] = s[i]
            nextS[pos] = s[pos]+1;
            for i in range(pos+1, len(s)):
                nextS[i] = 0
        return nextS
        
    def exhaustiveSearch(self):
        melhorScore = -1
        res = []
        s = [0]* len(self.seqs)
        while (s!= None):
            sc = self.score(s)
            if (sc > melhorScore):
                melhorScore = sc
                res = s
            s = self.nextSol(s)
        return res

    # BRANCH AND BOUND      
    def bypass (self, s):
        res =  []
        pos = len(s) -1
        while pos >=0 and s[pos] == self.seqSize(pos) - self.motifSize:
            pos -= 1
        if pos < 0: res = None 
        else:
            for i in range(pos): res.append(s[i])
            res.append(s[pos]+1)
        return res
        
    def nextVertex (self, s):
        res =  []
        if len(s) < len(self.seqs): # internal node -> down one level
            for i in range(len(s)): 
                res.append(s[i])
            res.append(0)
        else:# bypass
            pos = len(s)-1 
            while pos >=0 and s[pos] == self.seqSize(pos) - self.motifSize:
                pos -= 1
            if pos < 0: res = None # last solution
            else:
                for i in range(pos): res.append(s[i])
                res.append(s[pos]+1)
        return res

    def branchAndBound (self):
        melhorScore = -1
        melhorMotif = None
        size = len(self.seqs)
        s = [0]*size
        while s != None:
            if len(s) < size:
                max_s_score = self.score(s) + (size-len(s)) * self.motifSize
                if max_s_score < melhorScore: 
                    s = self.bypass(s)
                else: 
                    s = self.nextVertex(s)
            else:
                sc = self.score(s)
                if sc > melhorScore:
                    melhorScore = sc
                    melhorMotif  = s
                s = self.nextVertex(s)
        return melhorMotif

   # Consensus (heuristic)
  
    def heuristicConsensus(self):
        res = [0]* len(self.seqs) 
        maxScore = -1;
        partial = [0,0]
        for i in range(self.seqSize(0)-self.motifSize):
            for j in range(self.seqSize(1)-self.motifSize):
                partial[0] = i
                partial[1] = j
                sc = self.score(partial);
                if(sc > maxScore):
                    maxScore = sc
                    res[0] = i
                    res[1] = j
        for k in range(2, len(self.seqs)):
            partial = [0]*(k+1)
            for j in range(k):
                partial[j] = res[j]
            maxScore = -1
            for i in range(self.seqSize(k)-self.motifSize):
                partial[k] = i
                sc = self.score(partial)
                if(sc > maxScore):
                    maxScore = sc
                    res[k] = i
        return res    

    # heuristic stochastic
    def heuristicStochastic (self):
        s = [0]* len(self.seqs) 
        for k in range(len(s)):
            s[k] = randint(0, self.seqSize(k)- self.motifSize)
        motif = self.createMotifFromIndexes(s)
        motif.createPWM()
        sc = self.scoreMult(s)
        bestsol = s
        mel = True
        while(mel):
            for k in range(len(s)):
                s[k] = motif.mostProbableSeq(self.seqs[k])
            if self.scoreMult(s) > sc: 
                sc = self.scoreMult(s)
                bestsol = s
                motif = self.createMotifFromIndexes(s)
                motif.createPWM()
            else: mel = False    
        return bestsol

    # gibbs sampling
    def gibbs(self, numits):
        s = []
        for k in range(len(self.seqs)):
            s.append ( randint(0, self.seqSize(k)- self.motifSize) )
        bestS = list(s)
        bestScore = self.scoreMult(s)
        for its in range(numits):
            seqi = randint(0, len(self.seqs)-1)
            seqsel = self.seqs[seqi]
            s.pop(seqi)
            removed = self.seqs.pop(seqi)
            motif = self.createMotifFromIndexes(s)            
            motif.createPWM()
            self.seqs.insert(seqi, removed)
            r = motif.probAllPositions(seqsel)
            pos = self.roulette(r)
            s.insert(seqi, pos)
            score = self.scoreMult(s)
            if score > bestScore:
                bestScore = score
                bestS = list(s)
        return bestS

    ###########################
    # END TO DO

    def roulette(self, f):
        tot = 0.0
        for x in f: tot += (0.01+x)
        val = random()* tot
        acum = 0.0
        ind = 0
        while acum < val:
            acum += (f[ind] + 0.01)
            ind += 1
        return ind-1

# tests

def test1():  
    sm = MotifFinding()
    sm.readFile("exemploMotifs.txt","dna")
    sol = [25,20,2,55,59]
    sa = sm.score(sol)
    print(sa)
    scm = sm.scoreMult(sol)
    print(scm)

def test2():
    print ("Test exhaustive:")
    seq1 = MySeq("ATAGAGCTGA","dna")
    seq2 = MySeq("ACGTAGATGA","dna")
    seq3 = MySeq("AAGATAGGGG","dna")
    mf = MotifFinding(3, [seq1,seq2,seq3])
    sol = mf.exhaustiveSearch()
    print ("Solution", sol)
    print ("Score: ", mf.score(sol))
    print("Consensus:", mf.createMotifFromIndexes(sol).consensus())

    print ("Branch and Bound:")
    sol2 = mf.branchAndBound()
    print ("Solution: " , sol2)
    print ("Score:" , mf.score(sol2))
    print("Consensus:", mf.createMotifFromIndexes(sol2).consensus())
    
    print ("Heuristic consensus: ")
    sol3 = mf.heuristicConsensus()
    print ("Solution: " , sol3)
    print ("Score:" , mf.score(sol3))

def test3():
    mf = MotifFinding()
    mf.readFile("exemploMotifs.txt","dna")
    print ("Branch and Bound:")
    sol = mf.branchAndBound()
    print ("Solution: " , sol)
    print ("Score:" , mf.score(sol))
    print("Consensus:", mf.createMotifFromIndexes(sol).consensus())

def test4():
    mf = MotifFinding()
    mf.readFile("exemploMotifs.txt","dna")
    print ("Heuristic consensus: ")
    sol3 = mf.heuristicConsensus()
    print ("Solution: " , sol3)
    print ("Score:" , mf.score(sol3))
    print ("Score mult:" , mf.scoreMult(sol3))
    
    print("Heuristic stochastic")
    sol = mf.heuristicStochastic()
    print ("Solution: " , sol)
    print ("Score:" , mf.score(sol))
    print ("Score mult:" , mf.scoreMult(sol))
    print("Consensus:", mf.createMotifFromIndexes(sol).consensus())
    
    sol2 = mf.gibbs(1000)
    print ("Score:" , mf.score(sol2))
    print ("Score mult:" , mf.scoreMult(sol2))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
