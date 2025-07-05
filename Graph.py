class Graph:
    def __init__(self, inp, n, directed):
        self.size = n
        self.directed = directed
        self.edgelst = inp
        self.adjlst = {}
        self.setAdjLst()

    def setAdjLst(self):
        for i in range(self.size):
            self.adjlst[i] = []

        for i, j in self.edgelst:
            if not self.directed:
                self.adjlst[i] += [j]
                self.adjlst[j] += [i]
            else:
                self.adjlst[i] += [j]

    def getAdjLst(self):
        print(f"Adj List:\n{self.adjlst}")
