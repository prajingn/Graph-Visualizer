class Queue:
    def __init__(self):
        self.lst = []
    
    def add(self, v):
        self.lst.append(v)
    
    def remove(self):
        return self.lst.pop(0)
    
    def isEmpty(self):
        return self.lst == []