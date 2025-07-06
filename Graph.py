from utils import Queue

class Graph:
    def __init__(self, inp, n, directed):
        self.size = n
        self.directed = directed
        self.edgelst = inp
        self.adjlst = {}
        self.set_adj_lst()

    # adj_lst
    def set_adj_lst(self):
        for i in range(self.size):
            self.adjlst[i] = []

        for i, j in self.edgelst:
            if not self.directed:
                self.adjlst[i] += [j]
                self.adjlst[j] += [i]
            else:
                self.adjlst[i] += [j]

    def get_adj_lst(self):
        print(f"Adjacency list:\n{self.adjlst}")

    # BFS
    def set_BFS(self, v):
        q = Queue()
        visited = {i : False for i in range(self.size)}
        self.BFS_parent = {i : None for i in range(self.size)}

        q.add(v)
        while not q.isEmpty():
            k = q.remove()
            visited[k] = True
            for i in self.adjlst[k]:
                if not visited[i]:
                    self.BFS_parent[i] = k
                    q.add(i)
        
        self.BFS_edge_lst = [(j, i) for i, j in self.BFS_parent.items() if j != None]
    
    #DFS