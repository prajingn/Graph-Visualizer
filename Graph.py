from utils import Queue, Stack

class Graph:
    def __init__(self, inp, n, directed):
        self.size = n
        self.directed = directed
        self.edgelst = inp
        self.adjlst = {}
        self.BFS_edge_lst = None
        self.DFS_edge_lst = None
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
        parent = {i : None for i in range(self.size)}

        q.add(v)
        visited[v] = True
        while not q.isEmpty():
            k = q.remove()
            for i in self.adjlst[k]:
                if not visited[i]:
                    visited[i] = True
                    parent[i] = k
                    q.add(i)
        
        self.BFS_edge_lst = [(j, i) for i, j in parent.items() if j is not None]
    
    #DFS
    def set_DFS(self, v):
        s = Stack()
        visited = {i : False for i in range(self.size)}
        parent = {i : None for i in range(self.size)}

        s.add(v)
        while not s.isEmpty():
            k = s.remove()
            if visited[k]:
                continue
            visited[k] = True
            for i in self.adjlst[k]:
                if not visited[i]:
                    parent[i] = k
                    s.add(i)
        
        self.DFS_edge_lst = [(j, i) for i, j in parent.items() if j is not None]
                    