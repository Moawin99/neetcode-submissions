class UnionFind:
    
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
        
    def union(self, x: int, y: int) -> bool:
        t1, t2 = self.find(x), self.find(y)
        if t1 != t2:
            if self.size[t1] < self.size[t2]:
                self.par[t1] = t2
                self.size[t2] += self.size[t1]
            else:
                self.par[t2] = t1
                self.size[t1] += self.size[t2]
            self.num_components -= 1
            return True
        return False

    def getNumComponents(self) -> int:
        return self.num_components
